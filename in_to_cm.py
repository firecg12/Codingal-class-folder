# converting inches to centimeters using Tkinter
from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg='lightblue')
frame.place(x=120, y=50)

lbl = Label(frame, text="Enter Measurement (in)", bg="#3895D3", fg="white")
lbl.place(x=20, y=20)

user_entry = Entry(frame)
user_entry.place(x=180, y=20)

cm = 2.54

textbox = Text(root, bg="#000000", fg="white", height=5, width=40)
textbox.place(x=120, y=200)

def logic():
    user = float(user_entry.get())   # convert text to number
    calculation = user * cm
    conversion = str(user) + " in is equal to " + str(calculation) + " cm\n"
    textbox.insert(END, conversion)

btn = Button(root, text="Convert", command=logic, bg="red")
btn.place(x=250, y=150)

root.mainloop()
