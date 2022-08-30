def for_numbers(massive): 
    sum = 0
    if len(massive) == 1:
        return massive[0]  
    for item in massive: 
        sum += item
    
    return sum


def while_numbers(massive): 
    sum = 0
    if len(massive) == 1:
        return massive[0]
    while len(massive) != 0: 
        sum += massive.pop()

    return sum

def recurs_numbers(massive): 
    if len(massive) == 1:
        return massive[0]
    return massive.pop() + recurs_numbers(massive)

# 
list_of_number = [1, 2, 3, 4]

print(for_numbers(list_of_number))
print(while_numbers(list_of_number))
list_of_number = [1, 2, 3, 4]
print(recurs_numbers(list_of_number))