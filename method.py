import tkinter as tk
from tkinter import messagebox

def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def process_text(app):
    message = app.message_entry.get("1.0", tk.END).strip()
    try:
        shift = int(app.shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if app.operation.get() == "encrypt":
        result = encrypt_caesar(message, shift)
    elif app.operation.get() == "decrypt":
        result = decrypt_caesar(message, shift)
    else:
        messagebox.showerror("Invalid Operation", "Please select an operation (encrypt or decrypt).")
        return

    app.result_text.config(state=tk.NORMAL)
    app.result_text.delete("1.0", tk.END)
    app.result_text.insert(tk.END, result)
    app.result_text.config(state=tk.DISABLED)
