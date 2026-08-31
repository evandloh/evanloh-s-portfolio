from tkinter import Tk, Canvas
from datetime import date, datetime


def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.striptime(current_event[1], '%m/%d/%y').deate()
            current_event[1] = event_date
            list_events.append(current_event)
    return (current_event)


root = Tk()

c = Canvas(root, width=800, height=800, bg='black')
c.pack()

c.create_text(100, 50, anchor='w', fill='blue',
              font='Arial 28 bold underline',
              text='My Countdown Calender')
