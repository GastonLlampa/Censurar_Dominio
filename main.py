import re
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from tkinter import filedialog, PhotoImage, messagebox as mb
from io import open
import pathlib

def seleccionar_archivo():
    #Proceso de seleccionar el archivo de Texto
    archivo = filedialog.askopenfile(title="Abrir Archivo", filetypes=(("Archivos de Textos", "*.txt"),("Todos los Archivos", "*.*")))
    path = pathlib.Path(archivo.name)
    extension = (''.join(path.suffixes))
    if (extension == '.txt'):
        if archivo:
            lineasInit.set(value=archivo.read()) 
            mensaje_archivo_selecc.configure(text="Archivo seleccionado")
            boton_revisar.configure(state="normal")
            archivo.close()
        else:
            mb.showwarning(message="!!Archivo no selecionado!!", title="Advertencia")
    else:
        boton_revisar.configure(state="disabled")
        mensaje_archivo_selecc.configure(text="")
        mb.showerror(message="Seleccionar solo Archivos .txt", title="Error")

def censurarDominio():
    #Proceso de eliminacion del dominio
    dominio_delete = dominio_eliminar.get()
    patronDominio = '^[a-zA-Z]+$'
    patronUrl1 = 'www\.'+dominio_delete+'\.[a-z]{2,3}'
    patronUrl2 = 'https:\/\/www\.'+dominio_delete+'\.[a-z]{2,3}'
    patronUrl3 = 'https:\/\/'+dominio_delete+'\.[a-z]{2,3}'
    patronUrl4 = 'http:\/\/www\.'+dominio_delete+'\.[a-z]{2,3}'
    patronUrl5 = 'http:\/\/'+dominio_delete+'\.[a-z]{2,3}'
    patronUrl6 = dominio_delete+'\.[a-z]{2,3}'
    patronCompleto = patronUrl1+'|'+patronUrl2+'|'+patronUrl3+'|'+patronUrl4+'|'+patronUrl5+'|'+patronUrl6
    
    if (re.search(patronDominio, dominio_delete)):
        if (lineasInit.get() != ''):
            cantidad = len(re.findall(patronCompleto, lineasInit.get(), flags=re.IGNORECASE))
            lineasInit.set(re.sub(patronCompleto, '-', lineasInit.get(), re.IGNORECASE))
            #Es para ver como se modifica el texto, y por eso solo se ve desde la terminal
            print(lineasInit.get())
            if (cantidad != 0):
                texto_resul.configure(text="Dominio eliminado con exito")
                texto_Concidencias.configure(text="Coincidencias encontradas:" + str(cantidad))
                boton_exportar.configure(state="normal") #Activa el boton de Guardar Archivo
            else:
                texto_resul.configure(text="No se han encontrado coincidencias")
                texto_Concidencias.configure(text="")
        else:
            mb.showwarning(message="Archivo de texto vacio", title="Advertencia")
    else:
        texto_resul.configure(text="")
        texto_Concidencias.configure(text="")
        mb.showwarning(message="Dominio ingresado incorrecto", title="Advertencia")
        
def guardar():
    #Proceso para guardar el archivo de texto modificado
    nuevo_archivo = filedialog.asksaveasfilename(title="Exportar Archivo", defaultextension=".txt", filetypes=(("Archivos de Textos", "*.txt"),("Todos los Archivos", "*.*")))
    if nuevo_archivo!='':
        file = open(nuevo_archivo, "w")
        file.write(lineasInit.get())
        mb.showinfo("Informacion", "El texto se guardo con exito")
        file.close()
        boton_exportar.configure(state="disabled") #Desactiva el boton de Guardar Archivo

#Las ventana principal de la aplicacion y los Widgets
menu = ctk.CTk()
menu.title("Eliminar Dominio")
menu.geometry("290x340+534+200") #290x340
menu.config(bg='gray10')
menu.iconbitmap('logo_fi_J9A_icon.ico')
lineasInit = tk.StringVar(menu)

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

boton_revisar = ctk.CTkButton(frame, font=('sans rerif', 12), text="Eliminar Dominio", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, state="disabled", command=censurarDominio)
boton_revisar.grid(columnspan=2, row=5, padx=4, pady=4)

texto_resul = ctk.CTkLabel(frame, font=('sans rerif', 12), text="")
texto_resul.grid(columnspan=2, row=6)

texto_Concidencias = ctk.CTkLabel(frame, font=('sans rerif', 12), text="")
texto_Concidencias.grid(columnspan=2, row=7)

boton_exportar = ctk.CTkButton(frame, font=('sans rerif', 12), text="Guardar archivo", border_color='deep sky blue', fg_color='gray10', hover_color='DeepSkyBlue3', border_width=2, command=guardar, state="disabled")
boton_exportar.grid(columnspan=2, row=8, padx=4, pady=4)

menu.mainloop()