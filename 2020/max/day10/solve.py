def parse():
    l = []
    with open('input') as input:
        for line in input:
            l.append(int(line.strip()))
    return l

def process_part1(l):
    g = [0, 0, 0, 1]
    l.sort()

    print(l)

    prev = 0

    for n in l:
        diff = n - prev
        g[diff] += 1
        prev = n

    return g[1] * g[3]

def process_part2(l):
    l.sort()

    combinations = 1
    offsets = [2, 3]
    i = len(l) - 1
    while i > 0:
        num = l[i]

        print(f'At position {i}, num is {num}')
        
        for offset in offsets:
            candidate = i - offset
            print(f'  testing candidate index {candidate}')
            if candidate >= 0:
                prev = l[candidate]

                diff = num - prev

                print(f'    value for candidate is {prev}, with a resulting diff of {diff}')
                
                if diff <= 3:
                    print(f'    the candidate was deemed valid, double the combinations!')
                    combinations *= 2
        
        i -= 1

    return combinations

l = parse()

print(process_part1(l))

print(process_part2(l))