import tkinter
from tkinter import ttk

window = tkinter.Tk()

marcas =['Ford', 'Mazda', 'Toyota', 'Chevrolet', 'BMW', 'Audi']
listaItems = tkinter.StringVar(value=marcas)
listbox = tkinter.Listbox(window, height=10, listvariable=listaItems)
label = ttk.Label(window, text="Listado de marcas")

label.grid(column=0, row=0, sticky=tkinter.W)
listbox.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()