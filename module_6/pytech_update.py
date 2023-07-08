# Database Update Assignment
# Module 6.2 Assignment
# import MongoClient
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mt3lzum.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster using the connection string
client = MongoClient(url)
#specifying to connect to the pytech database and students collection
db = client.pytech
students = db.students

# Find all student documents in the collection  and store within student_list variable
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# Print all students within the student documents collection
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  "+
          "Last Name: " + doc["last_name"] + "\n")

# updating student document where student_id is 1007
students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Blitzendorf"}})

# finding the updated student document where student id is 1007
thorim = students.find_one({"student_id": "1007"})

# display the updated student document values
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("  Student ID: " + thorim["student_id"] + "\n  First Name: " + thorim["first_name"] + "\n  Last Name: " + thorim["last_name"] + "\n")

# Terminating program
input("\n\n  End of program, press any key to continue...")