""" Database Insert Assignment """
""" Module 5.3 Assignment: Part 2 """
""" import MongoClient """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mt3lzum.mongodb.net/?retryWrites=true&w=majority"

# Connect to the MongoDB cluster0
client = MongoClient(url)

# Connect to pytech database
db = client.pytech

# Use to pull students collection
students = db.students

# Find all student documents in the collection  and store within student_list variable
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Print all students within the student documents
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  "+
          "Last Name: " + doc["last_name"] + "\n")

# Find one document using student_id
leanna = students.find_one({"student_id": "1009"})

# Display the found student document
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + leanna["student_id"] + "\n  First Name: " + leanna["first_name"] + "\n  "+
      "Last Name: " + leanna["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")