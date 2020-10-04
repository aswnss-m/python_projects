from tkinter import *

root = Tk() #initialises the tkinter screen 
root.configure(background='black') #sets the properties of the window
root.geometry('800x800') #this specifies the window size 

root.title("Welcome to the world of tkinter") #sets the title of the screen

#Label(root, text="Hello").grid(column=2 , row=3) 
#This is used to insert text inside the window of the tkinter
label1=Label(root,text="Hello world")
label1.grid(row=3,column=2)


label2=Label(root,text="Hello world",font=("Ubuntu Bold" , 72))
label2.grid(row=4,column=2)

label3=Label(root,text="Hello world",font=("Ubuntu" , 72))
label3.grid(row=5,column=2)

def click():
	btn.configure( text="clicked", bg="red")

btn = Button(root, text="I am a button", width= 20 , font =("Ubuntu" , 10), command = click)
btn.grid(row=6 , column=2)

btn2 = Button(root, text="I am a button", width= 20 , font =("Ubuntu" , 10) ,fg="blue",bg="yellow")
btn2.grid(row=7 , column=2)

text = Entry(root , width = 20)
text.grid(row=8, column=2)




root.mainloop()