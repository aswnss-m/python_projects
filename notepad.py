from tkinter import *
import pyperclip
# initiallisation of the tkinter widget

class Notepad:
    def __init__(self, width = 800, height = 800):
	    self.width = width
	    self.height = height
	    self.root = Tk()
	    self.root.geometry("{}x{}".format(self.width, self.height))
	    self.root.columnconfigure(1, weight = 3)
	    self.entry1 = Text(self.root, width = self.width, height = self.height)
	    self.entry1.pack()
	    menubar = Menu(self.root)
	    filemenu = Menu(menubar, tearoff = 0)
	    filemenu.add_command(label = 'Save', command = self.save_window)
	    filemenu.add_command(label = 'Open  (beta)',command=self.open)
	    filemenu.add_command(label = 'Encrypt',command=self.encrypt)
	    filemenu.add_separator()
	    filemenu.add_command(label="Quit",command=self.Quit)

	    editmenu = Menu(menubar,tearoff=0)
	    editmenu.add_command(label="Copy",command=self.copy)
	    editmenu.add_command(label="Paste",command=self.paste)
	    menubar.add_cascade(label = "File", menu = filemenu)
	    menubar.add_cascade(label="Edit",menu=editmenu)
	    self.root.config(menu = menubar)
	    self.root.mainloop()
    def save_window(self):
	    self.window = Tk()
	    self.window.geometry('300x100')
	    self.window.columnconfigure(0, weight = 1)
	    self.window.columnconfigure(1, weight = 2)
	    self.window.title("Save!!")
	    label1 = Label(self.window, text = "FileName : ", padx = 5, pady = 5)
	    self.file = Entry(self.window)
	    savebut1 = Button(self.window, text = "Save", command =  self.call)
	    savebut2 = Button(self.window, text = "Close", command = self.window.destroy)

	    label1.grid(row=0,column=0)
	    self.file.grid(row=0,column=1,sticky=E+W)
	    savebut1.grid(row=1,column=0)
	    savebut2.grid(row=1,column=1)
	    self.content = self.entry1.get(1.0, "end-1c")
	    self.window.mainloop()
    def call(self):
	    self.filename = self.file.get() + '.txt'
	    try:
		    f= open(self.filename,"x")
		    f.close()
		    self.write_over()
		    self.window.destroy()
	    except FileExistsError:
		    self.warn()
    def warn(self):
    	warn_window = Tk()
    	warn_window.configure(padx = 10, pady = 10)
    	warn_window.title("Warning!!")
    	warn1 = Label(warn_window, text = "File Already Exist!", font = ("Ubuntu bold", 15))
    	warnbut1 = Button(warn_window, text = "overwrite", command = self.write_over)
    	warnbut2 = Button(warn_window, text = "Append", command = self.append_over)
    	warnbut3 = Button(warn_window, text = "Close", command = warn_window.destroy)
    	warn1.grid(row = 0, column = 0, columnspan = 3, ipady = 5)
    	warnbut1.grid(row = 1, column = 0)
    	warnbut2.grid(row = 1, column = 1)
    	warnbut3.grid(row = 1, column = 2)
    	warn_window.mainloop()
    def write_over(self):
    	f = open(self.filename, "w")
    	f.write(self.content)
    	f.close()
    def append_over(self):
    	f = open(self.filename, "a")
    	f.write(self.content)
    	f.close()
    def Quit(self):
    	quitwindow = Tk()
    	quitwarning = Label(quitwindow,text="You will lose this Document if you havent saved Them!!",font=("Arial Black",20),fg='red',bg='white')
    	quitwarning.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    	quitbut1 = Button(quitwindow,text="Back !!",command = quitwindow.destroy)
    	quitbut2 = Button(quitwindow,text="Close Anyway !!", command = self.root.quit)
    	quitbut1.grid(row=1,column=0,columnspan=2,sticky=E+W)
    	quitbut2.grid(row=1,column=2,sticky=E+W)
    	quitwindow.mainloop()

    def copy(self):
    	text = self.entry1.get(1.0,"end-1c")
    	pyperclip.copy(text)
    def paste(self):
    	if pyperclip.paste()=="":
    		pass
    	else:
    		text= self.entry1.get(1.0,"end-1c")
    		self.entry1.delete(1.0,"end-1c")
    		self.entry1.insert(1.0,"{} \n {}".format(text,pyperclip.paste()))

    def encrypt(self):
    	self.message = self.entry1.get(1.0,"end-1c")
    			#All the alphabets are included in this , can be used to find the next 5th charactor
    	keys = "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"

		# The encrpted message is stored in this variable
    	self.temp =""

		#traverse through all the charactors of the entered message
    	for i in self.message:
				#traverse through all the alphabets to find the matching pair
    		for x in keys:

				#if the message has any numbers , then we need to filter it out 
    			
    			if i in keys:
    				if i =='W':
    					self.temp += 'A'
    					break
    				elif i =='X':
    					self.temp += 'B'
    					break
    				elif i =='Y':
    					self.temp += 'C'
    					break
    				elif i =='Z':
    					self.temp += 'D'
    					break

    				elif i == ' ':
    					self.temp += '  '
    					break
    				elif i == x:
    					pos = keys.index(x)
    					self.temp += keys[pos+5] #this gets the next 5th element 

    	self.entry1.delete(1.0,"end-1c")
    	self.entry1.insert(1.0,self.temp)

################################################################################3
    def open(self):
    	self.openwindow = Tk()
    	self.openwindow.title("Open")
    	label1 = Label(self.openwindow,text="This is in beta stage!!!!")
    	label2 = Label(self.openwindow,text="Filename: ")
    	self.openfilename = Entry(self.openwindow)
    	but1 = Button(self.openwindow,text="Open",command=self.openfunc)
    	but2 = Button(self.openwindow,text="Clear",command= lambda : self.openfilename.delete(0,"end"))

    	label1.grid(row=0,column=0,columnspan=3,sticky=E+W)
    	label2.grid(row=1,column=0,sticky= E+W)
    	self.openfilename.grid(row=1,column=1,columnspan=2,sticky=E+W)
    	but1.grid(row=2,column=0,columnspan=2,sticky =E+W)
    	but2.grid(row=2,column=2,sticky =E+W)
    	self.openwindow.mainloop()
    def openfunc(self):
    	try:
    		f=open(self.openfilename.get(),"r")
    		text = f.read()
    		self.entry1.insert(1.0,text)
    		self.openwindow.destroy()
    		f.close()
    	except FileNotFoundError:
    		self.openfilename.delete(0,"end")
    		self.openfilename.insert(0,"File Not Found")


    	



Notepad(800, 800)












