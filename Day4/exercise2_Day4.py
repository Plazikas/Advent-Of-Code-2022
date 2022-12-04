from traceback import print_tb


currDirectory = 'Escritorio/AdventOfCode2022/Day4/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day4.txt'                       # Fichero de entrada
#input = 'example_Day4.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

cont = 0    # Contador de los pares completamente contenidos en otros

try:
    for linea in f:
        if linea != '\n':
            elves = linea[:-1].split(',')
            elf1 = elves[0].split('-')
            elf2 = elves[1].split('-')
            sectionElf1 = []
            sectionElf2 = []
            for i in range (int(elf1[0]), int(elf1[1])+1):
                sectionElf1.append(i)
            for i in range (int(elf2[0]), int(elf2[1])+1):
                sectionElf2.append(i)
            if not set(sectionElf1).isdisjoint(set(sectionElf2)):
                cont += 1 

finally:
    f.close()

print('El resultado es: ' + str (cont))