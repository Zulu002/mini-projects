import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style


# Создаём главное окно
root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")
style = Style(theme='journal')
style = ttk.Style()


# Настройте шрифт табуляции жирным шрифтом
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))


# Создайте блокнот для хранения заметок
notebook = ttk.Notebook(root, style="TNotebook")


# Загрузить сохраненные заметки
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass


# Создайте блокнот для хранения заметок
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


# Создайте функцию для добавления новой заметки
def add_note():
    # Создаем новую вкладку для заметки
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")
    
    
    # Создайте виджеты ввода для заголовка и содержания заметки
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    
    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)
    
    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    
    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Создаем функцию для сохранения заметки
    def save_note():
        # Получаем заголовок и содержание заметки
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)
        
        # Добавляем заметку в словарь заметок
        notes[title] = content.strip()
        
        # Сохраняем словарь заметок в файл
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        
        # Добавляем заметку в блокнот
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)
        
    # Добавляем кнопку сохранения в рамку заметки
    save_button = ttk.Button(note_frame, text="Save", 
                             command=save_note, style="secondary.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            # Добавляем заметку в блокнот
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        # Если файл не существует, ничего не делать
        pass

# Вызовите функцию load_notes при запуске приложения
load_notes()

# Создаем функцию для удаления заметки
def delete_note():
    
    # Получить индекс текущей вкладки
    current_tab = notebook.index(notebook.select())
    
    
    # Получить заголовок удаляемой заметки
    note_title = notebook.tab(current_tab, "text")
    
    
    # Показать диалог подтверждения
    confirm = messagebox.askyesno("Delete Note", 
                                  f"Are you sure you want to delete {note_title}?")
    
    if confirm:
        
        # Удалить заметку из блокнота
        notebook.forget(current_tab)
        
        # Удалить заметку из словаря заметок
        notes.pop(note_title)
        
        
        # Сохраняем словарь заметок в файл
        with open("notes.json", "w") as f:
            json.dump(notes, f)


# Добавляем кнопки в главное окно
new_button = ttk.Button(root, text="New Note", 
                        command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", 
                           command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()