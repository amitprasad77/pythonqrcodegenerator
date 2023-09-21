import tkinter as tk
import qrcode as qr
from PIL import Image, ImageTk

# Dictionary to store user credentials
user_credentials = {
    "Darshan": "1RF22IS020",
    "Amit": "1RF22IS005",
}

def authenticate():
    username = entry_username.get()
    password = entry_password.get()
    if username in user_credentials and user_credentials[username] == password:
        generate_qr_code()
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        error_label.config(text="Invalid username or password")
        qr_label.config(image=None)

def generate_qr_code():
    data = entry.get()
    qr_code = qr.make(data)
    qr_code.save("code.png")
    image = Image.open("code.png")
    photo = ImageTk.PhotoImage(image)
    qr_label.config(image=photo)
    qr_label.image = photo
    error_label.config(text="")

def register_user():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()
    if new_username and new_password:
        user_credentials[new_username] = new_password
        entry_new_username.delete(0, tk.END)
        entry_new_password.delete(0, tk.END)
        success_label.config(text="Registration successful!")
    else:
        success_label.config(text="Please enter both username and password")

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create and pack a label for instructions
instruction_label = tk.Label(window, text="Enter text to generate QR code:")
instruction_label.pack()

# Create and pack an entry field for user input
entry = tk.Entry(window)
entry.pack()

# Create and pack a label for username
username_label = tk.Label(window, text="Username:")
username_label.pack()

# Create and pack an entry field for username
entry_username = tk.Entry(window)
entry_username.pack()

# Create and pack a label for password
password_label = tk.Label(window, text="Password:")
password_label.pack()

# Create and pack an entry field for password
entry_password = tk.Entry(window, show="*")  # Show asterisks for password input
entry_password.pack()

# Create and pack a button to authenticate
authenticate_button = tk.Button(window, text="Authenticate", command=authenticate)
authenticate_button.pack()

# Create and pack a label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

# Create and pack a label for error messages
error_label = tk.Label(window, fg="red")
error_label.pack()

# Create and pack labels and entry fields for registration
registration_label = tk.Label(window, text="New User Registration:")
registration_label.pack()

new_username_label = tk.Label(window, text="New Username:")
new_username_label.pack()

entry_new_username = tk.Entry(window)
entry_new_username.pack()

new_password_label = tk.Label(window, text="New Password:")
new_password_label.pack()

entry_new_password = tk.Entry(window, show="*")
entry_new_password.pack()

# Create and pack a button to register a new user
register_button = tk.Button(window, text="Register", command=register_user)
register_button.pack()

# Create and pack a label for registration success
success_label = tk.Label(window, fg="green")
success_label.pack()

# Start the Tkinter main loop
window.mainloop()

@Darshan1447

