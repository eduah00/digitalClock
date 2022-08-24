from tkinter import BOTH, RIGHT, X, Tk
from tkinter import Label, Frame, Button, Canvas
import time
import sys

master = Tk()
master.title("Digital Clock")

def move_window(event):
    master.geometry('+{0}+{1}'.format(event.x_master, event.y_master))

master.overrideredirect(True) # turns off title bar, geometry
master.geometry('400x100+200+200') # set new geometry

# make a frame for the title bar
title_bar = Frame(master, bg='black', relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, text='X', command=master.destroy)

# a canvas for the main area of the window
#window = Canvas(master, bg='black')

# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
#window.pack(expand=1, fill=BOTH)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)

def update_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, update_time)

# Create a label widget
clock = Label(master, font=("MicroExtendFLF", 75, "bold"), bg="black", fg="white")
#Adds clock to the screen
clock.pack()

update_time()

master.mainloop()