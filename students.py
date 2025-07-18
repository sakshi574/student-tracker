
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}  # empty dictionary to store subject:grade

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            print("Grade must be between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_number}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        print(f"Average: {self.average_grade():.2f}")
class StudentTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number in self.students:
            print("This roll number already exists!")
        else:
            self.students[roll_number] = Student(name, roll_number)

    def add_grades(self, roll_number, subject, grade):
        student = self.students.get(roll_number)
        if student:
            student.add_grade(subject, grade)
        else:
            print("Student not found.")

    def view_student_details(self, roll_number):
        student = self.students.get(roll_number)
        if student:
            student.display_info()
        else:
            print("Student not found.") 
# students.py
from st_db import add_student, add_grade, view_student, show_all_records, close_connection

def menu():
    while True:
        print("\n🎓 Student Performance Tracker")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Details")
        print("4. Show All Records")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("👤 Enter student name: ")
            roll = input("🆔 Enter roll number: ")
            add_student(name, roll)

        elif choice == "2":
            roll = input("🆔 Enter roll number: ")
            subject = input("📘 Enter subject: ")
            try:
                grade = int(input("📊 Enter grade (0–100): "))
                add_grade(roll, subject, grade)
            except ValueError:
                print("❌ Invalid grade input. Must be a number.")

        elif choice == "3":
            roll = input("🆔 Enter roll number to view: ")
            view_student(roll)

        elif choice == "4":
            show_all_records()

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            close_connection()
            break

        else:
            print("⚠️ Invalid choice. Try again!")

# Entry point
if __name__ == "__main__":
    menu()