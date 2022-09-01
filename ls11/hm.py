def check(point_a, point_b):
    if(point_a[0] < 1 or point_a[0] > 8): 
        return False    
    if (abs(point_a[0] - point_b[0]) == 2 and abs(point_a[1] - point_b[1]) == 1) or abs(point_a[1] - point_b[1]) == 2 and abs(point_a[0] - point_b[0]) == 1:
        return True
    return False

print(check((1,1), (2, 3)))
