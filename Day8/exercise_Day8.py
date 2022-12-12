from turtle import clear
import numpy as np

def parse_input():
    currDirectory = 'Escritorio/AdventOfCode2022/Day8/'     # Dirección donde se encuentra la fichero de entrada
    input = 'inputExercise_Day8.txt'                       # Fichero de entrada
    #input = 'example_Day8.txt'

    f = open(currDirectory + input)                         # Abrimos el fichero de entrada

    lista_de_listas = []

    try:
        for line in f:
            if line != '\n':
                line = line[:-1]
                new_row = []
                for c in line:
                    new_row.append(int(c))
                lista_de_listas.append(list(new_row))
    finally:
        f.close
    
    return np.array(lista_de_listas)

def is_visible_tree(vector, pos):
    is_visible_left = True
    is_visible_right = True
    for i in range(0, pos):
        if vector[i] >= vector[pos]:
            is_visible_left = False
    if is_visible_left == False:
        for i in range (pos+1, len(vector)):
            if vector[i] >= vector[pos]:
                is_visible_right = False
    if is_visible_left == False and is_visible_right == False:
        return False
    else:
        return True

def calculate_visible_trees(matrix):
    cont = matrix.shape[0] * 4 - 4
    for i in range (1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
            if is_visible_tree(matrix[i,:], j):
                cont += 1
            elif is_visible_tree(matrix[:,j], i):
                cont += 1
    return cont

def calculate_viewing_distance_in_array(vector, pos):
    can_see_left = True
    cont_left = 1
    for i in range (1,pos):
        if vector[pos-i] < vector[pos] and can_see_left == True:
            cont_left += 1
        else:
            can_see_left = False
    
    can_see_right = True
    cont_right = 1
    for i in range (pos+1, len(vector)-1):
        if vector[i] < vector[pos] and can_see_right == True:
            cont_right+=1
        else:
            can_see_right = False
    return cont_left * cont_right

def calculate_viewing_distance(matrix, coordenates):
    horizontal_scenic_score = calculate_viewing_distance_in_array(matrix[coordenates[0],:], coordenates[1])   
    vertical_scenic_score = calculate_viewing_distance_in_array(matrix[:,coordenates[1]], coordenates[0])
    return horizontal_scenic_score * vertical_scenic_score

def problem_1():
    matrix = parse_input()
    print(calculate_visible_trees(matrix))

def problem_2():
    matrix = parse_input()
    scenic_score = 0
    for i in range(1, matrix.shape[0]-1):
        for j in range(1, matrix.shape[1]-1):
            new_viewing_distance = calculate_viewing_distance(matrix, [i,j])
            if scenic_score < new_viewing_distance:
                scenic_score = new_viewing_distance
    print(scenic_score)

if __name__ == '__main__':
    problem_1()
    problem_2()