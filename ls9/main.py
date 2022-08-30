"""
def sum(a, b = 0): 
    return a + b

print(sum(9, 0))
print(sum(9, 12))
print(sum(10))
print(sum(9, 18))
"""

def max_value(list_of_smth): 
    max_v = list_of_smth[0]

    for item in list_of_smth:
        if item > max_v:
            max_v = item
    
    return max_v

print(max_value([10, 9, 8 , 100, -1]))
print(max_value([-10, -9, -8 , -100, -1]))