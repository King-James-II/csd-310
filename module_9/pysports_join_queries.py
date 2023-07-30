# This Program Connects to a database and uses an INNER JOIN query to pull data from the database
# about the players and their team names.

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

# Try to connect to the database using the connection configuration. If successful display 
# connection success message.
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}\n".format(config["user"
        ], config["host"], config["database"]))

    # Create database cursor to process and store queries to the database.
    cursor = db.cursor()

    # Executing SQL INNER JOIN statement to retrieve Data from the the player and team tables and 
    # store in players variable.
    cursor.execute("SELECT player_id, first_name, last_name, team_name " +
                   "FROM player " +
                   "INNER JOIN team " +
                        "ON player.team_id = team.team_id;")
    playerteams = cursor.fetchall()

    print("-- DISPLAY PLAYER RECORDS --")

    # For each record retrieved from the data stored from the INNER JOIN query display player data.
    for playerteam in playerteams:
        print("Player ID: {}".format(playerteam[0]) + "\nFirst Name: {}".format(playerteam[1]) + 
              "\nLast Name: {}".format(playerteam[2])+ "\nTeam Name: {}".format(playerteam[3]) + "\n")
    
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