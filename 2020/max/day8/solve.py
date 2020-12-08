import re
import sys

def parse():
    instructions = []
    with open('input') as input:
        for line in input:
            line = line.strip()
            instructions.append(parse_line(line))
    return instructions

def parse_line(line):
    (instr, qty) = re.findall('^(nop|acc|jmp) \+?(-?\d+)$', line)[0]
    return (instr, int(qty))

def process(instructions, swap_instruction_at_pos = None, debug = False):
    pos_history = []
    pos = 0
    acc = 0
    while pos not in pos_history:
        pos_history.append(pos)

        if pos >= len(instructions):
            return acc

        (instr, qty) = instructions[pos]

        if swap_instruction_at_pos == pos:
            if debug:
                print(f'Attempting to swap instruction at {pos}')
            if instr == 'jmp':
                instr = 'nop'
            elif instr == 'nop':
                instr = 'jmp'

        if debug:
            print(f'Processing at {pos}. Current acc: {acc}')
            print(f'  Will {instr} {qty}')

        if instr == 'nop':
            pos += 1
        elif instr == 'acc':
            pos += 1
            acc += qty
        elif instr == 'jmp':
            pos += qty
        
        if debug:
            print(f'  Resulting pos:{pos}, acc: {acc}')

    raise Exception(f'Infinite loop detected at {pos} with acc: {acc}!')

def process_part2(instructions):
    i = 0
    for num, instruction in enumerate(instructions):
        try:
            acc = process(instructions, num)
            print(f'Got acc: {acc} when swapping at {num}!')
        except:
            a = 0

instructions = parse()

try:
    process(instructions)
except:
    print(sys.exc_info()[1])

process_part2(instructions)