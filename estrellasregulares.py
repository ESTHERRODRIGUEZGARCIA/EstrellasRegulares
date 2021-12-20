#ejercicio Estrellas regulares

from turtle import *

def estrella(n):
    def mcm(x,y):
        while y != 0:
            x, y = y, x % y
            return x
        
    def angulo():
        angulo = 0
        if n % 4 == 0:
            