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
t.speed(10)

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
    "#   #                 #     #   #",
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

def orientacion_turtle(direccion):

    if direccion == (1,0):
        t.setheading(0)
    elif direccion == (0, 1):
        t.setheading(270)
    elif direccion == (-1, 0):
        t.setheading(180)
    elif direccion == (0, -1):
        t.setheading(90)


def buscar_meta(laberinto, x, y, visitados, ruta_actual):
    if laberinto[y][x] == 'G':
        ruta_actual.append((x, y))
        t.dot(10, "blue")
        return True

    if (x, y) in visitados or laberinto[y][x] == '#':
        return False

    visitados.add((x, y))
    ruta_actual.append((x, y))

    # Mover la tortuga a la celda actual
    screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda + Tamaño_celda // 2
    screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda - Tamaño_celda // 2
    t.goto(screen_x, screen_y)
    time.sleep(0.02)

    # Direcciones: derecha, abajo, izquierda, arriba
    direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in direcciones:
        nuevo_x, nuevo_y = x + dx, y + dy

        if 0 <= nuevo_y < len(laberinto) and 0 <= nuevo_x < len(laberinto[0]):
            if laberinto[nuevo_y][nuevo_x] != '#' and (nuevo_x, nuevo_y) not in visitados:
                orientacion_turtle((dx, dy))

                if buscar_meta(laberinto, nuevo_x, nuevo_y, visitados, ruta_actual):
                    t.dot(10, "blue")
                    return True

    # Punto sin salida (gris)
    t.dot(8, "gray")

    # Retroceso físico
    ruta_actual.pop()
    if len(ruta_actual) > 0:
        paso_anterior = ruta_actual[-1]
        dx = paso_anterior[0] - x
        dy = paso_anterior[1] - y
        orientacion_turtle((dx, dy))

        screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + paso_anterior[0] * Tamaño_celda + Tamaño_celda // 2
        screen_y = len(laberinto) * Tamaño_celda // 2 - paso_anterior[1] * Tamaño_celda - Tamaño_celda // 2
        t.goto(screen_x, screen_y)
        time.sleep(0.02)

    return False


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

    x_inicio, y_inicio = encontrar_inicio(laberinto)

    ruta_actual = []
    visitados = set()
    buscar_meta(laberinto, x_inicio, y_inicio, visitados, ruta_actual)

    print("Ruta encontrada: ")
    for paso in ruta_actual:
        print(paso)

    t.update()
    t.mainloop()

if __name__ == "__main__":
    main()


