from random import randint

counter_of_rigth_answer = 0

for i in range(5):
    x = randint(1, 100)
    y = randint(1, 100)
    z = x + y

    print(f'{x} + {y} = ?')

    users_answer = int(input(">>>"))

    if z == users_answer: 
        print("Correct")
        counter_of_rigth_answer += 1
    else:
        print("Incorrect")

if counter_of_rigth_answer >= 3:
    print(f"U win, your score is {counter_of_rigth_answer}")
else: 
    print("Loser")

