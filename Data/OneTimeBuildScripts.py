import sqlite3 as sql
import csv

DbName = "FantasyDraftHost.db"
tables = {
    "teams": "Teams"
}

def buildTabes():
    populateTeams()

def populateSports(connection=None, shouldClose=False):
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
        cursor.execute('''INSERT INTO Teams (Name) VALUES ({league})''')

    cursor.commit()

    if shouldClose:
        connection.close()

def populateTeams(connection=None, shouldClose=False):
    if connection is None:
        connection = sql.connect(DbName)
        shouldClose = True

    # Pull seed data into memory
    teamsList = List()
    with open('./SeedData/Teams.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            teamsList.append(row)

    cursor = connection.cursor()

    # Create Teams table
    cursor.execute('''CREATE TABLE Teams(   Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            Name TEXT UNIQUE, 
                                            Abbreviation TEXT UNIQUE, 
                                            Location TEXT
                                        )''')

    # Add seed data
    for team in teamsList:
        cursor.execute('''INSERT INTO Teams(
                                            Name,
                                            Abbreviation,
                                            Location
                                           )
                                    VALUES (    
                                            {team[0]}
                                            {team[1]}
                                            {team[2]}
                                           )''')

    cursor.commit()

    if shouldClose:
        connection.close()
