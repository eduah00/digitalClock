from tkinter import *
import time
import sys
from typing import Container
from tkinter import messagebox

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Frame
        container = Frame(self)
        container.pack(side="bottom")
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)        


        self.frames = {}

        for F in (StartPage, ClockPage, TimerPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Creates button to navigate to the clock page or the timer page
        clock_page = Button(self, text="Clock", font=("Helvetica", 45), bg="black", fg="white", bd=0,command=lambda: controller.show_frame(ClockPage))
        clock_page.pack(side=LEFT, padx=130, expand=3)
        timer_page = Button(self, text="Timer", font=("Helvetica", 45), bg="black", fg="white", bd=0,command=lambda: controller.show_frame(TimerPage))
        timer_page.pack(side=RIGHT, padx=130)


class ClockPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def update_time():
            timeVar = time.strftime("%I:%M:%S %p")
            clock.config(text=timeVar)
            clock.after(200, update_time)

        # Create a label widget
        clock = Label(self, font=("Helvetica .Black", 90, "bold"), bg="black", fg="white")
        #Adds clock to the screen
        clock.pack(side=BOTTOM, expand=1, fill=X)

        update_time()

class TimerPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        hourString = StringVar()
        minuteString = StringVar()
        secondString = StringVar()

        ### Set strings to default value
        hourString.set("00")
        minuteString.set("00")
        secondString.set("00")

        ### Get user input
        hourTextbox = Entry(self, width=3, font=("Helvetica .Black", 90, "bold"), textvariable=hourString, bg="black", fg="white")
        minuteTextbox = Entry(self, width=3, font=("Helvetica .Black", 90, "bold"), textvariable=minuteString, bg="black", fg="white" )
        secondTextbox = Entry(self, width=3, font=("Helvetica .Black", 90, "bold"), textvariable=secondString, bg="black", fg="white" )

        ### Center textboxes
        hourTextbox.pack(side=LEFT, padx=10)
        minuteTextbox.pack(side=LEFT, padx=25)
        secondTextbox.pack(side=LEFT, padx=50)

        def runTimer():
            try:
                clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
            except:
                print("Incorrect values")

            while(clockTime > -1):
                
                totalMinutes, totalSeconds = divmod(clockTime, 60)

                totalHours = 0
                if(totalMinutes > 60):
                    totalHours, totalMinutes = divmod(totalMinutes, 60)

                hourString.set("{00:2d}".format(totalHours))
                minuteString.set("{00:2d}".format(totalMinutes))
                secondString.set("{00:2d}".format(totalSeconds))

                ### Update the interface
                self.update()
                time.sleep(1)

                ### Let the user know if the timer has expired
                if(clockTime == 0):
                    messagebox.showinfo("", "Your time has expired!")

                clockTime -= 1


        setTimeButton = Button(self, text='Set Time', bd='5', command=runTimer)
        setTimeButton.pack(side=BOTTOM, padx=10, pady=10)





def move_window(event):
    app.geometry(f'+{event.x_root}+{event.y_root}')


app = App()
app.configure(bg="Blue")
app.mainloop()