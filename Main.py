import Matrix
import InitialPopulation
import CitysList
import FitnessFunction
import NewPopulation

def main():
    city_list = CitysList.create()
    matrix = Matrix.create()
    population = InitialPopulation.create()
    for x in range(2):
        fitness_list = FitnessFunction.create(population).copy()
        population = NewPopulation.create(population).copy()

main()