student_info = {
    "name": "Sviat", 
    "marks": {
        "math": [10, 8, 9, 11, 7], 
        "physic": [10, 9, 8, 7, 11], 
        "geometry": [8, 7, 9, 6, 10]
    }}
while True:
    str = input("Enter subject: ")

    if str == "exit": 
        break
    
    while True: 
        mark = input("Enter mark: ")
        if mark == "e":
            break
        mark = int(mark)        
        if mark < 0 or mark > 12:
            continue  

        if  list(student_info["marks"].keys()).count(str) == 0:
            student_info["marks"][str] = []

        student_info["marks"][str].append(mark)

print(student_info)

marks_total = []

for key in student_info["marks"].keys():
    sum = 0
    for items in student_info["marks"][key]:
        sum += items
    marks_total.append(sum / len(student_info["marks"][key]))

mark_summary = 0
for mark in marks_total: 
    mark_summary += mark

mark_summary = mark_summary / len(marks_total)  
print(mark_summary)
