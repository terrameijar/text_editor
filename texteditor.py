#TextEditor

import Tkinter
import ScrolledText #because Tkinter textarea does not provide scrolling
root = Tkinter.Tk(classname="Text Editor")
textPad = ScrolledText.ScrolledText(root, width = 100, height = 80)
textPad.pack()
root.mainloop()
