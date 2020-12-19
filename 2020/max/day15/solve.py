numbers = [0,6,1,7,2,19,20]
start_numbers = len(numbers)
i = start_numbers + 1

while i<= 30000000:
    prev = numbers[i-2]
    #print(f'i is {i}, and then prev is {prev}')
    if prev in numbers[start_numbers:]:
        prev_indices = [i for i, x in enumerate(numbers) if x==prev]
        speak = prev_indices[len(prev_indices) - 1] - prev_indices[len(prev_indices) - 2]
        #print(f'  This is not the first time {prev} is spoken. Indices of previous speaks are {prev_indices}.')
        #print(f'  The diff between the last to speaks is: {speak}')
        numbers.append(speak)
    else:
        #print(f'  This is the first time {prev} is spoken, so speak 0')
        numbers.append(0)
    i += 1
    #print(f'  Resulting numbers: {numbers}')

print(numbers[len(numbers) - 1])