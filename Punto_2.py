import numpy as np
import matplotlib.pyplot as plt

class TSPGeneticAlgorithm:
    def __init__(self, num_cities=10):
        self.num_cities = num_cities
        self.cities = self.generate_cities(num_cities)

    def generate_cities(self, n):
        return [[np.random.random(), np.random.random()] for _ in range(n)]

    def distance(self, city1, city2):
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def total_distance(self, route):
        return sum(self.distance(self.cities[route[i]], self.cities[route[i+1]])
                  for i in range(len(route)-1))

    def fitness(self, route):
        return 1 / self.total_distance(route)

    def crossover(self, parent1, parent2):
        size = len(parent1)
        start, end = sorted(np.random.choice(size, 2, replace=False))
        child = [-1] * size
        child[start:end] = parent1[start:end]
        remaining = [x for x in parent2 if x not in child[start:end]]
        j = 0
        for i in range(size):
            if child[i] == -1:
                child[i] = remaining[j]
                j += 1
        return child

    def mutation(self, route):
        i, j = np.random.choice(len(route), 2, replace=False)
        route[i], route[j] = route[j], route[i]
        return route

    def plot_route(self, route):
        x = [self.cities[route[i]][0] for i in range(len(route))] + [self.cities[route[0]][0]]
        y = [self.cities[route[i]][1] for i in range(len(route))] + [self.cities[route[0]][1]]
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, '-o')
        plt.title("Ruta óptima del Viajante")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.show()

if __name__ == "__main__":
    tsp = TSPGeneticAlgorithm()

    current_route = list(range(tsp.num_cities))
    np.random.shuffle(current_route)

    mutated_route = tsp.mutation(current_route.copy())

    initial_distance = tsp.total_distance(current_route)
    mutated_distance = tsp.total_distance(mutated_route)

    print(f"Distancia inicial: {initial_distance}")
    print(f"Distancia después de mutación: {mutated_distance}")

    tsp.plot_route(current_route)