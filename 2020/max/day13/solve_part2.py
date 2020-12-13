from datetime import datetime

class Bus:
    def __init__(self, k, m):
        self.k = k
        self.m = m
    
    def is_valid(self, t):
        return t % self.k - self.m == 0

    def merge(self, other):
        x = 0
        matches = []
        while True:
            t = self.k * x + self.m

            if other.is_valid(t):
                matches.append(t)

                if len(matches) > 1:
                    bus = Bus(matches[1] - matches[0], matches[0])
                    return bus
            
            x += 1

    def first_t(self):
        return self.k - self.m

    def __str__(self):
        return f'Bus with period {self.k} and offset {self.m}'

def parse(input):
    buses = []
    for i, c in enumerate(input.split(',')):
        if c != 'x':
            buses.append(Bus(int(c), i))
    return buses

def process(buses):
    i = 1
    new_bus = None
    while i <= (len(buses) - 1):
        old_bus = buses[i-1] if new_bus is None else new_bus
        new_bus = old_bus.merge(buses[i])
        print(datetime.now().strftime("%H:%M:%S"), i, new_bus)
        i += 1
    return new_bus.first_t()

print('Performing sanity check with known data to start with...')
if process(parse('1789,37,47,1889')) != 1202161486:
    raise Exception('Precondition failed!')
print('')
print('Sanity check done. Starting the real crunch now.')

buses = parse('23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,733,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37')
print(process(buses))