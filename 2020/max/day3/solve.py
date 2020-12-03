forest = open('input', 'r').readlines()

collisions = 0
width = len(forest[0].strip())

for i in range(len(forest)):
    x = i*3 % width
    if forest[i][x] == '#':
        collisions += 1

print(collisions)