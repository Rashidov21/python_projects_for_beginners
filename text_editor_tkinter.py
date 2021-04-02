from tkinter import *

root = Tk() 
root.geometry("350x250") 
root.title("Sticky Notes") 
root.minsize(height=250, width=350) 
root.maxsize(height=250, width=350) 


# adding scrollbar 
scrollbar = Scrollbar(root) 

# packing scrollbar 
scrollbar.pack(side=RIGHT, 
			fill=Y) 


text_info = Text(root, 
				yscrollcommand=scrollbar.set) 
text_info.pack(fill=BOTH) 

# configuring the scrollbar 
scrollbar.config(command=text_info.yview) 

root.mainloop() 
