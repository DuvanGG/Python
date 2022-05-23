
import tkinter
from tkinter import ttk

# obtiene el texto seleccionado y lo pasa al label
# get() -> obtiene el valor que tenga
def readLabelText():
    print(seleccionado.get())
    label.config(text="{}".format("has seleccionado: " + seleccionado.get()))

# set() -> asigna valor a variable de control
def clean():
    seleccionado.set("Estoy vacio")
    label.config(text="")
    print(seleccionado.get())
    

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Ubuntu', value='Ubuntu', variable=seleccionado, command=readLabelText)
r2 = ttk.Radiobutton(window, text='Fedora', value='Fedora', variable=seleccionado, command=readLabelText)
r3 = ttk.Radiobutton(window, text='Debian', value='Debian', variable=seleccionado, command=readLabelText)
boton = ttk.Button(window, text='Limpiar', command=clean)
label = ttk.Label(window)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)
boton.grid(column=0, row=4, pady=5, padx=5)
label.grid(column=0, row=5, pady=5, padx=5)

# pack() -> mostrar
window.mainloop()