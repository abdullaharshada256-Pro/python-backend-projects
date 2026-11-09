import json
import os

if os.path.exists("students.json"):
    with open("students.json", "r") as file:
        students = json.load(file)
else:
    students = []
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    student = {
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!")

def show_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("----------------")

def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            return

    print("Student not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")