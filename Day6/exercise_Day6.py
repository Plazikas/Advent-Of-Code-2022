from email import message


def number_processed(line):    
    cont = 0
    finded = False
    subsequent = ''
    message_length = 14
    while finded == False and len(line) > cont:
        if line[cont] in subsequent:
            subsequent = subsequent[subsequent.find(line[cont]) + 1:] + line[cont]
        else:
            subsequent += line[cont]
        
        if len(subsequent) == message_length:
            finded = True
        else:
            cont += 1
    return line.find(subsequent) + message_length

def parse_input():
    currDirectory = 'Escritorio/AdventOfCode2022/Day6/'     # Dirección donde se encuentra la fichero de entrada
    input = 'inputExercise_Day6.txt'                       # Fichero de entrada
    #input = 'example_Day6.txt'

    f = open(currDirectory + input)                         # Abrimos el fichero de entrada

    inputs = []
    try:
        for linea in f:
            if linea != '\n':
                inputs.append(linea)

    finally:
        f.close()

    return inputs

def problem_1():
    inputs = parse_input()
    for line in inputs:
        print('El resutado es: ' + str (number_processed(line)))
        print()

problem_1()