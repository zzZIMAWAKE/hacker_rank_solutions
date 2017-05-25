import sys
from random import randint

# https://www.hackerrank.com/challenges/walking-the-approximate-longest-path
# This code is not meant to look pretty, it's the result of several iterations of implementations
# If you are looking at this, do not judge this as code quality I am proud of, this is messy as I was testing out
# several solutions for this problem.
# Currently scores 66.5/70 consistently, passes all test cases
inputs = []
for line in sys.stdin:
    inputs.append(line.split(' '))

num_cities = int(inputs[0][0])
num_roads = int(inputs[0][1])


def prepare_paths(num_roads, inputs):
    cities = []
    i = 1
    while True:
        if i >= num_cities + 1:
            break
        cities.append(i)
        i += 1
    paths = {}

    i = 1
    while True:
        if i > num_roads:
            break
        city_one = int(inputs[i][0])
        city_two = int(inputs[i][1])
        try:
            paths[city_one]
        except:
            paths[city_one] = []
        try:
            paths[city_two]
        except:
            paths[city_two] = []
        paths[city_one].append(city_two)
        paths[city_two].append(city_one)
        i += 1
    return paths, cities


def travel(paths, total_moves, order, start):
    while True:
        total_moves += 1
        order.append(start)
        if not paths[start]:
            break
        visitable = list(set(paths[start]) - set(order))
        if not visitable:
            break

        best_choice = 100000
        choices = []
        for i in visitable:
            if len(paths[i]) < best_choice:
                best_choice = len(paths[i])
                choices = []
                choices.append(i)
            if len(paths[i]) == best_choice:
                choices.append(i)

        random = randint(0, len(choices) - 1)
        start = choices[random]
    return total_moves, order


def find_start_by_lowest_count(lowest_indices):
    random_index = randint(0, len(lowest_indices) - 1)
    return lowest_indices[random_index]


def find_start_randomly(num_cities):
    return randint(1, num_cities)


def random_neighbour_strategy(paths, start):
    total_moves, order = travel(paths, 0, [], start)
    return total_moves, order


def find_paths_with_lowest_connections(paths):
    i = 1
    lowest = len(paths[1])
    lowest_idx = 1
    lowest_indices = []
    while True:
        if len(paths[i]) < lowest:
            lowest = len(paths[i])
            lowest_idx = i
            lowest_indices = []
            lowest_indices.append(i)
        if len(paths[i]) == lowest:
            lowest_indices.append(i)
        i += 1
        if i not in paths:
            break
    return lowest_indices


def run():
    i = 0
    best_moves = 0
    best_order = []
    while True:
        if i > 4:
            break
        start = find_start_by_lowest_count(lowest_indices)
        total_moves, order = random_neighbour_strategy(paths, start)
        if total_moves > best_moves:
            best_order = order
            best_moves = total_moves
        i += 1

    print(best_moves)
    print(' '.join(str(i) for i in best_order))

paths, cities = prepare_paths(num_roads, inputs)
lowest_indices = find_paths_with_lowest_connections(paths)
run()

