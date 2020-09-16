import Matrix

def calculate(list, matrix):
    distance = matrix[9][list[0]]
    for x in list:
        if x != 8:
            distance += matrix[list[x]][list[x+1]]
        else:
            distance += matrix[list[x]][9]
    return distance

def create(population):
    matrix = Matrix.create()
    list = [0 for x in range(20)]
    for x in range(len(population)):
        list[x] = calculate(population[x], matrix)
    print(list)
    list_sort = list.copy()
    list_sort.sort()
    list_final = [0 for x in range(20)]
    for x in range(20):
        y = 0
        while list_sort[x] != list[y]:
            y += 1
        list_final[x] = y
        list[y] = 0
    print(list_sort)
    print(list_final)
    return list_final