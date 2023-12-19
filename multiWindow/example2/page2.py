import tkinter as tk
from tkinter import ttk

from multiWindow.example2.config import LARGEFONT
#from multiWindow.example2.page1 import Page21
#from multiWindow.example2.startPage import StartPage
import config


class Page2(tk.Frame):
    # third window frame page2
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(config.Page1Obj))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(config.StartPageObj))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)