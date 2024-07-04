import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()

screen.title("FinalApp")
screen.geometry('400x600')
screen.config(bg='lightblue')

fnm_lbl=tkinter.Label(text="Firstname:",bg='lightblue',fg='red',font='Ebrima 15 bold')
fnm_lbl.grid(row=0,column=0,sticky='W')

lnm_lbl=tkinter.Label(text="Lastname:",bg='lightblue',fg='red',font='Ebrima 15 bold')
lnm_lbl.grid(row=1,column=0,sticky='W')

txt_lnm=tkinter.Entry()
txt_lnm.grid(row=1,column=1,sticky='W')

txt_fnm=tkinter.Entry()
txt_fnm.grid(row=0,column=1,sticky='W')

ml=tkinter.Radiobutton(value=0, text='Male',bg='lightblue',fg='red',font='Ebrima 15 bold')
ml.grid(row=2,column=0,sticky='W')

fml=tkinter.Radiobutton(value=1,text='Female',bg='lightblue',fg='red',font='Ebrima 15 bold')
fml.grid(row=2,column=1,sticky='W')

ch1=tkinter.Checkbutton(text="HTML",bg='lightblue',fg='red',font='Ebrima 15 bold').grid(row=3,column=0,sticky='W')
ch2=tkinter.Checkbutton(text="Python",bg='lightblue',fg='red',font='Ebrima 15 bold').grid(row=4,column=0,sticky='W')
ch3=tkinter.Checkbutton(text="JAVA",bg='lightblue',fg='red',font='Ebrima 15 bold').grid(row=5,column=0,sticky='W')
ch4=tkinter.Checkbutton(text="iOS",bg='lightblue',fg='red',font='Ebrima 15 bold').grid(row=6,column=0,sticky='W')


city=['Ahmedabad','Rajkot','Surat','Baroda','Jamnagar']
ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

def btnclick():
    print("This is button!")

    #messagebox.showerror('Error','Something went wrong...Try again!')
    #messagebox.showinfo('Success','Your data has been saved!')
    #messagebox.showwarning('Warning','Disk is full!')

    print("Firstname:",txt_fnm.get())
    print("Lastname:",txt_lnm.get())

tkinter.Button(command=btnclick ,text="Submit",font='Ebrima 15 bold').place(x=170,y=350)

screen.mainloop()