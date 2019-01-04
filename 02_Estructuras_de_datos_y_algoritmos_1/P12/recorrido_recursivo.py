import turtle
import argparse

#Declaración de la función
#Recordar la importancia de la identación
def recorrido_recursivo(tortuga, espacio, huellas):
    if huellas > 0:
        tortuga.stamp()
        espacio = espacio + 3          
        tortuga.forward(espacio)       
        tortuga.right(24)  
        recorrido_recursivo(tortuga, espacio, huellas-1)
		
		
		
ap = argparse.ArgumentParser()

#El dato de entrada se ingresa con la bandera *--huellas*
ap.add_argument("--huellas", required=True, help="número de huellas")

#Lo que se obtiene es un diccionario (llave:valor) , en este caso llamado *args
args = vars(ap.parse_args())

# Los valores del diccionario son cadenas por lo que se tiene que transformar a un entero
huellas = int(args["huellas"])

if huellas < 10 or  huellas > 30:
	print('Dato incorrecto, se usará por defecto 15')
	huellas = 15

#Creando la ventana	
ventana = turtle.Screen()
ventana.bgcolor("lightgreen")

#Métodos de la tortuga, se pueden consultar en:
##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("blue")
tortuga.penup()


espacio = 20		#Espacio entre las huellas
recorrido_recursivo(tortuga, espacio, huellas)


#Cerrando la ventada dando un click sobre ella
ventana.exitonclick()		