from collections import namedtuple
import re

PasswordPolicy = namedtuple('PasswordPolicy', 'lower upper char')
PasswordWithPolicy = namedtuple('PasswordWithPolicy', 'password password_policy')

def read():
    passwords_with_policies = []

    with open('input') as input:
        for line in input: 
            parts = re.split(':? ', line.strip())
        
            occ = re.split('\-', parts[0])
            char = parts[1]
            password = parts[2]

            password_policy = PasswordPolicy(
                int(occ[0]),
                int(occ[1]),
                char
            )

            passwords_with_policies.append(
                PasswordWithPolicy(
                    password,
                    password_policy
                )
            )
    
    return passwords_with_policies

def process(passwords_with_policies, is_valid_password):
    valid_passwords = 0

    for password_with_policy in passwords_with_policies:
        if is_valid_password(password_with_policy.password, password_with_policy.password_policy):
            valid_passwords += 1
    
    return valid_passwords

def is_valid_password_part1(password, password_policy):
    matches = re.findall(password_policy.char, password)

    return len(matches) >= password_policy.lower and len(matches) <= password_policy.upper

def is_valid_password_part2(password, password_policy):
    return (password[password_policy.lower - 1] == password_policy.char) ^ (password[password_policy.upper -1] == password_policy.char)

def main(is_valid_password):
    input_list = read()
    return process(input_list, is_valid_password)

if __name__ == '__main__':
    print(f'Part 1: {main(is_valid_password_part1)}')
    print(f'Part 2: {main(is_valid_password_part2)}')