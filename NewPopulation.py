import random

def crossOver(father_matrix): # ta dando erro

    print(father_matrix)

    son_matrix = father_matrix.copy()
    start = random.randint(0,8)
    end = random.randint(0,8)


    if start > end:
        aux = start
        start = end
        end = aux
    
    print(start)
    print(end)

    reps = end - start + 1
    crossover_matrix = [[0 for x in range(reps)] for y in range(2)]

    for x in range(reps):
        crossover_matrix[0][x] = father_matrix[0][start + x]
        crossover_matrix[1][x] = father_matrix[1][start + x]

    for x in range(reps):
        son_matrix[0][start + x] = crossover_matrix[1][x]
        son_matrix[1][start + x] = crossover_matrix[0][x]

    for x in range(8):
        for y in range(reps):
            if x < start or x > end:
                if son_matrix[0][x] == crossover_matrix[1][y]:
                    son_matrix[0][x] = crossover_matrix[0][y]
                if son_matrix[1][x] == crossover_matrix[0][y]:
                    son_matrix[1][x] = crossover_matrix[1][y]

    print(son_matrix)

    return son_matrix

def mutation(list): # ta funcionando

    # print(list)

    first = random.randint(0,8)
    second = random.randint(0,8)

    # print(first)
    # print(second)

    if first != second:
        aux = list[first]
        list[first] = list[second]
        list[second] = aux

    # print(list)

    return list

def create(old_population):

    new_population = [[0 for x in range(8)] for y in range(20)]
    matrix_aux = [[0 for x in range (8)] for y in range(2)]

    new_population[0] = old_population[0].copy()

    for x in range(5):
        y = x * 2
        matrix_aux[0] = old_population[y].copy()
        matrix_aux[1] = old_population[y + 1].copy()
        matrix_aux = crossOver(matrix_aux).copy()
        new_population[y + 1] = matrix_aux[0].copy()
        new_population[y + 2] = matrix_aux[1].copy()

    for x in range(9):
        x += 11
        new_population[x] = mutation(old_population[x]).copy()

    return new_population
