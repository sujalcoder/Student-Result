from flask import Flask
from teacher import teacher_bp
from student import students_bp
from admin import admin_bp
import os

app = Flask(__name__)
app.register_blueprint(students_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(admin_bp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
app = app