from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
			background = 'tomato',
			foreground = 'white')
lbl.pack(anchor = 'center')
time()

mainloop()
