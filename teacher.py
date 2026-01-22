from flask import Blueprint, render_template, request
from database import teachers, marks

teacher_bp = Blueprint("teacher", __name__)

# TEACHER LOGIN ROUTE
@teacher_bp.route('/teacher/login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TEMP TEST LOGIN
        if username == "admin" and password == "pass":
            return render_template('teacher_dashboard.html')
        else:
            return render_template(
                'teacher_login.html',
                error='Invalid username or password'
            )

    return render_template('teacher_login.html')


# TEACHER DASHBOARD ROUTE
@teacher_bp.route('/teacher_dashboard', methods=['GET', 'POST'])
def teacher_dashboard():
    return render_template('teacher_dashboard.html')



