import re
from ferry import Ferry
from waypoint_ferry import WaypointFerry

def parse():
    instructions = []
    with open('input') as input:
        for line in input:
            (action, dist) = re.findall('^([NESWLRF])([0-9]+)$', line.strip())[0]
            instructions.append( (action, int(dist)) )
    return instructions

def process_part1(instructions):
    ferry = Ferry()
    for instruction in instructions:
        ferry.handle_instruction(instruction)
    return ferry.manhattan()

def process_part2(instructions):
    waypoint_ferry = WaypointFerry()
    for instruction in instructions:
        waypoint_ferry.handle_instruction(instruction)
        #print(instruction, waypoint_ferry)
    return waypoint_ferry.manhattan()


instructions = parse()
print(process_part1(instructions))
print(process_part2(instructions))