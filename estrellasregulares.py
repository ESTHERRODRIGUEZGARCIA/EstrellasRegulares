#ejercicio Estrellas regulares

import turtle

def estrella(esquinas, lado = 150):

    def mcd(x,y):
        while y != 0:
            x, y = y, x % y
            return x

    if esquinas <= 4:
        print("Introduce un número de esquinas mayor.")
        return

    for i in range (esquinas // 2, 1, -1):
        if mcd (esquinas, i) == 1:
            angulo = 360 / esquinas * i 
            break

