from tkinter import Tk, Toplevel, Button, Label
from func import Func

root = Tk()
label = Label(root, text='Текст')
label.pack()
button = Button(root, text='openModal', command=lambda: Func(root, label)).pack()
root.mainloop()