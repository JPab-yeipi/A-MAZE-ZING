#Librerias:
import turtle as t
import time
import random

#Creacion de pantalla:
pantalla = t.Screen()
pantalla.setup(width=1050, height=700)
pantalla.bgcolor("#34b800")

#Configuracion basica:
t.title("Laberinto con backtracking - Jose Pablo Garcia Zamudio")
t.shape("turtle")
t.speed(5)

#Variables:
Tamaño_celda = 24

#Laberintos:
#Laberinto 1 - Curvas locas y un solo camino correcto:
Laberinto_1 = [
    "#################################",
    "#S      #       #     #     #   #",
    "# ##### # ##### # ### # ### # # #",
    "#     # #     #   #   #   #   # #",
    "##### # ##### ##### ##### ##### #",
    "#   # #   #     #   #     #     #",
    "# # ##### # ##### ### ### # #####",
    "# #     #   #   #   #   # #     #",
    "# ##### ##### ### ### # ##### # #",
    "#     #     #   #     #     # # #",
    "##### ### # ### # ######### # # #",
    "#     #   #     #         #   # #",
    "# ##### ######### ####### ##### #",
    "#     #   #     # #     #     # #",
    "# ### ### # ### # ### # ### # # #",
    "#   #     #   #     # #   # #   #",
    "# ####### ### ##### ### ### ### #",
    "#             #         #     G #",
    "#################################"
]

#Laberinto 2 - Rutas falsas y cruces multiples:
Laberinto_2 = [
    "#################################",
    "#S    #     #     #   #     #   #",
    "### ### ### ### ### ### ### ### #",
    "#   #   #   #     #   #   #   # #",
    "# ### ##### ### ### ### ### # # #",
    "#     #     # #     #     # #   #",
    "##### # ### # ####### ### # #####",
    "#   # #   #   #   #     # #     #",
    "# # # ### ##### # ##### # ### # #",
    "# #   #   #   # #     # #   # # #",
    "##### # ### ### ### ### ### # # #",
    "#     #   #   #   #     #   # # #",
    "# ### ### ### ##### ##### ### # #",
    "#   #     #     #     #     #   #",
    "### # ### ### ### ### ### #######",
    "#   # #     #   #   #   #       #",
    "# ### ##### ### ### # ### ##### #",
    "#         #     #   #     #   G #",
    "#################################"
]

#Laberinto 3 - Muchos recovecos:
Laberinto_3 = [
    "#################################",
    "#S  #   #       #   #     #     #",
    "### # ### ##### # ### ### ##### #",
    "#   #     #   # #     #   #   # #",
    "# ####### # # # ##### # ### # # #",
    "#         # # #     # #   # #   #",
    "########### ##### # ### # #######",
    "#       #     #   #   # #       #",
    "# ##### ##### ### ### ### ##### #",
    "#   #       #     #     # #   # #",
    "### # ##### # ### ##### # # # # #",
    "#   #     #   #     #   # # # # #",
    "# ##### # ### ##### ### ### # # #",
    "#     # #   #     #     #   #   #",
    "# ### ##### ### ##### ### ##### #",
    "#   #       #   #   #     #     #",
    "##### ##### ### # ##### ### ### #",
    "#     #   #     #         #   G #",
    "#################################"
]

#Laberinto 4 - Pasillos angostos y vueltas falsas:
Laberinto_4 = [
    "#################################",
    "#S    #       #       #       # #",
    "# ### # ##### # ##### # ##### # #",
    "# #   #     # #     # #     # # #",
    "# # ####### ####### ##### ### # #",
    "# #         #   #       #   #   #",
    "# ######### # # ####### # ### ###",
    "#       #   # #       # #     # #",
    "####### # ### ##### # ######### #",
    "#     # #   #     # #     #     #",
    "# ### # ### ##### ### ### ### # #",
    "#   #     # #   #     # #   # # #",
    "### ##### # # # ####### # # # # #",
    "#   #     # # #       # # #   # #",
    "# # # ##### # ##### ### ####### #",
    "# # #       #     #   #         #",
    "# # ########### # ### ######### #",
    "# #             #             G #",
    "#################################"
]

#Laberinto 5 - Denso pero con varios caminos validos:
Laberinto_5 = [
    "#################################",
    "#S    #     #     #       #     #",
    "# ### ### ### ### # ##### # ### #",
    "# #   #   #   #   #     #   #   #",
    "# # ##### ### # ####### ##### # #",
    "# #     #     #       #     # # #",
    "# ### # ### ######### ### ### # #",
    "#   # #     #   #     #   #   # #",
    "### # ### ### ### ##### ### ### #",
    "#   #   #   #   #     #   #     #",
    "# ### ### ### ### ### ### ##### #",
    "# #   #     #     #   #     #   #",
    "# # ##### ######### ### ### # # #",
    "# #     #   #     #     #   # # #",
    "# ##### ### # ### ##### # ### # #",
    "#     #     # #         #     # #",
    "##### ### ### ### ########### # #",
    "#           #               G#  #",
    "#################################"
]

#Funciones:
#Funcion para dibujar cuadrados:
def dibujar_cuadrado(x, y, color):

    #Configuracion basica del cuadrado:
    t.color(color)
    t.goto(x, y)

    #dibujo del cuadrado:
    t.begin_fill()
    for i in range(4):
        t.pendown()
        t.forward(Tamaño_celda)
        t.right(90)
    t.end_fill()
    t.penup()

#Funcion para dibujar laberintos:
def dibujar_laberinto(laberinto):
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda
            screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda
            celda = laberinto[y][x]

            if celda == '#':
                dibujar_cuadrado(screen_x, screen_y, "black")

            elif celda == 'G':
                dibujar_cuadrado(screen_x, screen_y, "green")

            elif celda == 'S':
                dibujar_cuadrado(screen_x, screen_y, "blue")

            else:
                dibujar_cuadrado(screen_x, screen_y, "white")
 
def encontrar_inicio(laberinto):
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            if laberinto[y][x] == 'S':

                screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda
                screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda

                t.penup()
                t.goto(screen_x + Tamaño_celda // 2, screen_y - Tamaño_celda // 2)
                t.setheading(0)
                t.pendown()

                return x, y
     
    raise ValueError("No se encontró el punto de inicio en el laberinto.")


def main():
    t.tracer(0)
    Laberintos = [[Laberinto_1, "Laberinto 1 - Curvas locas y un solo camino correcto"],
                  [Laberinto_2, "Laberinto 2 - Rutas falsas y cruces múltiples"],
                  [Laberinto_3, "Laberinto 3 - Muchos recovecos"],
                  [Laberinto_4, "Laberinto 4 - Pasillos angostos y vueltas falsas"],
                  [Laberinto_5, "Laberinto 5 - Caminos válidos múltiples"]
                 ]
    The_Maze = random.choice(Laberintos)
    laberinto = The_Maze[0]
    nombre = The_Maze[1]

    titulo = t.Turtle()
    titulo.hideturtle()
    titulo.penup()
    titulo.color("black")
    titulo.goto(0, 280)
    titulo.write(nombre, align="center", font=("Arial", 40, "bold"))

    dibujar_laberinto(laberinto)

    #x_inicio, y_inicio = encontrar_inicio(laberinto)
    encontrar_inicio(laberinto)

    t.update()
    t.mainloop()

if __name__ == "__main__":
    main()


