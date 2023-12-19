from tkinter import Toplevel, Button

class Func():
  def __init__(self, root, label):
    self.top = Toplevel(root)
    self.button_top_level = Button(self.top, text='Нажми', command=lambda: label.config(text='Текст из модального окна')).pack()
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()