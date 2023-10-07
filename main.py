import re
import tkinter as tk
from tkinter import filedialog

def censurarDominio():
    #Proceso de eliminacion del dominio
    url_delete = dominio_eliminar.get()
    patron1 = 'www\.'+url_delete+'\.[a-z]{2,3}'
    patron2 = 'https:\/\/www\.'+url_delete+'\.[a-z]{2,3}'
    patron3 = 'https:\/\/'+url_delete+'\.[a-z]{2,3}'
    patron4 = 'http:\/\/www\.'+url_delete+'\.[a-z]{2,3}'
    patron5 = 'http:\/\/'+url_delete+'\.[a-z]{2,3}'
    patron6 = url_delete+'\.[a-z]{2,3}'
    patron_completo = patron1+'|'+patron2+'|'+patron3+'|'+patron4+'|'+patron5+'|'+patron6

    lineas = archivo.read()
    if archivo:
        lineas=re.sub(patron_completo, '-', lineas, flags=re.IGNORECASE)
        ventana_texto = lineas 
        texto_resul.config(text=lineas)
        boton_exportar.config(state="active")   #Activa el boton de exportar archivo


def exportar():
    #Si desea exportar el archivo de texto, se debe seleccionar un nuevo archivo
    nuevo_archivo = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(nuevo_archivo, "w") as file:
        file.write(texto_resul.get())

def seleccionar_archivo():
    #Seleccionar archivo de texto
    global archivo
    archivo = filedialog.askopenfile()
    if archivo:
        mensaje_archivo_selecc.config(text=f"Archivo seleccionado: {archivo.name}")
    else:
        mensaje_archivo_selecc.config(text="Archivo no seleccionado")


menu = tk.Tk()
menu.title("Eliminar Dominio")
menu.geometry("600x300")

mensaje_dominio = tk.Label(menu, text="Ingrese el dominio a eliminar")
mensaje_dominio.pack()

dominio_eliminar = tk.Entry(menu)
dominio_eliminar.pack()
mensaje_archivo = tk.Label(menu, text="Ingrese el archivo a revisar")
mensaje_archivo.pack()

boton_archivo = tk.Button(menu, text="Seleccionar..", command=seleccionar_archivo)
boton_archivo.pack()

mensaje_archivo_selecc = tk.Label(menu, text="")
mensaje_archivo_selecc.pack()

boton_revisar = tk.Button(menu, text="Eliminar Dominio", command=censurarDominio)
boton_revisar.pack()

texto_resul = tk.Label(menu, text="")
texto_resul.pack()

boton_exportar = tk.Button(menu, text="Reescribir archivo", command=exportar, state=tk.DISABLED)
boton_exportar.pack()

mensaje_exportar = tk.Label(menu, text="")
mensaje_exportar.pack()

menu.mainloop()