import sys

entries = []

with open("input") as input:
    for line in input: 
        entries.append(int(line.strip()))

entries.sort()

for entry1 in entries:
    for entry2 in entries:
        sum = entry1 + entry2
        print(entry1, entry2, sum)
        if sum == 2020:
            print("Fond them!")
            print(entry1*entry2)
            sys.exit()
        if sum > 2020:
            print("Breaking out since sum is over 2020")
            break

