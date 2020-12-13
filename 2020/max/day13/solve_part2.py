from operator import itemgetter

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
            # if x > 1000000000:
            #     raise Exception('Possible infinite loop detected')
            
            t = self.k * x + self.m

            # if not self.is_valid(t):
            #     raise Exception('Dont try a t thats not valid for yourself...')

            if other.is_valid(t):
                matches.append(t)

                if len(matches) > 2:
                    k = matches[1] - matches[0]
                    m = matches[0]
                    bus = Bus(k, m)
                    # for match in matches:
                    #     if not bus.is_valid(t):
                    #         print(matches, bus)
                    #         raise Exception('Failed merge!')
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
    print(len(buses) - 1)
    while i <= (len(buses) - 1):
        old_bus = buses[i-1] if new_bus is None else new_bus
        new_bus = old_bus.merge(buses[i])
        print(i, new_bus)
        i += 1
    return new_bus.first_t()

buses = parse('23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,733,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37')
print(process(buses))