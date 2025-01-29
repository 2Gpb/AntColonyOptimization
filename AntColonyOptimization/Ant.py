import numpy as np


class Ant:
    def __init__(self, points, pheromone, alpha, beta):
        self.__points = points
        self.__pheromone = pheromone
        self.__alpha = alpha
        self.__beta = beta
        self.path = []
        self.path_length = 0

    @staticmethod
    def __distance(point1, point2):
        return np.linalg.norm(point1 - point2)

    def __select_next_point(self, current_point, unvisited):
        probabilities = np.array([
            (self.__pheromone[current_point, u] ** self.__alpha) /
            (self.__distance(self.__points[current_point], self.__points[u]) ** self.__beta)
            for u in unvisited
        ])

        probabilities /= probabilities.sum()
        return np.random.choice(unvisited, p=probabilities)

    def construct_solution(self, n_points):
        visited = np.zeros(n_points, dtype=bool)
        current_point = np.random.randint(n_points)
        visited[current_point] = True
        self.path = [current_point]
        self.path_length = 0

        while not visited.all():
            unvisited = np.where(~visited)[0]
            next_point = self.__select_next_point(current_point, unvisited)
            self.path.append(next_point)
            self.path_length += self.__distance(self.__points[current_point], self.__points[next_point])
            visited[next_point] = True
            current_point = next_point
