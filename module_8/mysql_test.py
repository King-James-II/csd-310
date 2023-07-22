# Import MysQL connector
import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    "user": 'pysports_user',
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Try to connect to the database using the connection configuration. If successful display connection success message.
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

# Catch errors and display appropriate messages based on error type.
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

# After connection establishes or fails close the connection to the database.
finally:
    db.close()