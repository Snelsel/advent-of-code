import sys
def parse():
    rows = []
    with open('input') as input:
        for line in input:
            row = []
            for s in line.strip():
                row.append(s)
            rows.append(row)
    return rows

def process(seats, debug = False):
    updated_seats = []
    state_changed = False
    for r, row in enumerate(seats):
        updated_row = []
        for c, col in enumerate(row):
            occ = count_adj_occ(seats, r, c)
            state = row[c]
            if debug:
                print(f'Found {occ} occupied seats near {r}, {c} (={state})')
            new_state = state
            if state == 'L':
                if occ == 0:
                    new_state = '#'
                    state_changed = True
            elif state == '#':
                if occ >= 4:
                    new_state = 'L'
                    state_changed = True
            updated_row.append(new_state)
        updated_seats.append(updated_row)

    if not state_changed:
        raise Exception('No state changed')
    return updated_seats

def count_adj_occ(seats, row, col, debug = False):
    sum = -1 if seats[row][col] == '#' else 0
    for r in range(max(0, row - 1), min(len(seats), row + 2)):
        for c in range(max(0, col - 1), min(len(seats[row]), col + 2)):
            if debug:
                print(f'Checking at {r}, {c} (= {seats[r][c]})')
            if seats[r][c] == '#':
                sum += 1 
    return sum

def process_part2(seats, debug = False):
    updated_seats = []
    state_changed = False
    for r, row in enumerate(seats):
        updated_row = []
        for c, col in enumerate(row):
            occ = count_vis_occ(seats, r, c, debug and c==0 and r==0)
            state = row[c]
            if debug:
                print(f'Found {occ} occupied seats in sight from {r}, {c} (={state})')
            new_state = state
            if state == 'L':
                if occ == 0:
                    new_state = '#'
                    state_changed = True
            elif state == '#':
                if occ >= 5:
                    new_state = 'L'
                    state_changed = True
            updated_row.append(new_state)
        updated_seats.append(updated_row)

    if not state_changed:
        raise Exception('No state changed')
    return updated_seats

def count_vis_occ(seats, row, col, debug = False):
    sum = 0
    if debug:
        print(f'Will determine the visible occupied seats when looking from {row}, {col}')
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            if debug:
                print(f'  Angle dx:{dx}, dy:{dy}')

            hit = False
            i = 1
            while not hit:
                if i > 1000:
                    raise Exception('Infinite loop likely')
                
                r = row + dx * i
                c = col + dy * i
                
                if r < 0 or r >= len(seats):
                    if debug:
                        print('    hit a side wall!')
                    break
                if c < 0 or c >= len(seats[r]):
                    if debug:
                        print('    hit a top/bottom wall!')
                    break

                if debug:
                    print(f'    when i={i} I will check {r}, {c}')
                
                v = seats[row + dx * i][col + dy * i]
                
                if debug:
                    print(f'      value = {v}')
                
                if v == '#':
                    sum += 1
                    hit = True
                    if debug:
                        print('    hit!')
                elif v == 'L':
                    hit = True
                    if debug:
                        print('    hit!')
            
                i += 1
    return sum

def pretty(seats):
    for r, row in enumerate(seats):
        print(''.join(row))
    print('------------')
    print('')

def count_occ(seats):
    count = 0
    for r, row in enumerate(seats):
        for c, col in enumerate(row):
            if row[c] == '#':
                count += 1
    return count

seats = parse()
try:
    while True:
        seats = process_part2(seats)
        #pretty(seats)
except:
    print(sys.exc_info())
    print(count_occ(seats))
