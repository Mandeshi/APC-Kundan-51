
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Registration Form")
root.geometry("350x350")

Label(root, text="Student Registration Form",
      font=("Arial", 14, "bold")).pack(pady=10)

Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Roll Number").pack()
roll = Entry(root)
roll.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

def submit():
    if name.get() == "" or roll.get() == "" or email.get() == "":
        messagebox.showerror("Error", "Fill all fields")
    elif not name.get().isalpha():
        messagebox.showerror("Error", "Enter a valid name")
    elif not roll.get().isdigit():
        messagebox.showerror("Error", "Enter numbers in roll number")
    elif "@" not in email.get() or "." not in email.get():
        messagebox.showerror("Error", "Enter a valid email")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

Button(root, text="Submit", command=submit).pack(pady=15)

root.mainloop()
