from tkinter import *
import random

counter = 1


def click():
    global counter
    if counter == 1:
        btn_main['text'] = 'PLEASE DONT CLICK!'
        btn_main.place(x=50, y=90, width=400, height=30)
        counter = counter + 1
    elif counter == 2:
        btn_main['text'] = 'you might be dying to click this button....still don"t'
        btn_main.place(x=50, y=90, width=400, height=30)
    elif counter == 3:
        btn_main['text'] = 'someting wrong might happen if you click this button (you will get hacked)'
        btn_main.place(x=60, y=20, width=400, height=30)
    elif counter == 4:
        btn_main['text'] = 'Stop, its making the system go WeIrD'
        btn_main.place(x=30, y=2, width=400, height=30)
    elif counter == 5:
        btn_main['text'] = 'STOP CLICKING THE BUTTON'
        btn_main.place(x=345, y=200, width=400, height=30)
    elif counter == 6:
        btn_main['text'] = 'I DONT WANT TO BE CLICKED'
        btn_main.place(x=310, y=90, width=400, height=30)
    elif counter == 7:
        btn_main['text'] = 'I CANT TAKE IT ANYMORE'
        btn_main.place(x=120, y=70, width=400, height=30)
    elif counter == 8:
        btn_main['text'] = 'you better not click'
        btn_main.place(x=170, y=59, width=400, height=30)
    elif counter == 9:
        btn_main['text'] = 'no clicky'
        btn_main.place(x=60, y=49, width=400, height=30)


window = Tk()
window.title(text="Don't click me")
window.geometry('700x800')

btn_main = Button(text='DONT CLICK', command=click)
btn_main.place(x=50, y=90, width=200, height=30)

window.mainloop()
