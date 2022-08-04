from random import randint 

x = randint(1, 10)
print(x)

login = "scsvv"
user = "scsvv"

if login == user: 
    print("Welcome")
else:
    print("Go Back")

tempature = 10
# so cold / cold / normal / warm / hot / so hot  
if tempature < -10:
    print("So cold")
elif tempature < 0:
     print("Cold")
elif tempature < 10:
    print("Normal")
elif tempature < 20:
    print("Warm")
elif tempature < 30:
    print("Hot")
elif tempature >= 30:
    print("SO HOT")