from flask import Flask
from teacher import teacher_bp

app = Flask(__name__)
app.register_blueprint(teacher_bp)

app.run(debug=True)
