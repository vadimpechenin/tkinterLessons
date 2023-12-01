from tkinter import *
import pathlib
from PIL import ImageTk, Image



root = Tk()
root.title("Simple Calculator")

#Поставить иконку
def getSolutionFolder():
    return pathlib.Path(__file__).parent.resolve()

path = getSolutionFolder()
file = path.joinpath("test_axe.ico").resolve()
root.iconbitmap(file)

#Расположить картинку
file_img = path.joinpath("images").joinpath("test.png").resolve()
my_img1 = ImageTk.PhotoImage(Image.open(file_img))
file_img = path.joinpath("images").joinpath("test2.png").resolve()
my_img2 = ImageTk.PhotoImage(Image.open(file_img))

image_list = [my_img1, my_img2]

my_label = Label(image = my_img1, width=500, height=500)
my_label.grid(row=0, column = 0, columnspan = 3)


def forward(image_number: int):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number], width=500, height=500)
    button_forward = Button(root, text=">>", command = lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command = lambda: back(image_number-1))

    if image_number == 1:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row=1, column=2)

def back(image_number: int):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number], width=500, height=500)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command = back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text=">>", command = lambda: forward(1))

button_back.grid(row = 1, column = 0)
button_quit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)

root.mainloop()