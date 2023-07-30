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

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"
        ], config["host"], config["database"]))

    print("-- DISPLAY TEAM RECORDS --")

    # Create database cursor to process and store queries to the database.
    cursor = db.cursor()

    # Executing SQL statements to retrieve Team Data from the database and store in teams variable.
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    # For each record retrieved from the data stored from the query display team data.
    for team in teams:
        print("Team ID: {}".format(team[0]) + "\nTeam Name: {}".format(team[1]) + 
              "\nMascot: {}".format(team[2])+ "\n")

    # Executing SQL statements to retrieve Player Data from the database and store in players variable.
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    print("-- DISPLAY PLAYER RECORDS --")

    # For each record retrieved from the data stored from the query display player data.
    for player in players:
        print("Player ID: {}".format(player[0]) + "\nFirst Name: {}".format(player[1]) + 
              "\nLast Name: {}".format(player[2])+ "\nTeam ID: {}".format(player[3]) + "\n")
    
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