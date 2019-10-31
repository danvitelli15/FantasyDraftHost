import sqlite3 as sql
import Core.context as db

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