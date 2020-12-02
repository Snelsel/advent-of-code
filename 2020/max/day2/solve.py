import re

validPasswords = 0

class PasswordPolicy:
    def __init__(self, lower, upper, char):
        self.lower = lower
        self.upper = upper
        self.char = char
    
    def get_char(self):
        return self.char
    
    def get_lower(self):
        return self.lower
    
    def get_upper(self):
        return self.upper

def read():
    input_list = []

    with open('input') as input:
        for line in input: 
            parts = re.split(':? ', line.strip())
        
            occ = re.split('\-', parts[0])
            char = parts[1]
            password = parts[2]

            passwordPolicy = PasswordPolicy(
                int(occ[0]),
                int(occ[1]),
                char
            )

            input_list.append(
                [password, passwordPolicy]
            )
    
    return input_list

def process(input_list):
    valid_passwords = 0

    for parsed_line in input_list:
        matches = re.findall(parsed_line[1].get_char(), parsed_line[0])

        if len(matches) >= parsed_line[1].get_lower() and len(matches) <= parsed_line[1].get_upper():
            valid_passwords += 1
    
    return valid_passwords

def main():
    input_list = read()
    return process(input_list)

if __name__ == '__main__':
    print(f'Part 1: {main()}')