import sys
from random import randint

# https://www.hackerrank.com/challenges/walking-the-approximate-longest-path
# Currently scores 49.0/70.0 consistently, passes up to test case #15
# I think to improve this further we need to improve performance so that we can pass the last 5 test cases
# Currently they timeout.

inputs = []
for line in sys.stdin:
    inputs.append(line.split(' '))

num_cities = int(inputs[0][0])
num_roads = int(inputs[0][1])

road_layout = []
cities = []
i = 1
while True:
    if i >= num_cities + 1:
        break
    cities.append(i)
    i += 1
paths = {}


def construct_must_visit():
    i = 1
    must_visit = []
    while True:
        if i >= num_cities + 1:
            break
        must_visit.append(i)
        i += 1
    return must_visit

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
    paths[city_one] = list(set(paths[city_one]))
    paths[city_two] = list(set(paths[city_two]))
    i += 1


def travel(must_visit, paths, total_moves, order, start):
    total_moves += 1
    order.append(start)
    if not paths[start] or not must_visit:
        return total_moves, order
    visitable = list(set(paths[start]) - set(order))
    if not visitable:
        return total_moves, order

    random = randint(0, len(visitable) - 1)
    return travel(must_visit, paths, total_moves, order, visitable[random])


def find_start_randomly(paths):
    return randint(1, len(paths) - 1)


def find_start_by_lowest_count(lowest_indices):
    random_index = randint(0, len(lowest_indices) - 1)
    return lowest_indices[random_index]


def random_neighbour_strategy(paths, lowest_indices):
    best_moves = 0
    best_order = 0
    best_start = 0
    must_visit = construct_must_visit()
    i = 0
    while True:
        if i >= 200:
            break
        if i <= 5:
            start = find_start_by_lowest_count(lowest_indices)
        if i > 5 and i < 10:
            start = find_start_randomly(paths)
        if i >= 10:
            start = best_start
        total_moves, order = travel(must_visit, paths, 0, [], start)
        if best_moves < total_moves:
            best_moves = total_moves
            best_order = order
            best_start = start
        i+= 1
    return best_moves, best_order


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

total_moves = 0
order = []
total_moves, order = random_neighbour_strategy(paths, lowest_indices)
print(total_moves)
print(' '.join(str(i) for i in order))
