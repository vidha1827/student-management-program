#Contains the student class


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}, Grade : {self.grade}")
