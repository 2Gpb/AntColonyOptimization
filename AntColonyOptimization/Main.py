from AntColonyOptimization import *
import matplotlib.pyplot as plt
import time


def print_banner():
    print("=" * 60)
    print(" " * 18 + "Optimization Completed")
    print("=" * 60 + "\n")


def print_results(points, best_path, best_path_length, execution_time):
    for i, point in enumerate(best_path):
        end = " ->" if i < len(best_path) - 1 else ""
        print(f"Point {point}: {points[point]}{end}")

    print("\nBest Path (Indices):", " -> ".join(map(str, best_path)) + " -> " + str(best_path[0]))

    print(f"\nBest Path Length: {best_path_length:.4f}")
    print(f"Execution Time: {execution_time:.4f} sec\n")

    print("=" * 60)


def main():
    print_banner()

    dimension = 3
    coordinates = np.random.rand(10, dimension)

    aco = AntColonyOptimization(
        points=coordinates,
        n_ants=10,
        iterations=100,
        alpha=1,
        beta=1,
        evaporation_rate=0.7,
        q=1
    )

    start_time = time.time()
    best_path, best_path_length = aco.optimize()
    execution_time = time.time() - start_time

    print_results(coordinates, best_path, best_path_length, execution_time)

    fig = plt.figure(figsize=(8, 6))

    match dimension:
        case 2:
            plt.scatter(coordinates[:, 0], coordinates[:, 1], c='red', marker='o', label="Cities")
            for i in range(len(best_path)):
                start = coordinates[best_path[i]]
                end = coordinates[best_path[(i + 1) % len(best_path)]]
                plt.plot([start[0], end[0]], [start[1], end[1]], 'b-')

            plt.title(f"Optimized Path in 2D | Distance: {best_path_length:.4f}")
            plt.legend()
            plt.show()
        case 3:
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], c='red', marker='o', label="Cities")
            for i in range(len(best_path)):
                start = coordinates[best_path[i]]
                end = coordinates[best_path[(i + 1) % len(best_path)]]
                ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 'b-')

            ax.set_title(f"Optimized Path in 3D | Distance: {best_path_length:.4f}")
            plt.show()
        case _:
            print("Invalid dimension for the graph! Choose 2 or 3.")


if __name__ == "__main__":
    main()
