from tkinter import *
import math

root = Tk()
root.title("Answering mathematical questions with Tkinter")
root.geometry("900x500")


# Labels
question_label = Label(root, text="What mathematical question do you want to ask (+,-,*,/): ")
number1_label = Label(root, text="Enter the first number: ")
number2_label = Label(root, text="Enter the second number: ")
answer_label = Label(root, text="The answer is: ")

# Entry boxes
input_for_the_question = Entry(root)
number1 = Entry(root)
number2 = Entry(root)

# Text box
text_box = Text(root, height=3)

def display():
    question = input_for_the_question.get()

    if "+" in question:
        answer = int(number1.get()) + int(number2.get())

    elif "-" in question:
        answer = int(number1.get()) - int(number2.get())

    elif "*" in question:
        answer = int(number1.get()) * int(number2.get())

    elif "/" in question:
        answer = int(number1.get()) / int(number2.get())

    else:
        answer = "Invalid question"

    TEXT = "The answer is: " + str(answer)

    answer_label.config(text=TEXT)
    text_box.insert(END, TEXT + "\n")

# Button
btn = Button(root, text="Calculate", command=display, height=1, bg="#1261A0", fg="white")

# Pack widgets
question_label.pack()
input_for_the_question.pack()

number1_label.pack()
number1.pack()

number2_label.pack()
number2.pack()

btn.pack()

answer_label.pack()
text_box.pack()

root.mainloop()