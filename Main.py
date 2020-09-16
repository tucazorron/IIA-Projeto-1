import Matrix
import InitialPopulation
import CitysList
import FitnessFunction
import NewPopulation

def main():
    city_list = CitysList.create()
    matrix = Matrix.create()
    population = InitialPopulation.create()
    for x in range(5):
        fitness_list = FitnessFunction.create(population)
        population = NewPopulation.create(fitness_list, population)



    print(city_list[9])
    print(population[8])
    print(matrix[4][2])

main()