#Main file that runs the program
from manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\nOptions : Add / display / search / delete / exit")
        choice = input("Enter choice:  ").lower()

        if choice == "add":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            manager.add_student(name,age,grade)

        elif choice == "display":
            manager.display_student()

        elif choice == "search":
            name = input("Enter name to search: ")
            student = manager.search_student(name)
            if student:
                student.display()
            else:
                print("Student not found. ")

        elif choice == "delete":
            name = input("Enter name to delete: ")
            manager.delete_student(name)

        elif choice == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. ")

if __name__ == "__main__":
    main()





