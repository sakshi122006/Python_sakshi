import tkinter as tk
def display_selection():
selection = "Yes" if var.get() == 1 else "No"
label.config(text="Selection: " + selection)
# create the main window
root = tk.Tk()
root.title("CheckButton Demo")
# create a label
label = tk.Label(root, text="Selection: ")
label.pack()
# create a check button
var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Yes", variable=var, command=display_selection)
check_button.pack()
# start the main event loop
root.mainloop()