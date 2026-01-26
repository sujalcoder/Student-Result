from flask import Blueprint, render_template, request
from database import students, marks

students_bp = Blueprint("student", __name__)

# STUDENT LOGIN ROUTE
@students_bp.route('/', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        student_check=students.find_one({'roll_no': roll_no})
        # TEMP TEST LOGIN
        if student_check:
            return render_template('result.html')
        else:
            return render_template(
                'index.html',
                error='Please enter a valid Roll Number'
            )

    return render_template('index.html')

# STUDENT RESULT ROUTE
@students_bp.route('/result', methods=['GET', 'POST'])  
def student_result():
    all_marks = list(marks.find())
    total=
    return render_template('result.html', marks=all_marks)