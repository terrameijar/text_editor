# TextEditor

import Tkinter
from Tkinter import *
from ScrolledText import * #  Tkinter textarea does not provide scrolling
import tkFileDialog
import tkMessageBox
root = Tkinter.Tk(className=" Text Editor")
textPad = ScrolledText(root, width=80, height=30)


def dummy():
	print "Stub to be removed"


def save_command(self):
	file = tkFileDialog.asksaveasfile(mode='w')
	if file is not None:
		# slice off last char from GET as an extra return is added
		data = self.textPad.get('1.0', END + '-1c')
		file.write(data)
		file.close()


def exit_command():
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()


def about_command():
	label = tkMessageBox.showinfo("About", "Text Editor by Terrameijar"
		                             "\n Copyright \nNo rights left to reserve")


def open_command():
	file = tkFileDialog.askopenfile(parent=root, mode='rb', title="Select a file")
	if file is not None:
		contents = file.read()
		textPad.insert('1.0', contents)
		file.close()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)  # adds menu item
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)


textPad.pack()
root.mainloop()
