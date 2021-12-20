#ejercicio Estrellas regulares

import turtle

def estrella(puntas, lado = 150):

    def mcd(x,y):
        while y != 0:
            x, y = y, x % y
            return x
