import sqlite3 as sql
from Data import Context as db

class Player:
    def __init__(self, firstName, lastName, position, team, stats):
        self.FirstName = firstName
        self.LastName = lastName
        self.Position = position
        self.Team = team
        self.Stats = stats

def getById(id):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Players WHERE Id = ?', [id])
    print(cursor.fetchone())

    connection.close()

def savePlayer(player):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT Id FROM Teams')
    TeamId = 0

    cursor.execute('INSERT INTO Players (FirstName, LastName, TeamId) VALUES (?, ?, ?)', [player.FirstName, player.LastName, TeamId])

    cursor.commit()
    connection.close
