import tkinter as tk
from tkinter import filedialog

# Callback functions
def nuevo_archivo():
    text.delete("1.0", tk.END)

def guardar_archivo():
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de textos", "*.txt"), ("Archivos de python", "*.py"), ("Todos", "*.*")])
    if nombre_archivo:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(text.get("1.0", tk.END))

def guardar_como():
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de textos", "*.txt"), ("Archivos de python", "*.py"), ("Todos", "*.*")])
    if nombre_archivo:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(text.get("1.0", tk.END))

def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivos de textos", "*.txt"), ("Archivos de python", "*.py"), ("Todos", "*.*")])
    if nombre_archivo:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, contenido)

def copiar():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def pegar():
    text.insert(tk.INSERT, text.clipboard_get())

def cortar():
    copiar()
    text.delete("sel.first", "sel.last")

ventana = tk.Tk()
ventana.title("blog notes")
ventana.geometry("800x600")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo)

edicion = tk.Menu(menu)
menu.add_cascade(label="Edición", menu=edicion)

text = tk.Text(ventana)
text.pack(fill=tk.BOTH, expand=True)

archivo.add_command(label="New", command=nuevo_archivo)
archivo.add_command(label="Open File", command=abrir_archivo)
archivo.add_command(label="Save", command=guardar_archivo)
archivo.add_command(label="Save As", command=guardar_como)

edicion.add_command(label="Copy", command=copiar)
edicion.add_command(label="Paste", command=pegar)
edicion.add_command(label="Cut", command=cortar)

ventana.mainloop()