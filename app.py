from flask import Flask, render_template, request, redirect
from st_db import add_student, add_grade, view_student , get_top_students ,delete_student ,get_all_students # Add this import
from flask import send_file
from st_db import export_grades_csv




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # this will be your home page

@app.route('/add_student', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        add_student(name, roll)
        return redirect('/')
    return render_template('add_student.html')

@app.route('/add_grade', methods=['GET', 'POST'])
def add_grade_route():
    if request.method == 'POST':
        roll = request.form['roll']
        subject = request.form['subject']
        grade = int(request.form['grade'])
        add_grade(roll, subject, grade)
        return redirect('/')
    return render_template('add_grade.html')

@app.route('/view_student', methods=['GET', 'POST'])
def view_student_route():
    student_info = None
    if request.method == 'POST':
        roll = request.form['roll']
        student_info = view_student(roll)
    return render_template('view_student.html', student=student_info)
@app.route('/toppers')
def toppers():
    top_students = get_top_students()
    return render_template('toppers.html', toppers=top_students)
@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student_route():
    message = ""
    if request.method == 'POST':
        roll = request.form['roll']
        delete_student(roll)
        message = f"🗑️ Deleted roll number {roll}"
    return render_template('delete_student.html', message=message)
@app.route('/export')
def export_route():
    success = export_grades_csv()
    if success:
        return send_file("grades_export.csv", as_attachment=True)
    return "❌ Export failed."


@app.route('/student/<roll>')
def student_profile(roll):
    student_info = view_student(roll)
    print(student_info)
    if student_info:
        return render_template('student_profile.html', student=student_info)
    else:
        return render_template('student_profile.html', student=None, roll=roll)
from st_db import get_subject_averages

@app.route('/subject_performance')
def subject_performance():
    data = get_subject_averages()
    labels = [item[0] for item in data]
    values = [item[1] for item in data]
    return render_template('subject_chart.html', labels=labels, values=values)



if __name__ == "__main__":
    app.run(debug=True)
    print("✅ Flask app is running. Visit http://127.0.0.1:5000/")