from tkinter import *

root = Tk()
root.title("Login App")
root.geometry('800x800')

frame = Frame(master=root, height=200, width=360, bg='lightblue')
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text="Email ID", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Password", bg="#3895D3", fg="white", width=12)
def display():
    name = name_entry.get()
    greet = "\nHey "+name+"!"
    message = "\nCongratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#000000", fg="white")

btn = Button(text = "Create Account", command=display, bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()


