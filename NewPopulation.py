import random


def crossOver(father_list):

    son_list = [[0 for x in range(8)] for y in range(2)]
    start = random.randint(0,8)
    end = random.randint(0,8)

    if start > end:
        aux = start
        start = end
        end = start

    
    aux = father_list[0][start]

def create(fitness_list, old_population):

    new_population = [[0 for x in range(8)] for y in range(20)]

    new_population[0] = old_population[0]



    return new_population
