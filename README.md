#  Student Performance Tracker

A Flask-based web application that allows users to manage student records, assign subject-wise grades, and view academic performance reports. Built for simplicity, functionality, and real-world deployment practice.



##  Live Demo
🔗 [Access the app online](https://student-tracker-h8nh.onrender.com)

---
## ✨ Features

- ➕ Add new students (name, ID)
- ✏️ Assign grades across subjects
- 📋 View full performance reports in table format
- 🧮 Identify top performer by average score
- 🗃️ View individual subject performance
- ❌ Delete student records if needed
- 📥 Download performance data as a CSV file
- 👀 Browse list of all enrolled students

---

##  How to Use

### 1. Add Students
Navigate to “Add Student” → input name and ID → submit.

### 2. Assign Grades
Go to “Assign Grades” → choose student → add subjects and marks.

### 3. View Reports
Explore performance table under “Reports” tab:
- Sort by top performer
- View specific subject scores
- Download CSV summary

### 4. Delete Students
If a record is incorrect or outdated:
- Go to “View Students”
- Select and delete the entry

---

## ⚙️ Tech Stack

- Python 3.x
- Flask
- SQLite
- Gunicorn
- Hosted on Render

---

## 📦 Deployment Files

- `requirements.txt`: contains dependencies
  ```text
  Flask
  gunicorn

### project structure
student-performance-tracker/
├── app.py                  # Main Flask script
├── database.db             # SQLite database
├── templates/              # HTML views
│   ├── add_student.html
│   ├── assign_grades.html
│   ├── view_reports.html
│   ├── view_students.html
│   └── download.html
├── static/                 # Optional CSS or assets
├── requirements.txt        # Packages needed
├── Procfile                # Deployment config

A hands-on learning project showcasing full-stack development and deployment.
