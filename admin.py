from flask import Blueprint, render_template, request
from database import teachers, marks ,students, admins

admin_bp = Blueprint("admin", __name__)


# ADMIN LOGIN ROUTE
@admin_bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TEMP TEST LOGIN
        if username == "admin" and password == "adminpass":
            return render_template('admin_dashboard.html')
        else:
            return render_template(
                'admin_login.html',
                error='Invalid username or password'
            )

    return render_template('admin_login.html')


# ADMIN DASHBOARD ROUTE
@admin_bp.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    return render_template('admin_dashboard.html')

# ADD TEACHER ROUTE
@admin_bp.route('/admin/add-teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        teacher_name = request.form['teacher_name']
        teacher_gender = request.form['teacher_gender']
        section = request.form['section']
        teacher_username = request.form['teacher_username']
        teacher_password = request.form['teacher_password']

        # Insert new teacher into the database
        teachers.insert_one({
            'name': teacher_name,
            'username': teacher_username,
            'password': teacher_password
        })

        return render_template(
            'manage_teacher.html',
            success='Teacher added successfully!'
        )

    return render_template('add_teacher.html')

# MANAGE TEACHER ROUTE
@admin_bp.route('/admin/manage-teacher', methods=['GET', 'POST'])
def manage_teacher():  
    all_teachers = list(teachers.find())
    return render_template('manage_teacher.html', teachers=all_teachers) 


# ADD STUDENT ROUTE
@admin_bp.route('/admin/add-student', methods=['GET', 'POST'])  
def add_student():
    if request.method == 'POST':
        student_name = request.form['student_name']
        roll_no = request.form['roll_no']
        course = request.form['course']
        # Insert new student into the database
        students.insert_one({
            'name': student_name,
            'roll_no': roll_no,
            'course': course
        })

        return render_template(
            'manage_student.html',
            success='Student added successfully!'
        )

    return render_template('add_student.html')

# MANAGE STUDENT ROUTE
@admin_bp.route('/admin/manage-student', methods=['GET', 'POST'])  
def manage_student():  
    all_students = students.find()
    return render_template('manage_student.html', students=all_students)
