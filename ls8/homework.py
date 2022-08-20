# Создайте список из случайных чисел. 
# Найдите количество различных элементов в нем.
from random import randint

N = 10
list_of_number = []
list_of_unique_numbers = []

for i in range(0, N):
    list_of_number.append(randint(0, 10))


print(list_of_number)


for number in list_of_number: 
    
    if list_of_number.count(number) == 1:
         list_of_unique_numbers.append(number)


print(list_of_unique_numbers)

for number in list_of_number: 
    
    if list_of_number.count(number) != 1:
        k = list_of_number.count(number)
        for j in range(0, k): 
            list_of_number.remove(number)
print(list_of_number)
