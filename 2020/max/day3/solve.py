import numpy

forest = open('input', 'r').readlines()

width = len(forest[0].strip())

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
all_collisions = []

for (right, down) in slopes:
    collisions = 0
    i = 0
    while i * down < len(forest):
        x = i * right % width
        y = i * down
        if forest[y][x] == '#':
            collisions += 1
        i += 1
    all_collisions.append(collisions)

print(numpy.prod(all_collisions))