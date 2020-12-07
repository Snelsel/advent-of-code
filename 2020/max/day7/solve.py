import re

def parse():
    ruleset = []
    with open('input') as input:
        for line in input:
            line = line.strip()
            ruleset.append(parse_line(line))
    return ruleset

def parse_line(line):
    rule = line.split('contain')

    container_raw = rule[0]

    contents_raw = rule[1].split(', ')

    container = clean(container_raw)

    contents = []
    for content_raw in contents_raw:
        content = clean(content_raw)
        if re.match('^(\d+) (.+)$', content):
            (quantity, color) = re.findall('^(\d+) (.+)$', content)[0]
            contents.append((int(quantity), color))
    
    return (container, contents)

def clean(raw_input):
    p = re.compile('(\.|bags|bag)')
    return p.sub('', raw_input).strip()

def contains(container, search, ruleset):
    for rule in ruleset:
        if rule[0] == container:
            for content in rule[1]:
                if content[1] == search:
                    return True
                if contains(content[1], search, ruleset):
                    return True
    return False

def count_children(container, ruleset):
    sum = 0
    for rule in ruleset:
        if rule[0] == container:
            for content in rule[1]:
                sum += content[0] * (1 + count_children(content[1], ruleset))
    return sum

def process_part1(search, ruleset):
    sum = 0
    for rule in ruleset:
        if contains(rule[0], search, ruleset):
            sum += 1
    return sum

def process_part2(search, ruleset):
    return count_children(search, ruleset)

ruleset = parse()
print(process_part1('shiny gold', ruleset))
print(process_part2('shiny gold', ruleset))