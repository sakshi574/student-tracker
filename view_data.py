import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# View all students
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print("STUDENTS:")
for s in students:
    print(s)

# View all grades
cursor.execute("SELECT * FROM grades")
grades = cursor.fetchall()
print("\nGRADES:")
for g in grades:
    print(g)

conn.close()