import itertools
import math

def read():
    input_list = []
    with open('input') as f:
        for line in f:
            input_list.append(int(line))
    return input_list


def process(input_list, combo_no):
    for combo in itertools.combinations(input_list, combo_no):
        if sum(combo) == 2020:
            return math.prod(combo)


def main(combo_no):
    input_list = read()
    return process(input_list, combo_no)


if __name__ == '__main__':
    print(f'Combo 2: {main(combo_no=2)}')
    print(f'Combo 3: {main(combo_no=3)}')