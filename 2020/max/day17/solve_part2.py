from datetime import datetime

class Point:
    def __init__(self, x, y, z, w, state = '.'):
        (self.x, self.y, self.z, self.w, self.state) = (x, y, z, w, state)

class Space:
    def __init__(self, SIZE=12):
        self.SIZE = SIZE
        self.space = {}
        for x in range(-self.SIZE, self.SIZE + 1):
            self.space[x] = {}
            for y in range(-self.SIZE, self.SIZE + 1):
                self.space[x][y] = {}
                for z in range(-self.SIZE, self.SIZE + 1):
                    self.space[x][y][z] = {}
                    for w in range(-self.SIZE, self.SIZE + 1):
                        self.space[x][y][z][w] = '.'

    def clone(self):
        new_space = Space()
        new_space.apply_list(self.points())
        return new_space

    def apply_list(self, points):
        for point in points:
            self.apply(point)
    
    def apply(self, p):
        self.space[p.x][p.y][p.z][p.w] = p.state
    
    def count_active(self):
        count = 0
        for point in self.points():
            count += 1 if point.state == '#' else 0
        return count

    def points(self):
        points = []
        for x in range(-self.SIZE, self.SIZE + 1):
            for y in range(-self.SIZE, self.SIZE + 1):
                for z in range(-self.SIZE, self.SIZE + 1):
                    for w in range(-self.SIZE, self.SIZE + 1):
                        points.append(Point(x, y, z, w, self.space[x][y][z][w]))
        return points
    
    def print_at_z_w(self, z, w, s):
        size = self.SIZE if s == None else s
        for y in range(-size, size + 1):
            line = []
            for x in range(-size, size + 1):
                line.append(self.space[x][y][z][w])
            print(''.join(line))
    
    def count_active_neighbors(self, x_target, y_target, z_target, w_target):
        count = 0
        for x in range(max(x_target - 1, -self.SIZE), min(x_target + 1, self.SIZE) + 1):
            for y in range(max(y_target - 1, -self.SIZE), min(y_target + 1, self.SIZE) + 1):
                for z in range(max(z_target - 1, -self.SIZE), min(z_target + 1, self.SIZE) + 1):
                    for w in range(max(w_target - 1, -self.SIZE), min(w_target + 1, self.SIZE) + 1):
                        # print(f'Checking ({x}, {y}, {z}), state: {self.space[x][y][z]}')
                        if x == x_target and y == y_target and z == z_target and w == w_target:
                            # print('Skipping myself')
                            pass
                        elif self.space[x][y][z][w] == '#':
                            # print('Increase count!')
                            count += 1
        return count
    
    def cycle(self):
        new_space = self.clone()
        for x in range(-self.SIZE, self.SIZE + 1):
            for y in range(-self.SIZE, self.SIZE + 1):
                for z in range(-self.SIZE, self.SIZE + 1):
                    for w in range(-self.SIZE, self.SIZE + 1):
                        active_neighbors = self.count_active_neighbors(x, y, z, w)
                        if self.space[x][y][z][w] == '#':
                            if active_neighbors < 2 or active_neighbors > 3:
                                new_space.apply(Point(x, y, z, w, '.'))
                        else:
                            if active_neighbors == 3:
                                new_space.apply(Point(x, y, z, w, '#'))
                        
        return new_space

def parse():
    points = []
    with open('input') as input:
        for y, line in enumerate(input):
            for x, s in enumerate(line.strip()):
                points.append(Point(x, y, 0, 0, s))
    return points

space = Space()

points = parse()
space.apply_list(points)

# print(space.count_active())
# print(space.count_active_neighbors(0, 0, 0, 0))

for i in range(1, 7):
    space = space.cycle()
    print(f'Cycle {i} completed at {datetime.now()}')
    print(f'Active after cycle: {space.count_active()}')

