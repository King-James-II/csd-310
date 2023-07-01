from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:admin@cluster0.mt3lzum.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
db = client.pytech
print("Pinged your deployment. You successfully connected to MongoDB! \n\n-- Pytech C0llection +"
      "List --")
print(db.list_collection_names())
print ("\n\n")
input("End of program, press any key to exit...")