from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title("")
root.geometry("500x250")
root.iconbitmap("heart.ico")

Text = Label(text="You matter", font=("Arial", 18))
Text.place(relx=0.5,
           rely=0.5,
           anchor="center")

root.mainloop()
