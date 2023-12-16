from tkinter import *
from tkinter import ttk
import pathlib

root = Tk()
root.title('TreeView')

#Поставить иконку
def getSolutionFolder():
    return pathlib.Path(__file__).parent.parent.resolve()

path = getSolutionFolder()
file = path.joinpath("l8_9").joinpath("test_axe.ico").resolve()
root.iconbitmap(file)
root.geometry("500x760")

#Добавление стиля
style = ttk.Style()
#Добавить тему
style.theme_use("default")

#Конфигурация цветов дерева
style.configure("Treeview",
                background="silver",
                foreground="black",
                rowheight=25,
                fieldbackground="D3D3D3"
                )
#Изменить цвет выбранного элемента
style.map('Treeview', background=[('selected', 'blue')])

#создание окна
tree_frame = Frame(root)
tree_frame.pack(pady=20)

#Создание окна прокрутки
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
#Создание дерева
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set, selectmode="extended")
#Разместить дерево на экране
my_tree.pack()

#Конфигурация scrollbar
tree_scroll.config(command=my_tree.yview)

#Определим столбцы
my_tree['columns'] = ("Name", "ID","Favourite Pizza")

#Оформление столбцов
#my_tree.column("#0", width=0, minwidth=25)
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width = 120)
my_tree.column("ID", anchor=W, width = 80)
my_tree.column("Favourite Pizza", anchor=W, width = 120)

#Создание заголовков
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Favourite Pizza", text="Favourite Pizza", anchor=W)

#Наполнение данными
names = ["John", "Mary", "Tina", "Bob", "Erin", "Wes", "Tina", "Bob", "Erin","John", "Mary",
         "Tina", "Bob", "Erin", "Wes", "Tina", "Bob", "Erin"]
pizza = ["Peperroni", "Cheese", "Ham", "Supreme", "Cheese", "Onion", "Ham", "Supreme", "Cheese",
         "Peperroni", "Cheese", "Ham", "Supreme", "Cheese", "Onion", "Ham", "Supreme", "Cheese"]

#Создать чредование цвета строк
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0

for record in names:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record, count + 1, pizza[count]),
                       tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="",values=(record, count+1, pizza[count]), tags = ('oddrow',))
    count +=1
#Добавить детей
if (1==0):
    my_tree.insert(parent='', index='end', iid=6, text="Child",values=("Steve", "1.2", "Peppers"))
    #Добавить подзапись, ребенка в качестве подзаписи к 0 записи, 0 уровень
    my_tree.move('6', '0','0')


add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

#Поля для ввода
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

#Функция добавления записи
def add_record():
    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()),
                       tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(name_box.get(), id_box.get(), topping_box.get()),
                       tags=('oddrow',))
    count += 1
    #Очистить поля
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

#Удалить все записи
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

#Удалить выбранную запись
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

#Удалить много записей
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

#Select Record
def select_record():
    # Очистить пустые ячейки
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    # Сохранить номер записи
    selected = my_tree.focus()
    #Сохранить значение записи
    values = my_tree.item(selected, 'values')

    #temp_label.config(text=values)
    #вывести выделенные значения в окна
    name_box.insert(0,values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


#Сохранение обновленной записи
def update_record():
    # Сохранить номер записи
    selected = my_tree.focus()
    #Сохранить новые данные
    my_tree.item(selected, text="", values=(name_box.get(), id_box.get(),
                                            topping_box.get()))

    # Очистить пустые ячейки
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

#Создание привязки при нажатии
def clicker(event):
    select_record()

#Подняться выше
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

#Опуститься
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

#
move_up = Button(root, text="Переместиться выше", command=up)
move_up.pack(pady=10)

move_down = Button(root, text="Переместиться ниже", command=down)
move_down.pack(pady=10)

#Выделение информации
select_button = Button(root, text="Выбрать запись", command=select_record)
select_button.pack(pady=10)
#Обновление информации
update_button = Button(root, text="Обновить запись", command=update_record)
update_button.pack(pady=10)
#Кнопки
add_record = Button(root, text="Добавить запись", command=add_record)
add_record.pack(pady=10)

#Удалить все записи
remove_all = Button(root, text="Удалить все записи", command=remove_all)
remove_all.pack(pady=10)

#Удалить одну запись
remove_one = Button(root, text="Удалить выбранную запись", command=remove_one)
remove_one.pack(pady=10)

#Удалить много записей
remove_many = Button(root, text="Удалить несколько записей", command=remove_many)
remove_many.pack(pady=10)


#temp_label = Label(root, text=" ")
#temp_label.pack(pady=10)

#Привязки (Bindings)
#my_tree.bind("<Double-1>", clicker) #Двойной щелчек
my_tree.bind("<ButtonRelease-1>", clicker) #просто щелчек

root.mainloop()