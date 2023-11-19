from tkinter import *

window = Tk()

window.config(background="black")

icona = PhotoImage(file="icona.png")

label = Label(window,
              text="Hello World",
              font=("Arial",
                    40,
                    "bold",
                    "underline"),
              bg="dark red",
              fg="red",
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=icona,
              compound="bottom")

count = 0


def click():

    global count
    count += 1
    print(count)


like = PhotoImage(file="like.png")

button = Button(window,
                text="Click me",
                command=click,
                font=("Comic Sans", 30),
                fg="red",
                bg="black",
                activeforeground="black",
                activebackground="black",
                image=like,
                compound="top")

entry = Entry(window,
              font=("Arial", 30),
              fg="dark red",
              bg="silver")

password = Entry(window,
                 font=("Arial", 30),
                 fg="dark red",
                 bg="silver",
                 show="*")


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


submit_btn1 = Button(window,
                     text="Submit",
                     command=submit)


delete_btn1 = Button(window,
                     text="Delete",
                     command=delete)


backspace_btn1 = Button(window,
                        text="Backspace",
                        command=backspace)


label.pack()
button.pack()
entry.pack(side=LEFT)
submit_btn1.pack(side=RIGHT)
delete_btn1.pack(side=RIGHT)
backspace_btn1.pack(side=RIGHT)
password.pack()


window.mainloop()
