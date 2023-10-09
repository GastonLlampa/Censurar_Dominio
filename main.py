import re
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from tkinter import filedialog, PhotoImage, messagebox as mb
from io import open

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

    global lineas
    lineas = archivo.read()
    if archivo:
        cantidad = len(re.findall(patron_completo, lineas, flags=re.IGNORECASE))
        lineas=re.sub(patron_completo, '-', lineas, flags=re.IGNORECASE)
        if (cantidad != 0 ):
            texto_resul.configure(text="Dominio eliminado con exito")
            texto_Concidencias.configure(text="Coincidencias encontradas:" + str(cantidad))
            boton_exportar.configure(state="normal")   #Activa el boton de guardar archivo
        else:
            texto_resul.configure(text="No se han encontrado coincidencias")
            boton_exportar.configure(state="disabled")   #Desacctiva el boton de guardar archivo
            texto_Concidencias.configure(text="")

def guardar():
    #Si desea exportar el archivo de texto, se debe seleccionar un nuevo archivo
    nuevo_archivo = filedialog.asksaveasfilename(title="Exportar Archivo", defaultextension=".txt", filetypes=(("Archivos de Texto", "*.txt"),("Todos los Archivos","*.*")))
    if nuevo_archivo!='':
        file = open(nuevo_archivo, "w")
        file.write(lineas)
        file.close()
        mb.showinfo("Informacion", "El texto se guardo con exito")

def seleccionar_archivo():
    #Seleccionar archivo de texto
    global archivo
    archivo = filedialog.askopenfile(title="Abrir Archivo", filetypes=(("Archivos de Texto", "*.txt"),("Todos los Archivos","*.*")))
    if archivo:
        mensaje_archivo_selecc.configure(text=f"Archivo seleccionado")
    else:
        mensaje_archivo_selecc.configure(text="!!Archivo no seleccionado!!")

#Las ventana principal de la aplicacion y los Widgets
menu = ctk.CTk()
menu.title("Eliminar Dominio")
menu.geometry("290x340")
menu.config(bg='gray10')
menu.iconbitmap('logo_fi_J9A_icon.ico')

frame = ctk.CTkFrame(menu, fg_color='gray10')
frame.grid(column = 0, row = 0, sticky = 'nsew', padx=10, pady=15)
frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1)

menu.columnconfigure(0, weight=1)
menu.rowconfigure(0, weight=1)

mensaje_archivo = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Ingrese el archivo a revisar")
mensaje_archivo.grid(columnspan=2, row=0)

boton_archivo = ctk.CTkButton(frame, font=('sans rerif', 12), text="Seleccionar Archivo", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, command=seleccionar_archivo)
boton_archivo.place_configure(relx=0.5, rely=0.5, anchor=ctk.CENTER)
boton_archivo.grid(columnspan=2, row=1, padx=4, pady=4)

mensaje_archivo_selecc = ctk.CTkLabel(frame, font=('sans rerif', 12), text="")
mensaje_archivo_selecc.grid(columnspan=2, row=2)

mensaje_dominio = ctk.CTkLabel(frame, font=('sans rerif', 12), text="Ingrese el dominio a eliminar", fg_color='gray10')
mensaje_dominio.grid(columnspan=2, row=3)

dominio_eliminar = ctk.CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Dominio', border_color='deep sky blue', fg_color='gray10', width=220, height=40)
dominio_eliminar.grid(columnspan=2, row=4, padx=4, pady=4)

boton_revisar = ctk.CTkButton(frame, font=('sans rerif', 12), text="Eliminar Dominio", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, command=censurarDominio)
boton_revisar.grid(columnspan=2, row=5, padx=4, pady=4)

texto_resul = ctk.CTkLabel(frame, font=('sans rerif', 12), text="")
texto_resul.grid(columnspan=2, row=6)

texto_Concidencias = ctk.CTkLabel(frame, font=('sans rerif', 12), text="")
texto_Concidencias.grid(columnspan=2, row=7)

boton_exportar = ctk.CTkButton(frame, font=('sans rerif', 12), text="Guardar archivo", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, command=guardar, state="disabled")
boton_exportar.grid(columnspan=2, row=8, padx=4, pady=4)

menu.mainloop()