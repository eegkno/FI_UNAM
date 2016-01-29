#Este ejemplo ha sido tomado de 
#http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                
size = 20
for i in range(30):
   tess.stamp()             #Esta determinado que se impriman 30 huellas de la tortuga
   size = size + 3          # Huella de la tortuga
   tess.forward(size)       # Se incrementa el paso de la tortuga cada iteración
   tess.right(24)           # y se gira a la derecha

wn.mainloop()