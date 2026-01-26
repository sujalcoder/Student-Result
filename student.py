from flask import Blueprint, render_template, request
from database import students, marks

students_bp = Blueprint("student", __name__)

# STUDENT LOGIN ROUTE
@students_bp.route('/', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        roll_no = request.form['roll_no']

        # TEMP TEST LOGIN
        if roll_no == "101":
            return render_template('result.html')
        else:
            return render_template(
                'index.html',
                error='Invalid username or password'
            )

    return render_template('index.html')

# STUDENT RESULT ROUTE
@students_bp.route('/result', methods=['GET', 'POST'])  
def student_result():
    return render_template('result.html')