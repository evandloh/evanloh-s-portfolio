# 1. Import Libraries
from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from datetime import date, datetime


# 2. Create class
class AUPI:
    def __init__(self, root):
        self.root = root
        self.root.title('Advanced User Profile Interface')
        self.root.geometry('1040x700+0+0')
        self.root.configure(background='red')

        # 3. Create dictionary and read from file
        self.the_dictionary = {}
        self.read_from_file()

        # 4. Create image list
        self.image1 = PhotoImage(file='Basketball.png')
        self.image2 = PhotoImage(file='Basketball.png')
        self.image3 = PhotoImage(file='Brownie.png')
        self.image4 = PhotoImage(file='Water.png')
        self.image5 = PhotoImage(file='Basketball.png')
        self.image6 = PhotoImage(file='Basketball.png')

        self.image_list = [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6]
        self.image_index = 0

        # 5. MainFrame
        MainFrame = Frame(self.root, bd=7, bg='orange', relief=SUNKEN, width=1000, height=500)
        MainFrame.pack(side=TOP, padx=8, pady=8)

        # 6. ButtonFrame
        ButtonFrame = Frame(MainFrame, bd=7, bg='yellow', width=1000, height=125, padx=4, pady=4, relief=SUNKEN)
        ButtonFrame.pack(side=BOTTOM)

        ButtonFrame2 = Button(ButtonFrame, padx=2, font='System 10 bold', text='There is nothing to see here', bg='orange')
        ButtonFrame2.pack(fill=BOTH, expand=True, anchor=W)

        # 7. DataFrame setup
        DataFrame = Frame(MainFrame, bd=7, bg='orange', width=600, height=550, padx=4, pady=4, relief=SUNKEN)
        DataFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        # 8. Countdown Frames
        DataFrame_Two = Frame(DataFrame, bd=7, bg='darkorange3', width=300, height=500, padx=5, relief=SUNKEN)
        DataFrame_Two.pack(side=LEFT, expand=True, fill=BOTH)

        self.CountDown_Left = Frame(DataFrame_Two, bd=7, relief=RAISED, bg='lime', width=150, height=500)
        self.CountDown_Left.pack(side=LEFT, expand=True, fill=BOTH)

        self.CountDown_Right = Frame(DataFrame_Two, bd=7, relief=RAISED, bg='lime', width=150, height=500)
        self.CountDown_Right.pack(side=RIGHT, expand=True, fill=BOTH)

        # 9. Profile Frame
        Frame_One = Frame(MainFrame, bd=7, bg='orange', width=350, height=175, padx=4, pady=4, relief=SUNKEN)
        Frame_One.pack(side=TOP, fill=BOTH, expand=True)

        self.btn_back = Button(Frame_One, text='<<', command=self.back)
        self.btn_back.pack(side=LEFT)

        self.btn_for = Button(Frame_One, text='>>', command=self.forward)
        self.btn_for.pack(side=RIGHT)

        self.lblProfilePicture = Label(Frame_One, padx=2, image=self.image_list[0], width=104, height=154, bd=5, relief=RAISED, bg='black')
        self.lblProfilePicture.pack(side=LEFT, padx=8, pady=8)

        self.lblName = Label(Frame_One, padx=2, pady=15, font='System 18 bold', text='Evan Loh', bg='orange')
        self.lblName.pack(side=TOP, anchor=W)

        self.lblTitle = Label(Frame_One, padx=2, font='System 10 bold', text='7th grader', bg='orange')
        self.lblTitle.pack(anchor=W)

        self.lblMajor = Label(Frame_One, padx=2, font='System 10 bold', text='Getting to high school', bg='orange')
        self.lblMajor.pack(anchor=W)

        self.lblEmail = Label(Frame_One, padx=2, font='System 10 bold', text='evandloh@gmail.com', bg='orange')
        self.lblEmail.pack(anchor=W)

        self.lblDoB = Label(Frame_One, padx=2, font='System 10 bold', text='DOB: February 5th', bg='orange')
        self.lblDoB.pack(anchor=W)

        # 10. Chatbot Frame
        Frame_Two = Frame(MainFrame, bd=7, bg='orange', width=350, height=375, padx=4, pady=4, relief=SUNKEN)
        Frame_Two.pack(side=TOP, fill=BOTH, expand=True)

        Frame_Two_TOP = Frame(Frame_Two, bd=7, bg='tan', width=350, height=250, padx=4, pady=4, relief=SUNKEN)
        Frame_Two_TOP.pack(side=TOP)

        Frame_Two_BOT = Frame(Frame_Two, bd=7, bg='tan', width=350, height=300, padx=4, pady=4, relief=SUNKEN)
        Frame_Two_BOT.pack(side=TOP, expand=True, fill=BOTH)

        self.count = Label(Frame_Two_TOP, padx=2, font='System 10 bold', text='chatbot', bg='orange')
        self.count.pack(anchor=W)

        self.btnSend = Button(Frame_Two_BOT, text='SEND', bg='red', font='System 10 bold', padx=5, width=4, height=2, command=self.Send)
        self.btnSend.pack(side=RIGHT)

        self.InputBox = Entry(Frame_Two_BOT, text='', bg='white', font='System 10 bold')
        self.InputBox.pack(side=LEFT, expand=True, fill=BOTH)

        self.OutputBox = Label(Frame_Two_TOP, text='', width=30, height=10, bg='yellow', font='System 10 bold', wraplength=200)
        self.OutputBox.pack(fill=BOTH, expand=True)

        # 11. Load events and display countdowns
        events = self.get_events()
        today = date.today()

        for event in events:
            event_name = event[0]
            days_until = self.days_between_dates(event[1], today)
            display1 = event_name
            display2 = f'{days_until} days left'

            Label(self.CountDown_Left, text=display1, font='arial 12 bold', relief=RAISED, bd=7).pack()
            Label(self.CountDown_Right, text=display2, font='arial 12 bold', relief=RAISED, bd=7).pack()

    def read_from_file(self):
        try:
            with open('Create.txt', 'r') as file:
                for line in file:
                    line = line.rstrip('\n')
                    question, answer = line.split('/')
                    self.the_dictionary[question] = answer
        except FileNotFoundError:
            pass

    def write_to_file(self, question_item, answer_item):
        with open('Create.txt', 'a') as file:
            file.write('\n' + question_item + '/' + answer_item)

    def waithere(self):
        var = IntVar()
        self.root.after(50, var.set, 1)
        self.root.wait_variable(var)

    def Send(self):
        query = str(self.InputBox.get()).lower()
        strResponse = ''
        if query in self.the_dictionary:
            result = self.the_dictionary[query]
            for i in result:
                strResponse += i
                self.OutputBox.configure(text=strResponse)
                self.waithere()
            self.InputBox.delete(0, END)
        else:
            self.OutputBox.configure(text='Sorry I dont understand what you mean, please teach me.')
            self.InputBox.delete(0, END)
            new_answer = simpledialog.askstring('Teach me', 'Please enter what you want me to keep in memory.')
            if new_answer:
                self.the_dictionary[query] = new_answer
                self.write_to_file(query, new_answer)

    def get_events(self):
        list_events = []
        try:
            with open('events.txt', 'r') as file:
                for line in file:
                    line = line.rstrip('\n')
                    current_event = line.split(',')
                    event_date = datetime.strptime(current_event[1], '%m/%d/%y').date()
                    current_event[1] = event_date
                    list_events.append(current_event)
        except FileNotFoundError:
            pass
        return list_events

    def days_between_dates(self, date1, date2):
        return str((date1 - date2).days)

    def back(self):
        self.image_index = (self.image_index - 1) % len(self.image_list)
        self.lblProfilePicture.configure(image=self.image_list[self.image_index])

    def forward(self):
        self.image_index = (self.image_index + 1) % len(self.image_list)
        self.lblProfilePicture.configure(image=self.image_list[self.image_index])


# 3. Initiate Program
if __name__ == '__main__':
    root = Tk()
    application = AUPI(root)
    root.mainloop()
