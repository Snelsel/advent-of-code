class WaypointFerry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_offset_x = 10
        self.waypoint_offset_y = 1
    
    def manhattan(self):
        return abs(self.x) + abs(self.y)
    
    def handle_instruction(self, instruction):
        self.handle_action(instruction[0], instruction[1])
    
    def handle_action(self, action, dist):
        # Action N means to move the waypoint north by the given value.
        # Action S means to move the waypoint south by the given value.
        # Action E means to move the waypoint east by the given value.
        # Action W means to move the waypoint west by the given value.
        # Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
        # Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        # Action F means to move forward to the waypoint a number of times equal to the given value.
        
        if action == 'N':
            self.waypoint_offset_y += dist
        elif action == 'S':
            self.waypoint_offset_y -= dist
        elif action == 'E':
            self.waypoint_offset_x += dist
        elif action == 'W':
            self.waypoint_offset_x -= dist
        elif action == 'L':
            self.turn(-1 * dist)
        elif action == 'R':
            self.turn(dist)
        elif action == 'F':
            self.x += self.waypoint_offset_x * dist
            self.y += self.waypoint_offset_y * dist
    
    def turn(self, angle):
        angle = angle % 360
        
        if angle == 90:
            (self.waypoint_offset_x, self.waypoint_offset_y) = (self.waypoint_offset_y, -1 * self.waypoint_offset_x)
        elif angle == 180:
            (self.waypoint_offset_x, self.waypoint_offset_y) = (-1 * self.waypoint_offset_x, -1 * self.waypoint_offset_y)
        elif angle == 270:
            (self.waypoint_offset_x, self.waypoint_offset_y) = (-1 * self.waypoint_offset_y, self.waypoint_offset_x)
        elif angle == 0:
            pass
        else:
            raise Exception('Unsupported angle!')
    
    def __str__(self):
        return f'Ferry position ({self.x}, {self.y}). The waypoint is {self.waypoint_offset_x} east and {self.waypoint_offset_y} north of the ship'
