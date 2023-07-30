""" Database Insert Assignment """
""" Module 5.3 Assignment: Part 1 """
""" import MongoClient """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mt3lzum.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster using client variable with MongoClient
client = MongoClient(url)

db = client.pytech

""" Student documents """
# Thorim Darby student document
thorim = {
    "student_id": "1007",
    "first_name": "Thorim",
    "last_name": "Darby",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "4.0",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Lovett",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Jillian",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Bobby Sadget student document
bobby = {
    "student_id": "1008",
    "first_name": "Bobby",
    "last_name": "Sadget",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "3.52",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Lovett",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Jillian",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# Leanna Smolder student document
leanna = {
    "student_id": "1009",
    "first_name": "Leanna",
    "last_name": "Smolder",
    "enrollments": [
        {
            "term": "Fall 2022",
            "gpa": "1.5",
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
                    "grade": "D"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
thorim_student_id = students.insert_one(thorim).inserted_id
print("  Inserted student record Thorim Darby into the students collection with document_id " + str(thorim_student_id))

bobby_student_id = students.insert_one(bobby).inserted_id
print("  Inserted student record Bobby Sadget into the students collection with document_id " + str(bobby_student_id))

leanna_student_id = students.insert_one(leanna).inserted_id
print("  Inserted student record Leanna Smolder into the students collection with document_id " + str(leanna_student_id))

input("\n\n  Finished insertion, press any key to exit... ")