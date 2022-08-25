from tkinter import *
import time
import sys

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Frame
        container = Frame(self, bg='black')
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    ################################################################################################
        

        self.overrideredirect(True) # turns off title bar, geometry
        self.geometry('900x150') # set new geometry

        # make a frame for the title bar
        title_bar = Frame(self, bg='black', relief='sunken', bd=0)

        # Make a label for the title
        titleLabel = Label(title_bar, text="", font=("Helvetica", 10), fg="white", bg="black")
        titleLabel.pack(side=LEFT, anchor=N, padx=15)

        def on_enter(e):
            close_button['background'] = 'red'

        def on_leave(e):
            close_button['background'] = 'black'

        # put a close button on the title bar
        close_button = Button(title_bar, text='X', command=self.destroy, activebackground='red', bg='black', fg='white', relief='sunken', bd=0)


        # pack the widgets
        title_bar.pack(expand=1, fill=BOTH)
        close_button.pack(side=RIGHT, padx=4)

        # bind title bar motion to the move window function
        title_bar.bind('<B1-Motion>', move_window)
        # bind the close button to the mouses hover to change the color of background
        close_button.bind("<Enter>", on_enter)
        close_button.bind("<Leave>", on_leave)

    ################################################################################################
    




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
        clock_page.pack(side=LEFT, padx=130)
        timer_page = Button(self, text="Timer", font=("Helvetica", 45), bg="black", fg="white", bd=0,command=lambda: controller.show_frame(TimerPage))
        timer_page.pack(side=RIGHT, padx=130)


class ClockPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to the Clock", font=("Helvetica", 20))
        label.pack(pady=10, padx=10)

class TimerPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to the Timer", font=("Helvetica", 20))
        label.pack(pady=10, padx=10)







# master = Tk()
# master.title("Digital Clock")

# #Moves the window accroding to the mouse position
def move_window(event):
    app.geometry(f'+{event.x_root}+{event.y_root}')

# master.overrideredirect(True) # turns off title bar, geometry
# master.geometry('900x150') # set new geometry

# # make a frame for the title bar
# title_bar = Frame(master, bg='black', relief='sunken', bd=0)

# # Make a label for the title
# titleLabel = Label(title_bar, text="", font=("Helvetica", 10), fg="white", bg="black")
# titleLabel.pack(side=LEFT, padx=15)

# def on_enter(e):
#     close_button['background'] = 'red'

# def on_leave(e):
#     close_button['background'] = 'black'

# # put a close button on the title bar
# close_button = Button(title_bar, text='X', command=master.destroy, activebackground='red', bg='black', fg='white', relief='sunken', bd=0)


# # pack the widgets
# title_bar.pack(expand=1, fill=BOTH)
# close_button.pack(side=RIGHT, padx=4)

# # bind title bar motion to the move window function
# title_bar.bind('<B1-Motion>', move_window)
# # bind the close button to the mouses hover to change the color of background
# close_button.bind("<Enter>", on_enter)
# close_button.bind("<Leave>", on_leave)

# #Method that updates the clock label with the current time every 200 milliseconds
# def update_time():
#     timeVar = time.strftime("%I:%M:%S %p")
#     clock.config(text=timeVar)
#     clock.after(200, update_time)

# # Create a label widget
# clock = Label(master, font=("Helvetica .Black", 90, "bold"), bg="black", fg="white")
# #Adds clock to the screen
# clock.pack(expand=1, fill=BOTH)

# update_time()

#master.mainloop()

app = App()
app.mainloop()