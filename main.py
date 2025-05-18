#Librerias:
import turtle as t
import time
import random

#Creacion de pantalla:
pantalla = t.Screen()
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

#Laberinto 4 - Estilo en espiral:
Laberinto_4 = [
    "#################################",
    "#S      #         #           G#",
    "# ####### ####### ####### ##### #",
    "# #     #       #       #     # #",
    "# # ### ####### ####### ##### # #",
    "# # #   #     #       #     # # #",
    "# # # ### ### ##### ##### ### # #",
    "# # # #   # #   #   #   #   # # #",
    "# # ### # # ### # # # # # # # # #",
    "# #   # # #     # # # # # #   # #",
    "# ### ### ######### # # ####### #",
    "#     #             #           #",
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
 

def main():
    t.tracer(0)
    Laberintos = [Laberinto_1, Laberinto_2, Laberinto_3, Laberinto_4, Laberinto_5]
    The_Maze = random.choice(Laberintos)
    dibujar_laberinto(The_Maze)
    t.update()
    t.mainloop()

if __name__ == "__main__":
    main()


