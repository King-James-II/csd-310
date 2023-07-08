# Database Delete Assignment
# Module 6.3 Assignment
# import MongoClient
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mt3lzum.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster using the connection string
client = MongoClient(url)
#specifying to connect to the pytech database and students collection
db = client.pytech
students = db.students

# Bethany Landox student document
bethany = {
    "student_id": "1010",
    "first_name": "Bethany",
    "last_name": "Landox",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "2.1",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Lovett",
                    "grade": "C-"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Jillian",
                    "grade": "D+"
                }
            ]
        }
    ]
}

# Find all student documents in the collection  and store within student_list variable
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Print all students within the student documents collection
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  "+
          "Last Name: " + doc["last_name"] + "\n")

# insert statement with output 
print("\n  -- INSERT STATEMENTS --")
bethany_student_id = students.insert_one(bethany).inserted_id
print("  Inserted student record Bethany Landox into the students collection with document_id " + str(bethany_student_id))

# finding the new student document where student id is 1010
bethany = students.find_one({"student_id": "1010"})

# display the updated student document list
print("\n  -- DISPLAYING STUDENT TEST DOCUMENT --")
print("  Student ID: " + bethany["student_id"] + "\n  First Name: " + bethany["first_name"] + "\n  Last Name: " + bethany["last_name"] + "\n")

#removing the previously inserted entry
students.delete_one({"student_id": "1010"})

# retrieve updated student list after deletion
new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Print all students within the student documents collection
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  "+
          "Last Name: " + doc["last_name"] + "\n")

# Exiting program.
input("\n\n  End of program, press any key to continue...")