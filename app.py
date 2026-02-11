from flask import Flask
from teacher import teacher_bp
from student import students_bp
from admin import admin_bp

app = Flask(__name__)
app.register_blueprint(students_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(admin_bp)

app.run(debug=True)
app = app