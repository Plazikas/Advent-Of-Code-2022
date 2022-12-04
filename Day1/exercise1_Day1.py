from ast import operator
import os
currDirectory = 'Escritorio/AdventOfCode2022/Day1/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day1.txt'                        # Fichero de entrada

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

print('El valor máximo es: ' + str(max(Elves)))         # Mostramos el mayor valor que carga un elfo