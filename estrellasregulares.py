#ejercicio Estrellas regulares

from turtle import *

n = int(input("Introduzca el número de puntas de la estrella: "))

def estrella(n):
            
    def angulo():
        angulo = 0
        if n % 4 == 0:
            angulo = 180 - (360/n) 
        elif n % 3 == 0:
            angulo = 120 + (360/n)
        else:
            pass
        return angulo
        
turtle.speed(0)
for _ in range(n):
    turtle.right(angulo())
    turtle.fordward(200)
turtle.done()


