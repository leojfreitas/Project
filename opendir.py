from tkinter import *
from tkinter import filedialog

root=Tk()

def opendir():
	dirr=filedialog.askopenfilename(title="Open", initialdir="C:/", filetypes=(("só excel","*.xlsx"),("todos", "*.*")))

	print(dirr)

Button(root, text="Open dir", command=opendir).pack()
	

root.mainloop()