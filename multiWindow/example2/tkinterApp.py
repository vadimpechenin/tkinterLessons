import tkinter as tk

from multiWindow.example2.page1 import Page1
from multiWindow.example2.page2 import Page2
from multiWindow.example2.startPage import StartPage
import config

class TkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        index = 0
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[frame] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            if (index==0):
                config.StartPageObj = frame
            elif (index==1):
                config.Page1Obj = frame
            else:
                config.Page2Obj = frame
            index += 1

        self.show_frame(config.StartPageObj)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()