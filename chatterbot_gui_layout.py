# 1 Import librarys
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import Tk, simpledialog, messagebox

# 2 Start
root = Tk()
root.title('Chatter Bot')

# 3 Make frames
MainFrame = Frame(root, bd=7, bg='powder blue', relief=RAISED)
MainFrame.pack()

TopFrame = Frame(MainFrame, bd=7, relief=RAISED,
                 width=250, height=150, bg='powder blue')
TopFrame.pack(side=TOP, fill=BOTH, expand=True)

BotFrame = Frame(MainFrame, bd=7, bg='powder blue',
                 width=250, height=50, relief=RAISED)
BotFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

# 4 Create label and widget
OutputBox = Label(TopFrame, width=30, height=10, bd=7,
                  bg='cornsilk', text='',
                  font='system 10 bold',
                  wraplength=200)
OutputBox.pack(fill=BOTH, expand=True)

EntryBox = Entry(BotFrame, bd=4, bg='cornsilk', text='',
                 font='system 10 bold')
EntryBox.pack(side=LEFT, fill=BOTH, expand=True)

btnSend = Button(BotFrame, bd=4, bg='red',
                 text='SEND', width=5, height=1,
                 font='System 10 bold')
btnSend.pack(side=RIGHT)
