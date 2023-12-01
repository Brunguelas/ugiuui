nombre = str(input("ingrese su nombre: "))
calificacion1 = int(input("ingrese su calificación de matemática: "))
calificacion2 = int(input("ingrese su calificación de física: "))
calificacion3 = int(input("ingrese su calificación de química: "))
calificacion4 = int(input("ingrese su calificación de lengua: "))
suma = calificacion1 + calificacion2 + calificacion3 + calificacion4
promedio = suma / 4 
if promedio >= 6:
    print ("felicitaciones ",nombre, "aprobaste con un promedio de ", promedio)
else:
    print (nombre,"debes seguir esforzandote tu promedio fue de ", promedio) 


