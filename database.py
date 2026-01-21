from pymongo import MongoClient
Mongo_URL="mongodb+srv://admin:admin@cluster0.atgtlwk.mongodb.net/?appName=Cluster0"
client = MongoClient(Mongo_URL)
db = client['student_marks']

admins=db.admins
students=db.students    
marks=db.marks
teachers=db.teachers
print(db.list_collection_names())
students.insert_one({
    "full_name": "Test Student",
    "roll_no": "1001",
    "class": "10",
    "section": "A"
})
