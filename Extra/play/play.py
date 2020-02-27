from tkinter import *
# import tkSnack
import os
import time

root =Tk()

# file="music.wav"
files=["music.wav","nupur.mp3"]

for file in files:
    os.system(file)
    time.sleep(20)


root.mainloop()