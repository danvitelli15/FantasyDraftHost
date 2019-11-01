import sqlite3 as sql
import Core.context as db

import Core.Repositories.TeamRepository as teamData
import Core.Entities.team as teamData

def getById(id):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Players WHERE Id = ?', [id])
    print(cursor.fetchone())

    connection.close()

def savePlayer(player):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()


    TeamId = teamData.getByAbbreviation(player.Team).Id
    TeamId = teamData.getByName(player.Team).Id

    cursor.execute('INSERT INTO Players (FirstName, LastName, TeamId) VALUES (?, ?, ?)', [player.FirstName, player.LastName, TeamId])

    connection.commit()
    connection.close
