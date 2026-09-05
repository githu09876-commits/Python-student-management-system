students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 40)

    for i, student in enumerate(students, start=1):
        print(
            f"{i}. Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Course: {student['course']}"
        )


def update_student():
    if not students:
        print("No students found.")
        return

    view_students()

    try:
        number = int(input("Enter student number to update: "))

        if 1 <= number <= len(students):
            student = students[number - 1]

            student["name"] = input(
                f"Enter new name ({student['name']}): "
            )
            student["age"] = input(
                f"Enter new age ({student['age']}): "
            )
            student["course"] = input(
                f"Enter new course ({student['course']}): "
            )

            print("Student updated successfully!")
        else:
            print("Invalid student number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_student():
    if not students:
        print("No students found.")
        return

    view_students()

    try:
        number = int(input("Enter student number to delete: "))

        if 1 <= number <= len(students):
            deleted_student = students.pop(number - 1)
            print(
                f"Student '{deleted_student['name']}' "
                "deleted successfully!"
            )
        else:
            print("Invalid student number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()