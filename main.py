#Librerias -----------------------------------------------------------------------
import turtle as t
import time
import maps
import tkinter as tk
from tkinter import PhotoImage
import os
from collections import deque
from turtle import RawTurtle, ScrolledCanvas

#Ruta de assets -------------------------------------------------------------------
RUTA_TITULO_AMZ = os.path.join("Assets", "AMAZEZINGTtl.png")
RUTA_BOTONES = os.path.join("Assets", "Botones")

#Variables  -----------------------------------------------------------------------
Tamaño_celda = 15
colores = ["Rojo", "Azul", "Amarillo", "Verde"]
metodos = [
        ("Maze 1", 1, 1, "Verde"),
        ("Maze 2", 2, 1, "Azul"),
        ("Maze 3", 1, 2, "Rojo"),
        ("Maze 4", 2, 2, "Amarillo"),
        ("Maze 5", 1, 3, "Azul"),
        ("Maze 6", 2, 3, "Verde"),
        ("Maze 7", 1, 4, "Amarillo"),
        ("Your Maze", 2, 4, "Rojo")
]

#Funciones ------------------------------------------------------------------------
#Funcion para dibujar cuadrados:
def dibujar_cuadrado(turtle, x, y, color):

    #Configuracion basica del cuadrado:
    turtle.color(color)
    turtle.goto(x, y)

    #dibujo del cuadrado:
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(Tamaño_celda)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

#Funcion para dibujar laberintos:
def dibujar_laberinto(turtle, laberinto):
    #Recorre las celdas del laberinto:
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            #centra el laberinto en el frame:
            screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda
            screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda

            #Guarda el valor de la celda actual:
            celda = laberinto[y][x]

            #Eleccion de colores de acuerdo a el simbolo:
            if celda == '#':
                dibujar_cuadrado(turtle, screen_x, screen_y, "black")

            elif celda == 'G':
                dibujar_cuadrado(turtle, screen_x, screen_y, "green")

            elif celda == 'S':
                dibujar_cuadrado(turtle, screen_x, screen_y, "blue")

            else:
                dibujar_cuadrado(turtle, screen_x, screen_y, "white")
 
#Funcion para encontrar el inicio del laberinto:
def encontrar_inicio(turtle, laberinto):
    #Recorre las celdas del laberinto:
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            #Detecta la celda con la letra S (Start):
            if laberinto[y][x] == 'S':
                
                #Coordenadas de S:
                screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda
                screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda

                #la tortuga se coloca en S
                turtle.penup()
                turtle.goto(screen_x + Tamaño_celda // 2, screen_y - Tamaño_celda // 2)
                turtle.setheading(0)

                #Devuelve la posicion de S:
                return x, y
    
    #Si no se encuentra S, manda un error:
    raise ValueError("No se encontró el punto de inicio en el laberinto.")

#Funcion para orientar tortuga depende a la direccion a la cual ira:
def orientacion_turtle(turtle, direccion):

    #Modifica el angulo de direccion de acuerdo a la direccion deseada:
    if direccion == (1,0):
        turtle.setheading(0)
    elif direccion == (0, 1):
        turtle.setheading(270)
    elif direccion == (-1, 0):
        turtle.setheading(180)
    elif direccion == (0, -1):
        turtle.setheading(90)

#Funcion para encontrar la meta con backtracking:
def buscar_meta(turtle, laberinto, x, y, visitados, ruta_actual):
    #En caso de que se encuentre la meta:
    if laberinto[y][x] == 'G':
        ruta_actual.append((x, y))
        screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda + Tamaño_celda // 2
        screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda - Tamaño_celda // 2
        turtle.goto(screen_x, screen_y)
        turtle.dot(10, "blue")  # Marca exacta sobre G
        turtle.hideturtle()
        turtle.getscreen().update()
        return True

    #Evitar repetir o chocar con muros:
    if (x, y) in visitados or laberinto[y][x] == '#':
        return False

    #Marca la celda actual como visitada para futuro conocimiento:
    visitados.add((x, y))
    ruta_actual.append((x, y))

    # Mover la tortuga a la celda actual
    screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda + Tamaño_celda // 2
    screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda - Tamaño_celda // 2
    turtle.goto(screen_x, screen_y)
    turtle.dot(10, "green")  # Celda explorada
    turtle.getscreen().update()
    time.sleep(0.02)

    # Direcciones: derecha, abajo, izquierda, arriba
    direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    #Explora en cada direccion:
    for dx, dy in direcciones:
        nuevo_x, nuevo_y = x + dx, y + dy

        if 0 <= nuevo_y < len(laberinto) and 0 <= nuevo_x < len(laberinto[0]):
            if laberinto[nuevo_y][nuevo_x] != '#' and (nuevo_x, nuevo_y) not in visitados:
                orientacion_turtle(turtle, (dx, dy))

                if buscar_meta(turtle, laberinto, nuevo_x, nuevo_y, visitados, ruta_actual):
                    turtle.dot(10, "blue")
                    return True

    # Punto sin salida se marca de color naranja:
    turtle.dot(10, "orange")

    # Retroceso físico
    ruta_actual.pop()
    if len(ruta_actual) > 0:
        paso_anterior = ruta_actual[-1]
        dx = paso_anterior[0] - x
        dy = paso_anterior[1] - y
        orientacion_turtle(turtle, (dx, dy))

        screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + paso_anterior[0] * Tamaño_celda + Tamaño_celda // 2
        screen_y = len(laberinto) * Tamaño_celda // 2 - paso_anterior[1] * Tamaño_celda - Tamaño_celda // 2
        turtle.goto(screen_x, screen_y)
        turtle.dot(10, "green")  # Camino correcto
        turtle.getscreen().update()
        time.sleep(0.02)

    return False

#Funcion para encontrar el camino mas eficiente del laberinto:
def camino_mas_corto(laberinto, inicio, meta):
    queue = deque()
    queue.append((inicio, [inicio]))
    visitados = set()
    visitados.add(inicio)

    while queue:
        (x, y), ruta = queue.popleft()

        if (x, y) == meta:
            return ruta
        
        for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(laberinto) and 0 <= nx < len(laberinto[0]):
                if laberinto[ny][nx] != '#' and (nx, ny) not in visitados:
                    queue.append(((nx, ny), ruta + [(nx, ny)]))
                    visitados.add((nx, ny))
    return []

#Funcion que imprime el laberinto a resolver:
def mostrar_laberinto(nombre):
    ventana_laberinto = tk.Tk()
    ventana_laberinto.title(f'Laberinto - {nombre}')
    ventana_laberinto.geometry("1000x700")
    ventana_laberinto.configure(bg="#292826")

    canvas_turtle = ScrolledCanvas(ventana_laberinto, width=600, height=600)
    canvas_turtle.place(x=50, y=50)

    turtle = RawTurtle(canvas_turtle)
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle._tracer(0, 0)  #Evita que se vea la animación de construcción

    turtle.screen.bgcolor("#292826")

    laberinto = maps.MAZE_DICC[nombre]

    # Dibuja laberinto sin animación
    dibujar_laberinto(turtle, laberinto)
    turtle._update()  # Dibuja todo de golpe

    # Ya puedes continuar como normalmente con la búsqueda
    x_inicio, y_inicio = encontrar_inicio(turtle, laberinto)

    ruta_actual = []
    visitados = set()
    buscar_meta(turtle, laberinto, x_inicio, y_inicio, visitados, ruta_actual)

    x_meta, y_meta = ruta_actual[-1]
    ruta_corta = camino_mas_corto(laberinto, (x_inicio, y_inicio), (x_meta, y_meta))

    time.sleep(1)  # Espera tras la búsqueda

    turtle.showturtle()
    for i in range(len(ruta_corta)):
        x, y = ruta_corta[i]

        # Orientar tortuga
        if i > 0:
            x_ant, y_ant = ruta_corta[i - 1]
            dx = x - x_ant
            dy = y - y_ant
            orientacion_turtle(turtle, (dx, dy))

        # Mover y pintar
        screen_x = -len(laberinto[0]) * Tamaño_celda // 2 + x * Tamaño_celda + Tamaño_celda // 2
        screen_y = len(laberinto) * Tamaño_celda // 2 - y * Tamaño_celda - Tamaño_celda // 2
        turtle.goto(screen_x, screen_y)
        turtle.dot(10, "blue")
        turtle.getscreen().update()
        time.sleep(0.05)

    ventana_laberinto.mainloop()

#Funcion main (llama las funciones anteriores en el orden deseado):
def main():

    #Configuracion de la ventana:
    menu_principal = tk.Tk()
    menu_principal.title("A-MAZE-ZING")
    menu_principal.geometry("525x727")
    menu_principal.configure(bg="#292826")
    menu_principal.resizable(False, False)

    #Agregar logo de la applicacion:
    Titulo_Amazezing = PhotoImage(file=RUTA_TITULO_AMZ)
    frame_titulo = tk.Frame(menu_principal, bg="#292826")
    frame_titulo.pack(pady=10)
    tk.Label(frame_titulo, image=Titulo_Amazezing, bg="#292826").pack(pady=10)

    #Canvas para botones:
    frame_canvas = tk.Frame(menu_principal, bg="#292826")
    frame_canvas.pack()
    canvas = tk.Canvas(frame_canvas, width=1100, height=430, bg="#292826", highlightthickness=0)
    canvas.pack()

    #Cargar botones:
    botones_on = {color: PhotoImage(file=os.path.join(RUTA_BOTONES, f'BtnMaze{color}On.png')) for color in colores}
    botones_off = {color: PhotoImage(file=os.path.join(RUTA_BOTONES, f'BtnMaze{color}Off.png')) for color in colores}

    fuente = ("Arial Black", 20)
    espacio_x = 260
    espacio_y = 85

    for texto, col, fila, color in metodos:
        x = espacio_x * col - espacio_x / 2
        y = espacio_y * fila - espacio_y / 2

        imagen_id = canvas.create_image(x, y + 2, image=botones_off[color])
        sombra_id = canvas.create_text(x + 2, y + 2, text=texto, font=fuente, fill="black")
        texto_id = canvas.create_text(x, y, text=texto, font=fuente, fill="white")

        def al_presionar(event, img=imagen_id, txt=texto_id, sombra=sombra_id, col=color):
            canvas.itemconfig(img, image=botones_on[col])
            canvas.itemconfig(txt, fill="gray")
            canvas.move(txt, 0, 6)
            canvas.move(sombra, 0, 6)

        def al_soltar(event, img=imagen_id, txt=texto_id, sombra=sombra_id, col=color, nombre=texto):
            canvas.itemconfig(img, image=botones_off[col])
            canvas.itemconfig(txt, fill="white")
            canvas.move(txt, 0, -6)
            canvas.move(sombra, 0, -6)
            abrir_ventana_laberinto(nombre)

        for item in [imagen_id, texto_id, sombra_id]:
            canvas.tag_bind(item, "<ButtonPress-1>", al_presionar)
            canvas.tag_bind(item, "<ButtonRelease-1>", al_soltar)

    #Funcion para cerrar la ventana del menu al seleccionar laberinto
    def abrir_ventana_laberinto(nombre):
        menu_principal.destroy()
        mostrar_laberinto(nombre)

    menu_principal.mainloop()

#Ejecucion de la funcion main:
if __name__ == "__main__":
    main()