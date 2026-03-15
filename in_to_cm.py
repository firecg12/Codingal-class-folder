# converting inches to centimeters using Tkinter
from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x300")

frame = Frame(master=root, height=120, width=350, bg='lightblue')
frame.place(x=25, y=20)

lbl = Label(frame, text="Enter Measurement (in)", bg="#3895D3", fg="white")
lbl.place(x=20, y=20)

user_entry = Entry(frame)
user_entry.place(x=180, y=20)

cm = 2.54

textbox = Text(root, bg="black", fg="white", height=5, width=35)
textbox.place(x=60, y=170)

def logic():
    try:
        user = float(user_entry.get())
        calculation = user * cm
        conversion = f"{user} in is equal to {calculation} cm\n"
        textbox.insert(END, conversion)
    except:
        textbox.insert(END, "Please enter a valid number\n")

btn = Button(frame, text="Convert", command=logic, bg="red", fg="white")
btn.place(x=140, y=70)

root.mainloop()
