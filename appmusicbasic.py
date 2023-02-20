import pygame
from pygame import mixer
from tkinter import *
import os
import threading
import time

from mutagen.mp3 import MP3
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, askquestion, showinfo
from tkinter import ttk
from PIL import Image, ImageTk

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

def prev_song():
    next_one = playlist.curselection()
    next_one = next_one[0]-1
    song = playlist.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    playlist.select_clear(0, END)
    playlist.activate(next_one)
    playlist.selection_set(next_one, last=None)

def nextsong():
    next_one = playlist.curselection()
    next_one = next_one[0]+1
    song = playlist.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    playlist.select_clear(0, END)
    playlist.activate(next_one)
    playlist.selection_set(next_one, last=None)

root=Tk()
root.title('Music player project')

#init: hàm tạo dựng, hàm tự động được gọi để phân chia bộ nhớ khi một đối tượng hay một thực thể
    # của một Lớp được khởi tạo.
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#----------playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40, height=8)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\mi_go\Music\Playlists')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

prev_song=Button(root,text="Previous",command=prev_song)
prev_song.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
prev_song.grid(row=1,column=4)

nextsong=Button(root,text="Next",command=nextsong)
nextsong.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
nextsong.grid(row=1,column=5)

mainloop()