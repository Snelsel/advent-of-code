import sys

entries = []

with open("input") as input:
    for line in input: 
        entries.append(int(line.strip()))

entries.sort()

for entry1 in entries:
    for entry2 in entries:
        if entry1 + entry2 > 2020:
            break
        for entry3 in entries:
            sum = entry1 + entry2 + entry3
            print(entry1, entry2, entry3, sum)
            if sum == 2020:
                print("Fond them!")
                print(entry1*entry2*entry3)
                sys.exit()
            if sum > 2020:
                break

