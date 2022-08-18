
"""
from random import randint

list_of_numbers = []

for i in range(20):
    list_of_numbers.append( randint(-100, 100) )

print(list_of_numbers) 

# TASK 1
max_value = list_of_numbers[0]
index_of_max_value = 0
i = 0
for number in list_of_numbers: 
    if number >= max_value: 
        max_value = number
        index_of_max_value = i
    i += 1

print(max_value, index_of_max_value)

# Task 2
max_count = 0
max_repeat_value = 0

for number in list_of_numbers: 
    if list_of_numbers.count(number) > max_count:
        max_count =  list_of_numbers.count(number)
        max_repeat_value = number

print(max_count, max_repeat_value)


first_value=list_of_numbers[0]
second_value=list_of_numbers[0]

for number in list_of_numbers: 
    
    if first_value < number: 
        
        if first_value == second_value:
            first_value = number
        elif first_value > second_value : 
            second_value = first_value
            first_value = number
        continue;

    if second_value < number: 
         second_value = number

print(first_value, second_value)

"""

a = 1
b = 1
c = 2
sum = 0
while True:
    c = a + b 
    print(c)
    if c > 4000000:
        break;
    
    if c % 2 == 0: 
        sum += c 

    a = b 
    b = c

print(sum)
