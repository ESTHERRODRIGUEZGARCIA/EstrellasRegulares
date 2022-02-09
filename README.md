# EstrellasRegulares
Voy a realizar la Tarea Las Estrellas Regulares.

Mi dirección de GitHub para este repositorio es la siguiente: https://github.com/ESTHERRODRIGUEZGARCIA/EstrellasRegulares.git

El reto consiste en programar una función que dibuje estrellas como la que aparece a continuación con un número de puntas dado.

![image](https://user-images.githubusercontent.com/91721860/146841372-15e2545e-c732-4c3f-bf99-b0f9a827395b.png)


Para ello hay que utilizar el módulo de Python Turtle que permite realizar trazos sencillos en una ventana gráfica.



Y también dispones un resumen aquí

https://docs.python.org/es/3.9/library/turtle.html

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
