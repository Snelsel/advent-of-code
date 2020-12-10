import itertools
import sys

PREAMBLE_LENGTH = 25
PART_1_ANSWER = None

def is_valid(num, prevs):
    for combo in itertools.combinations(prevs, 2):
        if sum(combo) == num:
            # print(f'{num} is valid!')
            return True
    return False

prevs = []
all_nums = []
i = 0
with open('input') as input:
    for line in input:
        num = int(line.strip())

        if i >= PREAMBLE_LENGTH:
            if not is_valid(num, prevs):
                print(f'{num} is invalid')
                PART_1_ANSWER = num
                
        i += 1
        prevs.append(num)
        all_nums.append(num)

        if len(prevs) > PREAMBLE_LENGTH:
            prevs.pop(0)

for i, num in enumerate(all_nums):
    for j, num in enumerate(all_nums):
        sequence = all_nums[i:j]
        if sum(sequence) == PART_1_ANSWER:
            sequence.sort()
            print(f'Found a sequence that adds to {PART_1_ANSWER}! From position {i} ({all_nums[i]}) to {j} ({all_nums[j]}) => result: {sequence[0] + sequence[len(sequence)-1]}')