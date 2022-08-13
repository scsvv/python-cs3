sum = 0
for i in range(1, 1001):
    if (i%3 == 0) and (i%5 == 0) and (i%7 == 0):
        sum += i 
print(sum)

sum = 0
j = 1;

while True: 
    if j == 1001:
        break
    if (j%3 == 0) and (j%5 == 0) and (j%7 == 0):
        sum += j
    j+=1
print(sum)