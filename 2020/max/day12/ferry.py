class Ferry:
    def __init__(self):
        self.dir = 'E'
        self.x = 0
        self.y = 0
    
    def manhattan(self):
        return abs(self.x) + abs(self.y)
    
    def handle_instruction(self, instruction):
        self.handle_action(instruction[0], instruction[1])
    
    def handle_action(self, action, dist):
        # Action N means to move north by the given value.
        # Action S means to move south by the given value.
        # Action E means to move east by the given value.
        # Action W means to move west by the given value.
        # Action L means to turn left the given number of degrees.
        # Action R means to turn right the given number of degrees.
        # Action F means to move forward by the given value in the direction the ship is currently facing.
        
        if action == 'N':
            self.y += dist
        elif action == 'S':
            self.y -= dist
        elif action == 'E':
            self.x += dist
        elif action == 'W':
            self.x -= dist
        elif action == 'L':
            self.turn(-1 * dist)
        elif action == 'R':
            self.turn(dist)
        elif action == 'F':
            self.handle_action(self.dir, dist)
    
    def turn(self, angle):
        steps = int((angle % 360) / 90)
        dirs = ['N', 'E', 'S', 'W']
        self.dir = dirs[ ( dirs.index(self.dir) + steps ) % 4 ]