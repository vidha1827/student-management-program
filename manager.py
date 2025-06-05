<<<<<<< HEAD
#Contains the StudentManager class with methods

from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name , age , grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print("Student successfully added.")

    def display_student(self):
        if not self.students:
            print("No student found.")
        else:
            for i, student in enumerate(self.students, start=1):
                print(f"{i}. ", end="")
                student.display()

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def delete_student(self, name):
        student = self.search_student(name)
        if student:
            self.students.remove(student)
            print("Student deleted.")
        else:
            print("Student not found.")


=======
#Contains the StudentManager class with methods

from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name , age , grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print("Student successfully added.")

    def display_student(self):
        if not self.students:
            print("No student found.")
        else:
            for i, student in enumerate(self.students, start=1):
                print(f"{i}. ", end="")
                student.display()

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def delete_student(self, name):
        student = self.search_student(name)
        if student:
            self.students.remove(student)
            print("Student deleted.")
        else:
            print("Student not found.")


>>>>>>> 04bdb98a03fa917bab53d0d50edd1b1e6f1927df
