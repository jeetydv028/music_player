def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stopmusic():
    mixer.music.stop()
def pausemusic():
    mixer.music.pause()
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()

    song = MP3(ad)
    totalsonglength = int(song.info.length)
def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)
def createwidthes():
    #################### Labels
    TrackLavel = Label(root,text='Select Audio Track: ',bg='#5584AC',font=('arial',15,'bold'))
    TrackLavel.grid(row=0,column=0,padx=20,pady=20)

    ########################## Entry Box
    TrackLavelEntery = Entry(root,font=('arial',15,'bold'),width=35,bd=4 ,textvariable=audiotrack)
    TrackLavelEntery.grid(row=0,column=1,padx=20,pady=20)

    ####################### Buttons
    BrowseButton =  Button(root,text='search',bg='#97BFB4',font=('arial',15,'bold'),width=18 ,bd=3 ,command=musicurl)
    BrowseButton.grid(row=0,column=3,padx=20,pady=20)

    ################ PlayButton
    PlayButton = Button(root, text='Play', bg='#97BFB4', font=('arial', 15, 'bold'), width=18, bd=3,command = playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)
    ############### StopButton
    StopButton = Button(root, text='Stop', bg='#97BFB4', font=('arial', 15, 'bold'), width=18, bd=3,command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    ############## PauseButton
    PauseButton = Button(root, text='Pause', bg='#97BFB4', font=('arial', 15, 'bold'), width=18, bd=3,command=pausemusic)
    PauseButton.grid(row=1, column=1, padx=20, pady=20)

    ############## Vol-Up
    VolumeUpButton = Button(root, text='Vol +', bg='#97BFB4', font=('arial', 15, 'bold'), width=18, bd=3,command=volumeup)
    VolumeUpButton.grid(row=1, column=3, padx=20, pady=20)

    ############## Vol-Dwn
    VolumeDwnButton = Button(root, text='Vol -', bg='#97BFB4', font=('arial', 15, 'bold'), width=18, bd=3,command=volumedown)
    VolumeDwnButton.grid(row=2, column=3, padx=20, pady=20)


################################################

from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
import datetime
from mutagen.mp3 import MP3
root.geometry('1000x500+200+100')
root.title("jk music")
root.iconbitmap("music30.ico")
root.resizable(False, False)
root.configure(bg="#5584AC")
################################################# Global variable
audiotrack = StringVar()
totalsonglength=0
############################################################ create slider
ss = 'Developed by jitendra k yadav'
count = 0
text = ''
SliderLabel = Label(root,text=ss,bg='#5584AC',font=('arial', 20, 'italic bold'))
SliderLabel.grid(row=3,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTRick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text = text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text = text)
    count += 1
    SliderLabel.after(200,IntroLabelTRick)



IntroLabelTRick()
mixer.init()
createwidthes()
root.mainloop()

