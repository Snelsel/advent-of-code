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

def process(input_list, is_valid_password):
    valid_passwords = 0

    for parsed_line in input_list:
        if is_valid_password(parsed_line[0], parsed_line[1]):
            valid_passwords += 1
    
    return valid_passwords

def is_valid_password_part1(password, passwordPolicy):
    matches = re.findall(passwordPolicy.get_char(), password)

    return len(matches) >= passwordPolicy.get_lower() and len(matches) <= passwordPolicy.get_upper()

def is_valid_password_part2(password, passwordPolicy):
    return (password[passwordPolicy.get_lower() - 1] == passwordPolicy.get_char()) ^ (password[passwordPolicy.get_upper() -1] == passwordPolicy.get_char())

def main(is_valid_password):
    input_list = read()
    return process(input_list, is_valid_password)

if __name__ == '__main__':
    print(f'Part 1: {main(is_valid_password_part1)}')
    print(f'Part 2: {main(is_valid_password_part2)}')