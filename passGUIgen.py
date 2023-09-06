import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    global generated_password  # Declare generated_password as global
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)
    generated_password = password


def copy_to_clipboard():
    global generated_password
    if generated_password:
        pyperclip.copy(generated_password)
        copied_label.config(text="Copied to clipboard!")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")


# Create and place widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=3)

length_entry = tk.Entry(root)
length_entry.pack(pady=3)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=7)



password_label = tk.Label(root, text="")
password_label.pack(pady=7)



button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
button.pack()

copied_label = tk.Label(root)
copied_label.pack()

generated_password = "" 
# Start the Tkinter event loop
root.mainloop()
