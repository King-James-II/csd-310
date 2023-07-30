# This Program Connects to a database and uses an INSERT, UPDATE, AND REMOVE statements to add
# update and remove an entry from the database. After each update the database is queried using
# a INNER JOIN query to obtain the player and team data for each player and display each update.

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

    # Executing SQL INSERT statement to add new player to the player database table.
    cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) " +
                   "VALUES (21, 'Smeagol', 'Shire Folk', 1);")
    
    # Executing SQL INNER JOIN statement to retrieve Data from the the player and team tables and 
    # store in players variable.
    cursor.execute("SELECT player_id, first_name, last_name, team_name " +
                   "FROM player " +
                   "INNER JOIN team " +
                        "ON player.team_id = team.team_id " +
                    "ORDER BY player_id;")
    playerteams = cursor.fetchall()

    print("-- DISPLAYING PLAYERS AFTER INSERT --")

    # For each record retrieved from the data stored from the INNER JOIN query display player data.
    for playerteam in playerteams:
        print("Player ID: {}".format(playerteam[0]) + "\nFirst Name: {}".format(playerteam[1]) + 
              "\nLast Name: {}".format(playerteam[2])+ "\nTeam Name: {}".format(playerteam[3]) + "\n")
    
    # Execute UPDATE statement to replace existing player record with new information.
    cursor.execute("UPDATE player " +
                   "SET team_id = 2," +
                        "first_name = 'Gollum'," +
                        "last_name = 'Ring Stealer' " +
                    "WHERE first_name = 'Smeagol';")
    
    # Executing INNER JOIN select query after UPDATE to database record.
    cursor.execute("SELECT player_id, first_name, last_name, team_name " +
                   "FROM player " +
                   "INNER JOIN team " +
                        "ON player.team_id = team.team_id;")
    playerteams = cursor.fetchall()

    print("\n-- DISPLAYING PLAYERS AFTER UPDATE --")

    # Display updated data from query after UPDATE statement.
    for playerteam in playerteams:
        print("Player ID: {}".format(playerteam[0]) + "\nFirst Name: {}".format(playerteam[1]) + 
              "\nLast Name: {}".format(playerteam[2])+ "\nTeam Name: {}".format(playerteam[3]) + "\n")
    
        # Execute DELETE statement to remove the updated record.
    cursor.execute("DELETE FROM player " +
                   "WHERE first_name = 'Gollum';")
    
    # Executing INNER JOIN select query after deletion of the database record.
    cursor.execute("SELECT player_id, first_name, last_name, team_name " +
                   "FROM player " +
                   "INNER JOIN team " +
                        "ON player.team_id = team.team_id;")
    playerteams = cursor.fetchall()

    print("\n-- DISPLAYING PLAYERS AFTER DELETE --")

    # Display updated data from query after DELETE statement.
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