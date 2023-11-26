from tkinter import *
#Базовое окно
root = Tk()

#Основной цикл создания виджета (элемента) на экране
#Создание виджета
myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text = "My Name Is Vadim Pechenin")
#myLabel3 = Label(root, text = "              ")

#myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
#myLabel3.grid(row=1, column=1)

root.mainloop()