import re
class Instruction:
    def __init__(self, str):
        if re.match('^mask', str):
            self.operation = 'mask'
            self.value = re.findall('^mask = ([01X]+)$', str)[0]
        else:
            self.operation = 'mem'
            (address, value) = re.findall('^mem\[([0-9]+)\] = ([0-9]+)$', str)[0]
            self.address = int(address)
            self.value = int(value)

class State:
    def __init__(self):
        self.mask = None
        self.memory = {}
    
    def apply(self, instruction):
        if instruction.operation == 'mask':
            self.mask = instruction.value
        else:
            val = bin(instruction.value)[2:].rjust(36, '0')
            i = 1
            new_val = []
            for i, m in enumerate(self.mask):
                new_val.append(m if m != 'X' else val[i])
            new_val = ''.join(new_val)
            v = int(new_val, 2)
            self.memory[instruction.address] = v
    
    def apply_2(self, instruction):
        if instruction.operation == 'mask':
            self.mask = instruction.value
        else:
            addresses = self.find_addresses(instruction.address, self.mask)
            
            for address in addresses:
                self.memory[int(address, 2)] = instruction.value

    @staticmethod
    def find_addresses(address, mask):
        address = bin(address)[2:].rjust(36, '0')
        addresses = ['']
        for i, m in enumerate(mask):
            if m == '0':
                for j, a in enumerate(addresses):
                    addresses[j] = a + address[i]
            elif m == '1':
                for j, a in enumerate(addresses):
                    addresses[j] = a + '1'
            elif m == 'X':
                duplicated_addresses = []
                for a in addresses:
                    duplicated_addresses.extend([a + '0', a + '1'])
                addresses = duplicated_addresses
        return addresses

    def mem_sum(self):
        sum = 0
        for v in self.memory.values():
            sum += v
        return sum
    

def parse():
    instructions = []
    with open('input') as input:
        for line in input:
            instructions.append(Instruction(line.strip()))
    return instructions

def process(instructions):
    state = State()
    state_2 = State()
    for instruction in instructions:
        state.apply(instruction)
        state_2.apply_2(instruction)
    return (state, state_2)

instructions = parse()
(state, state_2) = process(instructions)
print(state.mem_sum(), state_2.mem_sum())