class Point:
    def __init__(self, x, y, z, state = '.'):
        (self.x, self.y, self.z, self.state) = (x, y, z, state)

class Space:
    def __init__(self, SIZE=15):
        self.SIZE = SIZE
        self.space = {}
        for x in range(-self.SIZE, self.SIZE + 1):
            self.space[x] = {}
            for y in range(-self.SIZE, self.SIZE + 1):
                self.space[x][y] = {}
                for z in range(-self.SIZE, self.SIZE + 1):
                    self.space[x][y][z] = '.'

    def clone(self):
        new_space = Space()
        new_space.apply_list(self.points())
        return new_space

    def apply_list(self, points):
        for point in points:
            self.apply(point)
    
    def apply(self, p):
        self.space[p.x][p.y][p.z] = p.state
    
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
                    points.append(Point(x, y, z, self.space[x][y][z]))
        return points
    
    def print_at_z(self, z, s):
        size = self.SIZE if s == None else s
        for y in range(-size, size + 1):
            line = []
            for x in range(-size, size + 1):
                line.append(self.space[x][y][z])
            print(''.join(line))
    
    def count_active_neighbors(self, x_target, y_target, z_target):
        count = 0
        for x in range(max(x_target - 1, -self.SIZE), min(x_target + 1, self.SIZE) + 1):
            for y in range(max(y_target - 1, -self.SIZE), min(y_target + 1, self.SIZE) + 1):
                for z in range(max(z_target - 1, -self.SIZE), min(z_target + 1, self.SIZE) + 1):
                    # print(f'Checking ({x}, {y}, {z}), state: {self.space[x][y][z]}')
                    if x == x_target and y == y_target and z == z_target:
                        # print('Skipping myself')
                        pass
                    elif self.space[x][y][z] == '#':
                        # print('Increase count!')
                        count += 1
        return count
    
    def cycle(self):
        new_space = self.clone()
        for x in range(-self.SIZE, self.SIZE + 1):
            for y in range(-self.SIZE, self.SIZE + 1):
                for z in range(-self.SIZE, self.SIZE + 1):
                    active_neighbors = self.count_active_neighbors(x, y, z)
                    if self.space[x][y][z] == '#':
                        if active_neighbors < 2 or active_neighbors > 3:
                            new_space.apply(Point(x, y, z, '.'))
                    else:
                        if active_neighbors == 3:
                            new_space.apply(Point(x, y, z, '#'))
                        
        return new_space

def parse():
    points = []
    with open('input') as input:
        for y, line in enumerate(input):
            for x, s in enumerate(line.strip()):
                points.append(Point(x, y, 0, s))
    return points

space = Space()

points = parse()
space.apply_list(points)

# print(space.count_active())
# print(space.clone().count_active())

# print('Before any cycles:')
# print('z=0')
# space.print_at_z(0, 3)

# print('After clone:')
# print('z=0')
# space.clone().print_at_z(0, 3)

# print('active around 0,0,0', space.count_active_neighbors(0, 0, 0))

space = space.cycle()

# print('active around 0,0,0', space.count_active_neighbors(0, 0, 0))

# print('After 1 cycle:')
# print('z=-1')
# space.print_at_z(-1, 4)
# print('z=0')
# space.print_at_z(0, 4)
# print('z=1')
# space.print_at_z(1, 4)

space = space.cycle()

# print('After 2 cycles:')
# print('z=-2')
# space.print_at_z(-2, 4)
# print('z=-1')
# space.print_at_z(-1, 4)
# print('z=0')
# space.print_at_z(0, 4)
# print('z=1')
# space.print_at_z(1, 4)
# print('z=2')
# space.print_at_z(2, 4)

space = space.cycle()
space = space.cycle()
space = space.cycle()
space = space.cycle()

print(space.count_active())


