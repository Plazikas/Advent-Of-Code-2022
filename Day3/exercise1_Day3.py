# Función que devuelve qué elemento se encuentra en ambos compartimentos
def ItemShared(campartement1, compartement2):
    for c in compartement1:
        if c in compartement2:
            return c

# Función que calcula la suma de una lista de items a-z da 1-26 y A-Z da 27-52 respectivamente
def SumItems(lista):
    suma = 0
    for c in lista:
        if c.islower():
            suma += ord(c) - ord('a') + 1
        else:
            suma += ord(c) - ord('A') + 27

    return suma

currDirectory = 'Escritorio/AdventOfCode2022/Day3/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day3.txt'                       # Fichero de entrada
input = 'example_Day3.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

sharedItems = []        # Lista donde almacenamos los items compartidos
try:
    for linea in f:
        if linea != '\n':
            compartement1 = linea[:int(len(linea)/2)]
            compartement2 = linea[int(len(linea)/2):]
            
            sharedItems.append(ItemShared(compartement1, compartement2))
finally:
    f.close()

print('La suma total es: ' + str(SumItems(sharedItems)))