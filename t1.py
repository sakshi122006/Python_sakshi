import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    message = text_message.get("1.0", tk.END).strip()

    if not name or not email or not phone or not message:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Form Submitted",
                            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

# Main window
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Email:", font=("Arial", 12)).pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

tk.Label(root, text="Phone:", font=("Arial", 12)).pack(pady=5)
entry_phone = tk.Entry(root, width=40)
entry_phone.pack(pady=5)

tk.Label(root, text="Message:", font=("Arial", 12)).pack(pady=5)
text_message = tk.Text(root, width=30, height=5)
text_message.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white").pack(pady=10)

root.mainloop()
