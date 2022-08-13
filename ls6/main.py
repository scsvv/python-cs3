'''
list_of_names = ["Andrew", "Josh", "John", "Tyler", "Kriss"]

print(list_of_names[1])
print(len(list_of_names))

list_of_marks = [10, 9, 8, 12, 5, 12, 10]
eq_mark = 0
for mark in list_of_marks: 
    eq_mark += mark

print(eq_mark/len(list_of_marks))  
'''

users_cities = []

while True:
    letter = ''
    
    if len(users_cities) != 0: 
        word = users_cities[len(users_cities)-1]
        letter = word[len(word)-1]
    
    data = input(f"Enter cities on letter {letter} ")
    if data == "1":
        break    

    if data[len(data) - 1] == " ":
        print("U cheating")
        continue

    if  len(users_cities) != 0 and data[0] != letter: 
        print(f"Start of word must be on {letter}")
        continue;
    
    if users_cities.count(data.lower()) >= 1:
        print("This name used")
        continue

    users_cities.append(data.lower())

print(users_cities)