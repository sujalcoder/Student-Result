import os
from pymongo import MongoClient

Mongo_URL = os.environ.get("MONGO_URL")

try:
    client = MongoClient(Mongo_URL)
    db = client["student_marks"]

    admins = db.admins
    students = db.students
    marks = db.marks
    teachers = db.teachers

except Exception as e:
    print("MongoDB Connection Failed:", e)
    admins = None
    students = None
    marks = None
    teachers = None
