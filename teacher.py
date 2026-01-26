from flask import Blueprint, render_template, request, redirect, url_for
from database import teachers, marks, students

teacher_bp = Blueprint("teacher", __name__)

# TEACHER LOGIN
@teacher_bp.route('/teacher/login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        teacher_check = teachers.find_one({
            'username': username,
            'password': password
        })

        if teacher_check:
            return redirect(url_for('teacher.teacher_dashboard'))
        else:
            return render_template(
                'teacher_login.html',
                error='Invalid username or password'
            )

    return render_template('teacher_login.html')


# TEACHER DASHBOARD
@teacher_bp.route('/teacher/dashboard')
def teacher_dashboard():
    all_marks = list(marks.find())
    return render_template(
        'teacher_dashboard.html',
        marks=all_marks
    )


# ADD / UPDATE MARKS
@teacher_bp.route('/add-marks', methods=['GET', 'POST'])
def add_marks():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        section = request.form['section']

        student_check = students.find_one({'roll_no': roll_no})
        if not student_check:
            return render_template(
                'add_student_marks.html',
                error='Student with this Roll Number does not exist'
            )

        subjects = {}

        if section == 'bscit':
            subjects = {
                'python': request.form.get('python'),
                'networking': request.form.get('networking'),
                'web': request.form.get('web')
            }
        elif section == 'bsccs':
            subjects = {
                'c': request.form.get('c'),
                'ds': request.form.get('ds'),
                'os': request.form.get('os')
            }
        elif section == 'bbi':
            subjects = {
                'management': request.form.get('management'),
                'finance': request.form.get('finance')
            }
        elif section == 'bcom':
            subjects = {
                'accounts': request.form.get('accounts'),
                'economics': request.form.get('economics'),
                'business': request.form.get('business')
            }

        subjects = {k: int(v) for k, v in subjects.items() if v}

        marks.update_one(
            {'roll_no': roll_no},
            {'$set': {
                'roll_no': roll_no,
                'section': section,
                'subjects': subjects
            }},
            upsert=True
        )

        return redirect(url_for('teacher.add_marks', success=1))

    success = request.args.get('success')
    return render_template('add_student_marks.html', success=success)
