from ast import operator
import os
currDirectory = 'Escritorio/AdventOfCode2022/Day1/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day1.txt'                        # Fichero de entrada
#input = 'example_Day1.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

Elves = []                                              # Array donde se guarda cuántas calorias lleva cada elfo   
cont = 0                                                # Número de calorias que lleva un elfo                                        
    
try:
    for linea in f:                                     # Leemos el fichero línea por línea
        if linea != '\n':                               # Si la línea no es vacía
            cont = cont + int(linea)                    # Sumamos la cantidad a la carga del elfo
        else:                                           # en otro caso
            Elves.append(cont)                          # guardamos el peso que lleva el elfo
            cont = 0                                    # reiniciamos la carga a 0
finally:                                                # Cuando no haya más líneas
    f.close()                                           # Cerramos el fichero

threeHigher = [0,0,0]                                   # Lista donde almacenamos los tres valores más altos
for v in Elves:                                         # Mientras haya elementos en la lista Elves
    if v > threeHigher[0]:                              # Si v es mayor que el elemento más bajo de los tres más altos
        threeHigher[0] = v                              # lo sustituye
        threeHigher.sort()                              # y reordena la lista de los tres más altos

print('La suma de los tres elfos con más calorias es: ' + str(sum(threeHigher)))    # Se muestra la suma de los tres valores más altos