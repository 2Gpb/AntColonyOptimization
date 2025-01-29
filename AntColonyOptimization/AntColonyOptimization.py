from Ant import *


class AntColonyOptimization:
    def __init__(self, points, n_ants, n_iterations, alpha, beta, evaporation_rate, q):
        self.__n_iterations = n_iterations
        self.__points = points
        self.__n_ants = n_ants
        self.__alpha = alpha
        self.__beta = beta
        self.__evaporation_rate = evaporation_rate
        self.__q = q

    @staticmethod
    def __initialize_pheromones(n_points):
        return np.ones((n_points, n_points))

    def __update_pheromones(self, pheromone, ants):
        pheromone *= self.__evaporation_rate
        for ant in ants:
            deposit = self.__q / ant.path_length
            for i in range(len(ant.path) - 1):
                pheromone[ant.path[i], ant.path[i + 1]] += deposit
            pheromone[ant.path[-1], ant.path[0]] += deposit
        return pheromone

    def optimize(self):
        n_points = len(self.__points)
        pheromone = self.__initialize_pheromones(n_points)
        best_path, best_path_length = None, np.inf

        for _ in range(self.__n_iterations):
            ants = [Ant(self.__points, pheromone, self.__alpha, self.__beta) for _ in range(self.__n_ants)]
            for ant in ants:
                ant.construct_solution(n_points)

            best_iter_ant = min(ants, key=lambda agent: agent.path_length)
            if best_iter_ant.path_length < best_path_length:
                best_path, best_path_length = best_iter_ant.path, best_iter_ant.path_length

            pheromone = self.__update_pheromones(pheromone, ants)

        print(best_path)
        print(best_path_length)
        return best_path, best_path_length


coordinates = np.random.rand(10, 2)
a = AntColonyOptimization(coordinates, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.7, q=1)
a.optimize()
