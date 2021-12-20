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


