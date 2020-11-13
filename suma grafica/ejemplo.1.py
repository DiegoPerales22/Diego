mport tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def sumar():
    numeroA=NA.get()
    numeroB=NB.get()
    resultado=numeroA+numeroB
    Res.set(resultado)
    limpiarCampos()

def resta():
    numeroA=NA.get()
    numeroB=NB.get()
    resultado = numeroA - numeroB
    Res.set(resultado)
    limpiarCampos()

def multiplicar():
    numeroA = NA.get()
    numeroB = NB.get()
    resultado = numeroA * numeroB
    Res.set(resultado)
    limpiarCampos()

def dividir():
    numeroA = NA.get()
    numeroB = NB.get()
    resultado = numeroA / numeroB
    Res.set(resultado)
    limpiarCampos()
#Creacion de ventana
#Utilizamos el "tk" porque en la parte superior de la importacion
#en vez de utilizar la palabra "tkinter" utilizaremos "tk" por
ventana= tk.Tk()
#Configurar el tamaño de la ventana
ventana.config(width=300, height=200)
etiquetaNA=Label(ventana,text="Numero A: ")
etiquetaNA.place(x=70,y=0)
numA=IntVar()
#Creación de una entrada "caja de texto" con la palabra "ttk" que proviene
#de la libreria tkinter
entradaNa=Entry(ventina, textvariable=numA)
#Posteriormente le damos una posición a esta entrada o caja de texto
entradaNA.place(x=70,y=0)

botontransportar=Button(ventana, text="Sumar", command=sumar)
botontransportar.place(x=0,y=90)
botontransportar=Button(ventana, text="Resta", command=restar)
botontransportar.place(x=0,y=120)
botontransportar=Button(ventana, text="Multiplicar", command=multiplicar)
botontransportar.place(x=0,y=150)
botontransportar=Button(ventana, text="Dividir", command=dividir)
botontransportar.place(x=0,y=180)


ventana.mainloop()