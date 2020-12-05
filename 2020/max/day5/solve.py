import re

def find_row(row_instr):
    possible_rows = range(0, 128)

    for dir in row_instr:
        mid = int(len(possible_rows)/2)
        
        if dir == 'F':
            possible_rows = possible_rows[:mid]
        else:
            possible_rows = possible_rows[mid:]

    return possible_rows[0]


def find_col(col_instr):
    possible_cols = range(0, 8)

    for dir in col_instr:
        mid = int(len(possible_cols)/2)
        
        if dir == 'L':
            possible_cols = possible_cols[:mid]
        else:
            possible_cols = possible_cols[mid:]
    
    return possible_cols[0]

def to_seat_id(row, col):
    return row*8 + col

def boarding_pass_to_seat_id(boarding_pass):
    (row_instr, col_instr) = re.findall('^([FB]{7})([LR]{3})$', boarding_pass)[0]
    row = find_row(row_instr)
    col = find_col(col_instr)
    seat_id = to_seat_id(row, col)

    return seat_id

def parse():
    seat_ids = []
    with open('input') as input:
        for line in input:
            boarding_pass = line.strip()
            seat_id = boarding_pass_to_seat_id(boarding_pass)
            seat_ids.append(seat_id)
    
    seat_ids.sort()
    return seat_ids

def find_max(seat_ids):
    return seat_ids[len(seat_ids)-1]

def find_gap(seat_ids):
    prev = None
    for seat_id in seat_ids:
        if prev is not None and seat_id > prev + 1:
            return seat_id - 1
        prev = seat_id

seat_ids = parse()

print(f'Part 1: {find_max(seat_ids)}')
print(f'Part 1: {find_gap(seat_ids)}')
