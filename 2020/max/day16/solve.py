import re
import math

class Ticket:
    def __init__(self, str):
        self.list = []
        for c in str.split(','):
            self.list.append(int(c))
    
    def __str__(self):
        ret = []
        for c in self.list:
            ret.append(c.__str__())
        return ','.join(ret)

class Rule:
    def __init__(self, str):
        self.str = str
        (self.name, min1, max1, min2, max2) = re.findall('^([^:]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', str)[0]
        self.min1 = int(min1)
        self.max1 = int(max1)
        self.min2 = int(min2)
        self.max2 = int(max2)
    
    def __str__(self):
        return self.str
    
    def is_invalid(self, value):
        if value >= self.min1 and value <= self.max1:
            return False
        if value >= self.min2 and value <= self.max2:
            return False
        return True
        
class RuleSet:
    def __init__(self):
        self.rules = []
    
    def append(self, rule):
        self.rules.append(rule)
    
    def is_invalid(self, value):
        for rule in self.rules:
            if not rule.is_invalid(value):
                return False
        return True

def parse():
    state = 'rules'
    ruleset = RuleSet()
    your_ticket = None
    nearby_tickets = [] 
    with open('input') as input:
        for line in input:
            line = line.strip()
            
            if len(line) == 0:
                continue
            elif line == 'your ticket:':
                state = 'your_ticket'
                continue
            elif line == 'nearby tickets:':
                state = 'nearby_tickets'
                continue
            
            if state == 'rules':
                ruleset.append(Rule(line))
            elif state == 'your_ticket':
                your_ticket = Ticket(line)
            elif state == 'nearby_tickets':
                nearby_tickets.append(Ticket(line))
    return (ruleset, your_ticket, nearby_tickets)

def count_and_discard(ruleset, tickets):
    sum_invalid = 0
    valid_tickets = []
    for i, ticket in enumerate(tickets):
        is_invalid = False
        for j, value in enumerate(ticket.list):
            if ruleset.is_invalid(value):
                sum_invalid += value
                is_invalid = True
        if is_invalid == False:
            valid_tickets.append(ticket)
    return (valid_tickets, sum_invalid)

def find_valid_rules_by_position(ruleset, tickets):
    valid_rules_by_position = {}

    for i, _ in enumerate(tickets[0].list):
        valid_rules_by_position[i] = []
        for rule in ruleset.rules:
            rule_is_correct = True
            for ticket in tickets:
                if rule.is_invalid(ticket.list[i]):
                    rule_is_correct = False
                    #print(f'  Determined that rule {rule.name} is not correct for position {i} since the value {ticket.list[i]} is invalid')
            if rule_is_correct:
                #print(f'Determined that rule {rule.name} is correct for position {i}')
                valid_rules_by_position[i].append(rule.name)
        if len(valid_rules_by_position[i]) == 0:
            raise Exception(f'No rule was valid for position {i}. Is that really correct?')
    
    return valid_rules_by_position

    def reduce_valid_rules_by_position(rules_by_position):
        while True:
            delete_performed = False
            found_single_rule = False
            for i, rules in rules_by_position.items():
                if len(rules) == 1:
                    found_single_rule = True
                    for j, rules_to_delete_from in rules_by_position.items():
                        if j != i and rules[0] in rules_to_delete_from:
                            rules_to_delete_from.remove(rules[0])
                            delete_performed = True
            if found_single_rule == False:
                raise Exception('Did not find a single rule, cannot continue')

            if delete_performed == False:
                return rules_by_position

def reduce_valid_rules_by_position(rules_by_position):
    while True:
        delete_performed = False
        found_single_rule = False
        for i, rules in rules_by_position.items():
            if len(rules) == 1:
                found_single_rule = True
                for j, rules_to_delete_from in rules_by_position.items():
                    if j != i and rules[0] in rules_to_delete_from:
                        rules_to_delete_from.remove(rules[0])
                        delete_performed = True
        if found_single_rule == False:
            raise Exception('Did not find a single rule, cannot continue')

        if delete_performed == False:
            return rules_by_position

def process_part1(ruleset, nearby_tickets):
    (_, sum_invalid) = count_and_discard(ruleset, nearby_tickets)
    return sum_invalid

def process_part2(ruleset, your_ticket, nearby_tickets):
    (valid_tickets, _) = count_and_discard(ruleset, nearby_tickets)
    
    valid_rules_by_position = find_valid_rules_by_position(ruleset, valid_tickets)
    
    reduced_valid_rules_by_position = reduce_valid_rules_by_position(valid_rules_by_position)

    for i, v in reduced_valid_rules_by_position.items():
        print(i, v)

    departure_values = []
    for i, v in enumerate(your_ticket.list):
        rules = reduced_valid_rules_by_position[i]
        if re.match('^departure', rules[0]):
            departure_values.append(v)
    
    return departure_values

(ruleset, your_ticket, nearby_tickets) = parse()

print('Rules:')
for rule in ruleset.rules:
    print(f'  {rule}')

print('Your ticket:')
print(f'  {your_ticket}')

# print('Nearby tickets:')
# for ticket in nearby_tickets:
#     print(f'  {ticket}')

print('Sum of invalid: ', process_part1(ruleset, nearby_tickets))
departure_values = process_part2(ruleset, your_ticket, nearby_tickets)
print(departure_values)
print('Product of departure values: ', math.prod(departure_values))
