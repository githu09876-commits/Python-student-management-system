import json
import os

DATA_FILE = "students.json"


def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_students():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def update_student():
    if not students:
        print("No students found.")
        return

    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input(
                f"Enter new name ({student['name']}): "
            ) or student["name"]

            student["age"] = input(
                f"Enter new age ({student['age']}): "
            ) or student["age"]

            student["course"] = input(
                f"Enter new course ({student['course']}): "
            ) or student["course"]

            save_students()
            print("Student updated successfully!")
            return

    print("Student ID not found.")


def delete_student():
    if not students:
        print("No students found.")
        return

    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student ID not found.")


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
