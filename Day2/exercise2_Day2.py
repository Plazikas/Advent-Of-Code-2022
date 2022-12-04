from string import punctuation

# Función que indica qué forma necesito para ganar, empatar o perder
def SelectFormToAResult(rival, me):
    if me == 'X':
        if rival == 'A':
            return 'Z'
        elif rival == 'B':
            return 'X'
        else:
            return 'Y'
    elif me == 'Y':
        if rival == 'A':
            return 'X'
        elif rival == 'B':
            return 'Y'
        else:
            return 'Z'
    else:
            if rival == 'A':
                return 'Y'
            elif rival == 'B':
                return 'Z'
            else:
                return 'X'

# Función que devuelve el número de puntos obtenidos en función de si se gana, empata o pierde
def PointsPerResult(rival, me):
    if rival == 'A':
        if me == 'Y':
            return 6
        elif me == 'X':
            return 3
        else: 
            return 0
    elif rival == 'B':
        if me == 'Z':
            return 6
        elif me == 'Y':
            return 3
        else:
            return 0
    else:
        if me == 'X':
            return 6
        elif me == 'Z':
            return 3
        else:
            return 0

# Función que devuelve el número de puntos obtenidos en función de la figura que saque
def PointsPerForm(me):
    if me == 'X':
        return 1
    elif me == 'Y':
        return 2
    else:
        return 3

currDirectory = 'Escritorio/AdventOfCode2022/Day2/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day2.txt'                      # Fichero de entrada
#input = 'example_Day2.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

punctuation = 0                                         # Variable que almacena la puntuación que llevamos

try:
    for linea in f:
        if linea != '\n':
            forms = linea.split()                            # Lista que contiene en [0] la forma del rival y en [1] la nuestra
            forms[1] = SelectFormToAResult(forms[0],forms[1])   # Cambiamos nuestra figura en fucnión de si queremos ganar, empatar o perder
            punctuation += PointsPerResult(forms[0], forms[1])  # Sumamos la puntuación obtenida por el resultado
            punctuation += PointsPerForm(forms[1])              # Sumamos la puntuación obtenida por la forma sacada
finally:
    f.close()

print(punctuation)