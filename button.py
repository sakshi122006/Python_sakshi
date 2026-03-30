from tkinter import *
parent=Tk()
redbutton =Button (parent, text="Red", fg="red")
redbutton.pack(side=LEFT)
greenbutton=Button(parent, text="green", fg="green")
greenbutton.pack(side=RIGHT, fill=X)
bluebutton=Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)
blackbutton= Button (parent, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

parent.mainloop()