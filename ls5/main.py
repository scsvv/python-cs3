"""
sum = 0
N = int(input("N: "))

for i in range(N+1):
    sum += 1 + i/10
    
print(sum)

sum = 0

for i in range(N+1):
    if i == 0:
        sum += 1
        continue

    sum += 1 / i

print(sum)

"""
from turtle import right


password = "scsvv"
user_input = '' 
trying = 0
right_password = False

while trying < 4 and not(right_password):
    
    user_input = input('>>>')
    if (password == user_input):
        right_password = True
        print('U in system')
    else: 
        trying += 1


 
