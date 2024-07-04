import tkinter

screen=tkinter.Tk()
screen.title("MyApp")
screen.geometry("400x600")
screen.config(background='lightblue')

"""lbl=tkinter.Label(text="Firstname")
lbl.pack()"""

#tkinter.Label(text="Firstname").pack()

"""lbl=tkinter.Label(text="Firstname")
lbl.pack()

lbl=tkinter.Label(text="Lastname")
lbl.pack()"""


"""lblf=tkinter.Label(text="Firstname")
lblf.place(x=0,y=0)

lbll=tkinter.Label(text="Lastname")
lbll.place(x=0,y=30)"""

lblf=tkinter.Label(text="Firstname")
lblf.grid(row=0,column=0)

lbll=tkinter.Label(text="Lastname")
lbll.grid(row=1,column=0)


screen.mainloop()