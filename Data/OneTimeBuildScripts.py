import sqlite3 as sql
import csv

DbName = "FantasyDraftHost.db"
tables = {
    "teams": "Teams",
    "leagues": 'Leagues',
    "players": "Players"
}

def populateLeagues(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True

    cursor = connection.cursor()

    # Create Leagues table
    cursor.execute('''CREATE TABLE Leagues(  
                                            Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            Name TEXT UNIQUE
                                          )''')

    # Add seed data
    leagues = ['NFL', 'NBA', 'MLB']
    for league in leagues:
        cursor.execute('INSERT INTO Leagues (Name) VALUES (' + league + ')')

    cursor.commit()

    if shouldClose:
        connection.close()

def populateTeams(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True

    # Pull seed data into memory
    teamsList = []
    with open('Data\SeedData\Teams.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            teamsList.append(row)

    cursor = connection.cursor()

    # Create Teams table
    cursor.execute('''CREATE TABLE Teams(   Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            Name TEXT UNIQUE, 
                                            Abbreviation TEXT UNIQUE, 
                                            Location TEXT,
                                            LeagueId INTEGER
                                        )''')

    # Add seed data
    for team in teamsList:
        cursor.execute('INSERT INTO Teams(Name, Abbreviation, Location, LeagueId) VALUES ("' + team[0] + '","' + team[1] + '","' + team[2] + '","' + str(1) + '")')

    connection.commit()

    if shouldClose:
        connection.close()

def buildPlayers(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True
        
    cursor = connection.cursor()

    # Create Leagues table
    cursor.execute('''CREATE TABLE Players(  
                                            Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            FirstName TEXT,
                                            LastName TEXT,
                                            TeamId INTEGER,
                                            FOREIGN KEY (TeamId) 
                                                REFERENCES Teams (Id)
                                          )''')

    connection.commit()

    if shouldClose:
        connection.close()

def buildPositions(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True
    
    cursor = connection.cursor()

    # Create Leagues table
    cursor.execute('''CREATE TABLE Positions(  
                                              Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                              Name TEXT,
                                              LeagueId INTEGER
                                            )''')

def populatePositions(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True
    
    PositionList = []
    with open('Data\SeedData\Positions.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            PositionList.append(row) 

    cursor = connection.cursor()

    for position in PositionList:
        cursor.execute('SELECT Id FROM Leagues WHERE Name=?', [position[1].strip(' ')])
        position.append(cursor.fetchone()[0])
        
    for position in PositionList:
        cursor.execute('INSERT INTO Positions(Name, LeagueId) VALUES(?,?)', (position[0], position[2]))

    connection.commit()

    if shouldClose:
        connection.close()

def addPlayerPositions(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True

    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE PlayerPositions(
                                                    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                    PlayerId INTEGER, 
                                                    PositionId INTEGER
                                                  )''')

    connection.commit()

    if shouldClose:
        connection.close()
