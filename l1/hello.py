from tkinter import *
#Базовое окно
root = Tk()

#Основной цикл создания виджета (элемента) на экране
#Создание виджета
myLabel = Label(root, text = "Hello World!")
#Положили виджет на экран
myLabel.pack()

root.mainloop()