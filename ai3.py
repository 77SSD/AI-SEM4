import itertools
import time

def read_input(input_file):
    first_line = input_file.readline().strip()
    n = int(input_file.readline().strip())
    coordinates = []
    distances = []
    for i in range(n):
        coordinates.append(list(map(float, input_file.readline().strip().split())))
    for i in range(n):
        distances.append(list(map(float, input_file.readline().strip().split())))
    return first_line, n, coordinates, distances

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def non_euclidean_distance(x1, y1, x2, y2):
    # add implementation for non-euclidean distance
    pass

def calculate_distance(first_line, n, coordinates, distances, i, j):
    if first_line == "euclidean":
        return euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
    else:
        return non_euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

def tour_length(tour, first_line, n, coordinates, distances):
    length = 0
    for i in range(len(tour) - 1):
        length += calculate_distance(first_line, n, coordinates, distances, tour[i], tour[i + 1])
    return length

def solve_tsp(first_line, n, coordinates, distances):
    min_length = float("inf")
    min_tour = []
    start_time = time.time()
    for tour in itertools.permutations(range(n)):
        tour_len = tour_length(tour, first_line, n, coordinates, distances)
        if tour_len < min_length:
            min_length = tour_len
            min_tour = list(tour)
        if time.time() - start_time > 300: # 300s time limit
            break
    return min_length, min_tour

def write_output(output_file, min_length, min_tour):
    output_file.write(" ".join(str(x) for x in min_tour) + "\n")
    output_file.write("%.2f" % min_length)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        first_line, n, coordinates, distances = read_input(input_file)
    min_length, min_tour = solve_tsp(first_line, n, coordinates, distances)
    with open("output.txt", "w") as output_file:
        write_output(output_file, min_length, min_tour)
