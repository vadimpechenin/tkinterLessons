import tkinter as tk
from tkinter import ttk

from multiWindow.example2.config import LARGEFONT
#from multiWindow.example2.page1 import Page1
#from multiWindow.example2.page2 import Page2
import config
from multiWindow.example2.func import Func


class StartPage(tk.Frame):
    # first window frame startpage
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(config.Page1Obj))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(config.Page2Obj))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        label2 = ttk.Label(self, text='Текст', font=LARGEFONT)
        label2.grid(row=1, column=3, padx=10, pady=10)
        button = ttk.Button(self, text='openModal', command=lambda: Func(self, label2))
        button.grid(row=2, column=3, padx=10, pady=10)