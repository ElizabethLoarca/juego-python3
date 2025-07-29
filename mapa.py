import os
WIDTH_MAPA = 25
HEIHT_MAPA = 20
espacio_vacio = "   "
espacio_lleno = "[ ]"


coordenada_personaje = [8,10]
personaje = '▲'

def cargar_mapa(movimiento_personaje):

    #Menú
    #cargar_menu ()
    os.system('cls')
    if movimiento_personaje =='w':
        personaje ='▲'
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == 's':
        personaje = '▼'
        coordenada_personaje[0] += 1
    elif movimiento_personaje == 'a':
        personaje = '◀'
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == 'd':
        personaje = '▶'
        coordenada_personaje[1] += 1

    print("+"+"-"*75+ "+")
 #Damos indicaciones de los item
    for cada_fila in range(HEIHT_MAPA):
        print("|", end="")
        for cada_item in range(WIDTH_MAPA):
            if (coordenada_personaje[0]== cada_fila and coordenada_personaje[1]==cada_item):
                print(f" {personaje} ", end= "")
            else:
                print(espacio_vacio, end="")

 #imprime nada
        print("|")
    print("+"+"-"*75+ "+")