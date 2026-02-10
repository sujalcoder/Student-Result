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


@students_bp.route('/result', methods=['POST'])
def student_result():
    roll_no = request.form['roll_no'].strip()

    marks_data = marks.find_one({'roll_no': roll_no})
    print("ROLL NO FROM FORM:", roll_no)
    print("MARKS DATA FROM DB:", marks_data)

    if not marks_data:
        return render_template(
            'index.html',
            error='No result found for this Roll Number'
        )

    subjects = marks_data.get('subjects', {})

    if not subjects:
        return render_template(
            'index.html',
            error='No subjects found for this Roll Number'
        )

    # marks already int in DB 👍
    total = sum(subjects.values())
    percentage = round(total / (len(subjects) * 100) * 100, 2)

    if percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 35:
        grade = 'D'
    else:
        grade = 'Fail'

    return render_template(
        'result.html',
        roll_no=roll_no,
        subjects=subjects,
        total=total,
        percentage=percentage,
        grade=grade
    )
