# import imp modules
import pygame
import tkinter as tkr
from  tkinter.filedialog import askdirectory
import os
#creat music player window
musicplayer = tkr.Tk()
#set a tile fow window
musicplayer.title("my player")
# set the screen dimenson of window
musicplayer.geometry('400x350') # use a quote between on dimension
# askdirectory  to choose a user music directory
directory = askdirectory()
# now interact directory to system and turn it into current directory
os.chdir(directory)    #chdir = current directory
# now creat  a song list using directory
songlist = os.listdir()# list dir is a module of os system and its showing the list of the song name
#now creat the palylist of the song and pop the window and add its function
playlist = tkr.Listbox(musicplayer,font= "Cambria 14 bold",bg ="cyan2",selectmode= tkr.SINGLE)
#selectmode is to select a song and we put it single because we play one song at one time
# now we add for loop bc songs paly in loop
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
  # initilise the py game module and add mix function to stop and play the song
pygame.init()
pygame.mixer.init()
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))# NOW WE USE ATTRUBUTE ACTIVE TO ACTIVE SONG OF PLAYLIST
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()
# now creat button
Button_play =tkr.Button(musicplayer,height=3,width= 5, text = "play music",font= "Cambria 20 bold",command = play,bg="lime green",fg ="black")
# here bg =  background and fg =  front ground
Button_stop = tkr.Button(musicplayer,height=3,width= 5, text = "stop music",font= "Cambria 20 bold",command = stop,bg="skyblue",fg ="black")
Button_pause = tkr.Button(musicplayer,height=3,width= 5, text = "pause music",font= "Cambria 20 bold",command = pause,bg="blue",fg ="black")
Button_resume = tkr.Button(musicplayer,height=3,width= 5, text = "resume music",font= "Cambria 20 bold",command = resume,bg="red",fg ="black")
Button_resume.pack(fill="x") # here fill= x mean fill text on button completely
Button_pause.pack(fill="x")
Button_stop.pack(fill="x")
Button_play.pack(fill="x")
playlist.pack(fill="both",expand  = "yes")
# now we want to creat the current song title
var =  tkr.StringVar() # Stringvar is varible which hold an  string,default value is empty string
song_title =tkr.Label(musicplayer,font = "Cambrai 12 bold ",textvariable = var)
song_title.pack()

musicplayer.mainloop()
