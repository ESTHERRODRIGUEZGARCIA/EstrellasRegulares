# EstrellasRegulares
Voy a realizar la Tarea Las Estrellas Regulares.

Mi dirección de GitHub para este repositorio es la siguiente: https://github.com/ESTHERRODRIGUEZGARCIA/EstrellasRegulares.git

El diagrama de flujo del código se muestra a continuación:

![image](https://user-images.githubusercontent.com/91721860/146840978-e7bfad41-e14f-4ecb-a0a0-3ac5bb39e5dc.png)

El código que he utilizado para realizar este ejercicio es el siguiente:

````
#ejercicio Estrellas regulares

import turtle

def calculo_estrella(esquinas, lado = 150):

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

    for _ in range (esquinas):
        turtle.fordwar(lado)
        turtle.left(angulo)
        return

calculo_estrella(20)
````
