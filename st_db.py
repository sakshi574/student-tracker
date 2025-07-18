# st_db.py

import sqlite3
import csv

DB_PATH = "students.db"  # Easily change database location if needed

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create students and grades tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_number TEXT PRIMARY KEY,
        name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        roll_number TEXT,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY (roll_number) REFERENCES students(roll_number)
    )
""")
conn.commit()
import sqlite3

DB_PATH = "students.db"  # Easily change database location if needed

# Add a student
def add_student(name, roll_number):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
        conn.commit()
        conn.close()
        print("✅ Student added successfully.")
    except Exception as e:
        print("❌ Error adding student:", e)

# Add a grade
def add_grade(roll_number, subject, grade):
    try:
        if 0 <= grade <= 100:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
            conn.commit()
            conn.close()
            print("✅ Grade saved to database.")
        else:
            print("⚠️ Grade must be between 0 and 100.")
    except Exception as e:
        print("❌ Error adding grade:", e)

# View student details (returns string for web display)
def view_student(roll_number):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM students WHERE roll_number = ?", (roll_number,))
        student = cursor.fetchone()
        output = ""

        if student:
            output += f"Name: {student[0]}\nRoll No: {roll_number}\n"
            cursor.execute("SELECT subject, grade FROM grades WHERE roll_number = ?", (roll_number,))
            grades = cursor.fetchall()
            total = 0
            for subject, grade in grades:
                output += f"{subject}: {grade}\n"
                total += grade
            if grades:
                average = total / len(grades)
                output += f"Average Grade: {average:.2f}\n"
        else:
            output += "Student not found."

        conn.close()
        return output
    except Exception as e:
        return f"❌ Error fetching student: {e}"
def get_top_students(limit=5):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT students.roll_number, students.name,
                   AVG(grades.grade) as average
            FROM students
            JOIN grades ON students.roll_number = grades.roll_number
            GROUP BY students.roll_number
            ORDER BY average DESC
            LIMIT ?
        """, (limit,))
        
        toppers = cursor.fetchall()
        conn.close()
        return toppers
    except Exception as e:
        return []
def delete_student(roll_number):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        # Delete grades first (due to foreign key)
        cursor.execute("DELETE FROM grades WHERE roll_number = ?", (roll_number,))
        cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll_number,))
        conn.commit()
        conn.close()
        print("🗑️ Student and grades deleted.")
    except Exception as e:
        print("❌ Error deleting student:", e)


def export_grades_csv(filename="grades_export.csv"):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT students.roll_number, students.name, grades.subject, grades.grade
            FROM students
            JOIN grades ON students.roll_number = grades.roll_number
        """)

        rows = cursor.fetchall()
        conn.close()

        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Subject", "Grade"])
            writer.writerows(rows)

        print(f"📁 Exported to {filename}")
        return True
    except Exception as e:
        print("❌ Error exporting:", e)
        return False
    
def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT roll_number, name FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def get_subject_averages():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subject, AVG(grade) 
        FROM grades 
        GROUP BY subject
    """)
    data = cursor.fetchall()
    conn.close()
    return data
# Initialize tables (can be called at app startup if needed)
def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_number TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            roll_number TEXT,
            subject TEXT,
            grade INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students(roll_number)
        )
    """)
    conn.commit()
    conn.close()

# Add a student
# def add_student(name, roll_number):
#     try:
#         cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
#         conn.commit()
#         print("✅ Student added successfully.")
#     except Exception as e:
#         print("❌ Error adding student:", e)

# # Add a grade
# def add_grade(roll_number, subject, grade):
#     try:
#         if 0 <= grade <= 100:
#             cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
#             conn.commit()
#             print("✅ Grade saved to database.")
#         else:
#             print("⚠️ Grade must be between 0 and 100.")
#     except Exception as e:
#         print("❌ Error adding grade:", e)

# # View student details
# def view_student(roll_number):
#     cursor.execute("SELECT name FROM students WHERE roll_number = ?", (roll_number,))
#     student = cursor.fetchone()
#     if student:
#         print(f"\n👤 Name: {student[0]}")
#         print(f"🆔 Roll Number: {roll_number}")
#         cursor.execute("SELECT subject, grade FROM grades WHERE roll_number = ?", (roll_number,))
#         grades = cursor.fetchall()
#         total = 0
#         for subject, grade in grades:
#             print(f"📘 {subject}: {grade}")
#             total += grade
#         if grades:
#             average = total / len(grades)
#             print(f"📊 Average Grade: {average:.2f}")
#     else:
#         print("🚫 Student not found.")

# # View all records (optional)
# def show_all_records():
#     print("\n📚 All Students:")
#     cursor.execute("SELECT * FROM students")
#     for row in cursor.fetchall():
#         print(row)
    
#     print("\n📘 All Grades:")
#     cursor.execute("SELECT * FROM grades")
#     for row in cursor.fetchall():
#         print(row)

# # Close connection
# def close_connection():
#     conn.close()