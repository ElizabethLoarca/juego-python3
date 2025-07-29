import os
import readchar
from mapa import cargar_mapa

estado_juego =True

print("------------------------------------")
  #Iniciar juego 

def Juego_1():   
   tecla = readchar.readchar()

   if tecla =='w':
       cargar_mapa(tecla)
   elif tecla =='s':
       cargar_mapa(tecla)
   elif tecla =='a':
       cargar_mapa(tecla)
   elif tecla =='d':
      cargar_mapa(tecla)
   elif tecla == "q":
      estado_juego = False
Juego_1
while estado_juego:
   Juego_1()
