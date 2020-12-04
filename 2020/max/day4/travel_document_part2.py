import re

class TravelDocument:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
    
    def byr_is_valid(self):
        if self.byr is not None and len(self.byr) == 4 and self.byr.isdigit() and int(self.byr) >= 1920 and int(self.byr) <= 2002:
            print(f'byr valid: {self.byr}')
            return True
        else:
            print(f'byr invalid: {self.byr}')

    def iyr_is_valid(self):
        if self.iyr is not None and len(self.iyr) == 4 and self.iyr.isdigit() and int(self.iyr) >= 2010 and int(self.iyr) <= 2020:
            print(f'iyr valid: {self.iyr}')
            return True
        else:
            print(f'iyr invalid!: {self.iyr}')

    def eyr_is_valid(self):
        if self.eyr is not None and len(self.eyr) == 4 and self.eyr.isdigit() and int(self.eyr) >= 2020 and int(self.eyr) <= 2030:
            print(f'eyr valid: {self.eyr}')
            return True
        else:
            print(f'eyr invalid: {self.eyr}')

    def hgt_is_valid(self):
        if self.hgt is None or not re.match('([0-9]+)(in|cm)', self.hgt):
            print(f'hgt invalid: {self.hgt}')
            return False
        (num, uom) = re.findall('([0-9]+)(in|cm)', self.hgt)[0]

        if num is None or uom is None:
            print(f'hgt invalid: {self.hgt}')
            return False
        
        num = int(num)

        if uom == 'cm':
            if num >= 150 and num <= 193:
                print(f'hgt valid: {self.hgt}')
                return True
            else:
                print(f'hgt invalid: {self.hgt}')
        else:
            if num >= 59 and num <= 76:
                print(f'hgt valid: {self.hgt}')
                return True
            else:
                print(f'hgt invalid: {self.hgt}')
                return False

    def hcl_is_valid(self):
        if self.hcl is not None and re.match('#[0-9a-f]{6}', self.hcl):
            print(f'hcl valid: {self.hcl}')
            return True
        else:
            print(f'hcl invalid: {self.hcl}')

    def ecl_is_valid(self):
        if self.ecl is not None and re.match('(amb|blu|brn|gry|grn|hzl|oth)', self.ecl):
            print(f'ecl valid: {self.ecl}')
            return True
        else:
            print(f'ecl invalid: {self.ecl}')

    def pid_is_valid(self):
        if self.pid is not None and re.match('^[0-9]{9}$', self.pid):
            print(f'pid valid: {self.pid}')
            return True
        else:
            print(f'pid invalid: {self.pid}')

    def cid_is_valid(self):
        return True

    def is_valid(self):
        return (
            self.byr_is_valid() and
            self.iyr_is_valid() and
            self.eyr_is_valid() and
            self.hgt_is_valid() and
            self.hcl_is_valid() and
            self.ecl_is_valid() and
            self.pid_is_valid() and
            self.cid_is_valid())