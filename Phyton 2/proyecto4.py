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
pensize(8)  
penup()

goto(hearta(0) * 20, heartb(0) * 20)
pendown()

for i in range(1000):  
    k = i * 2 * math.pi / 1000  
    goto(hearta(k) * 20, heartb(k) * 20)

penup()
goto(0, -50)  
color("white")
write("Te amo Catalina", align="center", font=("Brush Script MT", 45, "bold"))

hideturtle()
done()
