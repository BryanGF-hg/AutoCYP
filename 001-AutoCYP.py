# Programa Semi-Automático de Copiar y Pegar v0.1
# Hecho por Bryan Glot Fong - 1 DAM con ayuda del profesorado

#RECOMENDACIONES:
#OPCIONAL--Cambiar "datos-AutoCYP.txt" a otro "archivo.txt" si quieres cambiar el archivo(solo se encuentra dentro de las funciones leer y escribir)

import tkinter as tk
ventana = tk.Tk()
marco = tk.Frame(ventana)

#función leer
def leer():
 archivo = open("datos-AutoCYP.txt",'r')
 filas = archivo.readlines()
 for fila in filas:
  print(fila)
 archivo.close()

#función escribir
def escribir():
    archivo = open("datos-AutoCYP.txt",'w')
    archivo.write("1.-Introduccion:\n")
#Primero dato introducido (linea de abajo)########################
    archivo.write(introduccion.get()+"\n")
    archivo.write("2.-Desarrollo:\n")
#Segundo dato introducido (linea de abajo)########################
    archivo.write(desarrollo.get()+"\n")
    archivo.write("3.-Aplicacion:\n")
#Tercer dato introducido (linea de abajo)########################
    archivo.write(aplicacion.get()+"\n")
    archivo.write("4.-Conclusion:\n")
#Cuarto dato introducido (linea de abajo)########################
    archivo.write(conclusion.get()+"\n")
    archivo.write("Codigo:\n")
    
    archivo.write("```\n")
    archivo.write(codigo.get()+"\n")
    archivo.write("```")
    archivo.close()
    

#1.-Introducción
tk.Label(marco,text="Introduce el contenido de      1.-Introducción").pack(padx=10,pady=10)
introduccion= tk.Entry(marco)
introduccion.pack(padx=10,pady=10)

#2.-Desarrollo
tk.Label(marco,text="Introduce el contenido de      2.-Desarrollo").pack(padx=10,pady=10)
desarrollo= tk.Entry(marco)
desarrollo.pack(padx=10,pady=10)

#3.-Aplicación
tk.Label(marco,text="Introduce el contenido de      3.-Aplicación").pack(padx=10,pady=10)
aplicacion= tk.Entry(marco)
aplicacion.pack(padx=10,pady=10)

#4.-Conclusión
tk.Label(marco,text="Introduce el contenido de      4-Conclusión").pack(padx=10,pady=10)
conclusion = tk.Entry(marco)
conclusion.pack(padx=10,pady=10)

#Código
tk.Label(marco,text="Introduce el contenido de      Código").pack(padx=10,pady=10)
codigo = tk.Entry(marco)
codigo.pack(padx=10,pady=10)


#BOTON (llamada a la funcion escribir)
tk.Button(marco,text="Pulsa para escribir",command = escribir).pack(padx=10,pady=10)
#BOTON (llamada a la funcion leer)
tk.Button(marco,text="Pulsa para leer",command = leer).pack(padx=10,pady=10)

marco.pack(padx=10,pady=10)
ventana.mainloop()
