import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (12 * math.cos(k) - 5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - math.cos(4 * k))

speed(0)
bgcolor("black")
color("red")
pensize(5)  # Aumenta el grosor del borde del corazón
penup()

# Moverse al punto inicial sin dibujar
goto(hearta(0) * 20, heartb(0) * 20)
pendown()

# Dibujar el contorno del corazón con un trazo grueso
for i in range(1000):  
    k = i * 2 * math.pi / 1000  
    goto(hearta(k) * 20, heartb(k) * 20)

# Escribir el mensaje dentro del corazón
penup()
goto(0, -50)  # Ajusta la posición del texto
color("white")
write("Te amo Catalina", align="center", font=("Brush Script MT", 45, "bold"))

hideturtle()
done()
