# -*- coding: utf-8 -*-
'''La linea de arriba sirve para que no nos marque error con
   los acentos y los caracteres especiales'''

print ("Hola, ¿cómo te llamas?")
nombre = input()
print ("Buen día {}".format(nombre))


while True:
    valor_1 = 0
    valor_2 = 0
    print ("---Calculadora---")
    print ("1- Sumar")
    print ("2- Restar")
    print ("3- Multiplicar")
    print ("4- Dividir")
    print ("5- Salir")
    op = int(input('Opcion: '))
    if op == 1:
        print ("---Sumar---")
        valor_1 = int(input('primer valor: '))
        print (" + ")
        valor_2 = int(input('segundo valor: '))
        suma = valor_1 + valor_2
        print ("El resultado es: {} \n".format(suma))
    elif op == 2:
        print ("---Restar---")
        valor_1 = int(input('primer valor: '))
        print (" - ")
        valor_2 = int(input('segundo valor:'))
        resta = valor_1 - valor_2
        print ("El resultado es: {} \n".format(resta))
    elif op == 3:
        print ("---Multiplicar---")
        valor_1 = int(input('primer valor: '))
        print (" x ")
        valor_2 = int(input('segundo valor:'))
        multiplicacion = valor_1 * valor_2
        print ("El resultado es: {} \n".format(multiplicacion))
    elif op == 4:
        print ("---Dividir---")
        valor_1 = int(input('primer valor: '))
        print (" / ")
        valor_2 = int(input('segundo valor:'))
        dividir = valor_1 / valor_2
        print ("El resultado es: {} \n".format(dividir))
    elif op == 5:
        break
