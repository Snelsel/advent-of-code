def parse():
    earliest_depart = None
    bus_ids = []
    with open('input') as input:
        for line in input:
            if earliest_depart is None:
                earliest_depart = int(line.strip())
            else:
                for str in line.strip().split(','):
                    if str != 'x':
                        bus_ids.append(int(str))
    return (earliest_depart, bus_ids)

def process(earliest_depart, bus_ids):
    min_wait = 100000000
    min_wait_bus_id = None
    for bus_id in bus_ids:
        wait = bus_id - earliest_depart % bus_id
        if wait < min_wait:
            min_wait = wait
            min_wait_bus_id = bus_id
    return (min_wait_bus_id, min_wait, min_wait_bus_id * min_wait)

(earliest_depart, bus_ids) = parse()
print(process(earliest_depart, bus_ids))