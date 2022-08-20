goods = {
    "name": "Pepsi", 
    "cost": 12.3
}

print(goods["name"])
print(goods["cost"])

goods["sale"] = 2

print(goods)


for key, value in goods.items():
    print(key, value) 

for value in goods.values():
    print(value)

for key in goods.keys():
    print(key)


goods = [ {}, {}, {}, {}]