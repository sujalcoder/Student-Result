from flask import Blueprint, render_template, request , redirect, url_for
from database import teachers, marks ,students, admins
from pymongo.errors import DuplicateKeyError
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

        # 🔍 Check duplicate username
        existing_teacher = teachers.find_one({'username': teacher_username})
        if existing_teacher:
            return render_template(
                'add_teacher.html',
                error='Teacher username already exists'
            )

        # ✅ Insert teacher
        teachers.insert_one({
            'name': teacher_name,
            'gender': teacher_gender,
            'section': section,
            'username': teacher_username,
            'password': teacher_password   # hashing later
        })

        # 🔁 Redirect to avoid duplicate submit
        return redirect(url_for('admin.manage_teacher'))

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
        section = request.form['section ']
        existing_student=students.find_one({'roll_no': roll_no})
        if existing_student:
            return render_template(
                'add_student.html',
                error='Roll No already exists'
            )
        else:

         # ✅ Insert student
            try:
                students.insert_one({
                   'name': student_name,
                   'roll_no': roll_no,
                   'section': section
            })

            # ✅ Redirect after POST (VERY IMPORTANT)
                return redirect(url_for('admin.manage_student'))

            except DuplicateKeyError:
                return render_template(
                  'add_student.html',
                   error='Roll No already exists'
            )

            except Exception as e:
                return render_template(
                  'add_student.html',
                   error='Something went wrong'
            )

    return render_template('add_student.html')

# MANAGE STUDENT ROUTE
@admin_bp.route('/admin/manage-student', methods=['GET', 'POST'])  
def manage_student():  
    all_students = students.find()
    return render_template('manage_student.html', students=all_students)
