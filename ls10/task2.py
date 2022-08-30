
def combine_lists(list_a, list_b):
    
    len_list = len(list_b) + len(list_a)
    comb_list = list_a.copy()
    i = 1
    j = 0
    while len(comb_list) != len_list:
        comb_list.insert(i, list_b[j])

        i += 2
        j += 1
    
    return comb_list

a = [1, 2, 3]
b = [11, 22, 33]

c = combine_lists(a, b)
print(c)