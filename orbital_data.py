import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo(title="Заголовок", message="Это сообщение!")

app = ctk.CTk()
app.geometry("300x200")

button = ctk.CTkButton(app, text="Показать сообщение", command=show_message)
button.pack(pady=20)

app.mainloop()