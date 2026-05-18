students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    student = {
        "name": name,
        "roll": roll
    }

    students.append(student)

    print("Student added successfully")


def view_students():
    if len(students) == 0:
        print("No students found")

    else:
        print("\nStudent List")

        for student in students:
            print("Name:", student["name"])
            print("Roll No:", student["roll"])


def search_student():
    roll = input("Enter roll number to search: ")

    found = False

    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print("Name:", student["name"])
            found = True

    if found == False:
        print("Student not found")


def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted")
            return

    print("Student not found")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")