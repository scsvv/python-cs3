"""
Диапозон 1000 -> 3000 

"""
year = int(input("Enter year: "))
str_build = ""

if year < 1000 or year > 3000:
    exit()

_t4 = year // 1000
year -= 1000 * _t4    
str_build = "M" *_t4

# C CC CCC CD D DC DCC DCCC CM 

_t3 = year // 100
year -= 100 * _t3

if _t3 < 4: 
    str_build += "C" *_t3
elif _t3 == 4: 
    str_build += "CD"
elif _t3 == 5:
    str_build += "D"
elif _t3 < 9:
    str_build += "D" + "C"*(_t3-5)
elif _t3 == 9:
    str_build += "CM"



_t2 = year // 10
year -= 10 * _t2

if _t2 < 4: 
    str_build += "X" *_t2
elif _t2 == 4: 
    str_build += "XL"
elif _t2 == 5:
    str_build += "L"
elif _t2 < 9:
    str_build += "L" + "X"*(_t2-5)
elif _t2 == 9:
    str_build += "XC"


if year < 4: 
    str_build += "I" *_t2
elif year == 4: 
    str_build += "IV"
elif year == 5:
    str_build += "V"
elif year < 9:
    str_build += "V" + "I"*(_t2-5)
elif year == 9:
    str_build += "IX"



print(str_build)
