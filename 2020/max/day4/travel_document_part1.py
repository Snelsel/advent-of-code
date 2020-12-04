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
        return self.byr is not None

    def iyr_is_valid(self):
        return self.iyr is not None

    def eyr_is_valid(self):
        return self.eyr is not None

    def hgt_is_valid(self):
        return self.hgt is not None

    def hcl_is_valid(self):
        return self.hcl is not None

    def ecl_is_valid(self):
        return self.ecl is not None

    def pid_is_valid(self):
        return self.pid is not None

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