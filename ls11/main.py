from typing import List


class Student:

    def __init__(self, name, surname, form):
        self.name = name
        self.surname = surname
        self.form =  form
    
    

student1 = Student("Svait", "Skorobohatov", 7)
student2 = Student("Artem", "Skripkin", 4)
student3 = Student("Rita", "Volkova", 3)
student4 = Student("Kostya", "Mazur", 5)

students = [student1, student2, student3, student4]

