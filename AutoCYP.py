# Programa Semi-Automático de Copiar y Pegar v0.2
# Hecho por Bryan Glot Fong - 1 DAM con ayuda del profesorado

# v0.2: Mejoras gramáticales hechas,    Función ComillasCerradas creada para usarla,   Función borrar_espacios creada para usarla

#RECOMENDACIONES:
#OPCIONAL--Cambiar "datos-AutoCYP.txt" a otro "archivo.txt" si quieres cambiar el archivo(solo se encuentra dentro de las funciones leer y escribir)
#Crear un boton eliminar


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
    archivo.write("1.-Introducción:\n")
#Primero dato introducido (linea de abajo)########################
    archivo.write(introduccion.get()+"\n")
    archivo.write("2.-Desarrollo:\n")
#Segundo dato introducido (linea de abajo)########################
    archivo.write(desarrollo.get()+"\n")
    archivo.write("3.-Aplicación:\n")
#Tercer dato introducido (linea de abajo)########################
    archivo.write(aplicacion.get()+"\n")
    archivo.write("4.-Conclusión:\n")
#Cuarto dato introducido (linea de abajo)########################
    archivo.write(conclusion.get()+"\n")
    archivo.write("Código:\n")
    
    archivo.write("```\n")
    archivo.write(codigo.get()+"\n")
    archivo.write("```")
    archivo.close()
    
#función Comillas Cerradas
def comillascerradas():
 archivo = open("datos-AutoCYP.txt",'w')
 archivo.write("```\n"+""+"```\n")
 archivo.close()



#función borrar_espacios
def borrar_espacios():
 archivo = open("datos-AutoCYP.txt",'a')
 archivo.truncate(5000)
 archivo.close()
 #Permite leer inmediamente después de usar la función borrar_espacios
 archivo = open("datos-AutoCYP.txt","r")
 print("\n"+archivo.read())

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
#BOTON (llamada a la funcion comillascerradas)
tk.Button(marco,text="Pulsa para crear ComillasCerradas",command = comillascerradas).pack(padx=10,pady=10)
#BOTON (llamada a la funcion borrar_espacios)
tk.Button(marco,text="Pulsa para borrar espacio",command = borrar_espacios).pack(padx=10,pady=10)
#BOTON (llamada a la funcion leer)
tk.Button(marco,text="---------Pulsa para leer---------",command = leer).pack(padx=10,pady=10)




marco.pack(padx=15,pady=15)
ventana.mainloop()