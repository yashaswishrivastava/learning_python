from tkinter import *
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Simple check
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
window = tk.Tk()
window.title("Login Window")
window.geometry("300x200")

# Username Label and Entry
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(window)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(window, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(window, show="*")  # Hide password input
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
window.mainloop()











from tkinter import *
root = Tk()
Entry(root).pack()
Entry(root, show="*").pack()
Button(root, text="Login").pack()
root.mainloop()
# Login window with username and password fields
