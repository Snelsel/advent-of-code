from operator import itemgetter

def parse(input):
    buses = []
    for i, c in enumerate(input.split(',')):
        if c != 'x':
            buses.append((i, int(c)))
    return buses

def process(buses):
    sorted_buses = sorted(buses, key=itemgetter(1))
    
    bus_with_highest_k = sorted_buses.pop()

    sorted_buses = sorted(buses, key=itemgetter(1), reverse=True)

    offset = bus_with_highest_k[0]
    k = bus_with_highest_k[1]

    i = 0
    while True:
        if i > 100000000000:
            raise Exception('Infinite loop')

        t = i * k - offset
        if valid(t, sorted_buses):
            return t
        i += 1

def valid(t, buses):
    for bus in buses:
        if (t + bus[0]) % bus[1] != 0:
            return False
    return True


print(3417, process(parse('17,x,13,19')) == 3417)
print(754018, process(parse('67,7,59,61')) == 754018)
print(779210, process(parse('67,x,7,59,61')) == 779210)
print(1261476, process(parse('67,7,x,59,61')) == 1261476)
print(1202161486, process(parse('1789,37,47,1889')) == 1202161486)
buses = parse('23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,733,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37')
print(buses)
print(process(buses))