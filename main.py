from tkinter import *

window = Tk()

photo = PhotoImage(file="icona.png")

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
              image=photo,
              compound="bottom")

window.config(background="black")
label.pack()

window.mainloop()