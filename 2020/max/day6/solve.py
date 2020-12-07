
def parse():
    all_answers = []

    group_answers = []

    with open('input') as input:
        for line in input:
            line = line.strip()
            
            if len(line) == 0:
                all_answers.append(group_answers)
                group_answers = []
            else:
                group_answers.append(list(line))
        all_answers.append(group_answers)
    return all_answers

def count_group_part1(group_answers):
    answers = list_answers(group_answers)
    return len(list(set(answers)))

def count_group_part2(group_answers):
    answers = list_answers(group_answers)
    sum = 0
    for a in group_answers[0]:
        if answers.count(a) == len(group_answers):
            sum+=1
    return sum

def list_answers(group_answers):
    answers = []
    for user_answers in group_answers:
        for a in user_answers:
            answers.append(a)
    return answers

def process(all_answers, count_group):
    sum = 0
    for group_answers in all_answers:
        sum += count_group(group_answers)
    return sum

all_answers = parse()
print(process(all_answers, count_group_part1))
print(process(all_answers, count_group_part2))