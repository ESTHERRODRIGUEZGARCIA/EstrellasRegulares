#ejercicio Estrellas regulares

import turtle

n = int(input("Introduzca el número de puntas de la estrella: "))

def estrella(n):
            
    def angulo():
        angulos = 0
        if n % 4 == 0:
            angulos = 180 - (360/n) 
        elif n % 3 == 0:
            angulos = 120 + (360/n)
        else:
            pass
        return angulos
        
turtle.speed(0)
for _ in range(n):
    turtle.right(angulo())
    turtle.fordward(200)
turtle.done()

estrella(n)
