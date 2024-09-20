import turtle

# Configuración de la ventana
win = turtle.Screen()
win.bgcolor("lightgreen")  # Fondo verde

# Crear una tortuga para dibujar la flor
flor = turtle.Turtle()
flor.speed(1)  # velocidad de dibujo

# Dibujar la flor amarilla
def dibujar_petal(tortuga, longitud, angulo):
    tortuga.fillcolor("yellow")
    tortuga.begin_fill()
    tortuga.circle(longitud, angulo)
    tortuga.left(180 - angulo)
    tortuga.circle(longitud, angulo)
    tortuga.end_fill()

def dibujar_flor(tortuga, num_petalos, longitud, angulo):
    for _ in range(num_petalos):
        dibujar_petal(tortuga, longitud, angulo)
        tortuga.left(360 / num_petalos)

# Dibujar varias flores
flor.penup()
flor.goto(0, -100)
flor.pendown()
dibujar_flor(flor, 12, 50, 120)

flor.penup()
flor.goto(-100, -50)
flor.pendown()
dibujar_flor(flor, 12, 40, 100)

flor.penup()
flor.goto(100, -50)
flor.pendown()
dibujar_flor(flor, 12, 40, 100)

# Agregar detalles románticos
flor.penup()
flor.goto(-50, 50)
flor.pendown()
flor.color("red")
flor.write("Feliz 21 de septiembre", font=("Arial", 20, "bold"))

flor.penup()
flor.goto(-150, -150)  # Alejar la frase "Te amo" de la flor
flor.pendown()
flor.color("purple")  # Cambiar el color de la palabra "Te amo" a púrpura
flor.write("Te amo", font=("Arial", 15, "italic"))

# Mantener la ventana abierta
win.mainloop()