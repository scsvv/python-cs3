class Student: 

    def __init__(self, _name, _form, _age):
        self.name = _name
        self.form = _form
        self.age = _age
        self.mark = {}
    
    def marks_add(self, subject, mark):
        self.mark[subject] = mark



student = Student("Egor", 11, 17)

print(student.name)

student.marks_add("Geogrphy", [10, 10, 11, 10])
student.marks_add("Math", [10, 9, 11, 10])
print(student.mark)
        