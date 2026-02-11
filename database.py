from pymongo import MongoClient

Mongo_URL="mongodb+srv://admin:admin@cluster0.atgtlwk.mongodb.net/?appName=Cluster0"

client = MongoClient(Mongo_URL)
db = client['student_marks']

admins=db.admins
students=db.students    
marks=db.marks
teachers=db.teachers