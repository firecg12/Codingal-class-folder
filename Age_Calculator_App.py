from tkinter import *
from datetime import date

root = Tk()
root.title("Login App")
root.geometry('800x800')

frame = Frame(master=root, height=260, width=360, bg='lightblue')

lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text="Birth Month", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Birth Day", bg="#3895D3", fg="white", width=12)
lbl4 = Label(frame, text="Birth Year", bg="#3895D3", fg="white", width=12)

name_entry = Entry(frame)
month_entry = Entry(frame)
day_entry = Entry(frame)
year_entry = Entry(frame)

textbox = Text(root, height=10, width=60, bg="black", fg="white")


def display():
    name = name_entry.get()
    month = month_entry.get()
    day = day_entry.get()
    year = year_entry.get()

    if month == "" or day == "" or year == "":
        textbox.insert(END, "\nPlease fill all the birth date fields.\n")
        return

    month = int(month)
    day = int(day)
    year = int(year)

    today = date.today()
    birthdate = date(year, month, day)

    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    greet = "\nHey " + name + "!"
    message = "\nCongratulations! You are " + str(age) + " years old."

    textbox.insert(END, greet)
    textbox.insert(END, message)

btn = Button(root, text="Calculate age", command=display, bg="red")

frame.place(x=20, y=0)

lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x=20, y=80)
month_entry.place(x=150, y=80)

lbl3.place(x=20, y=140)
day_entry.place(x=150, y=140)

lbl4.place(x=20, y=200)
year_entry.place(x=150, y=200)

btn.place(x=120, y=240)

textbox.place(x=20, y=280)

root.mainloop()

