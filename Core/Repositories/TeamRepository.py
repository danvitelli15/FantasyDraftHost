import sqlite3 as sql
import Core.context as db
import Core.Entities.team as Team

def getByName(name):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Teams WHERE Name = ?', [name])
    teamRecord = cursor.fetchone()

    connection.close()

    team = Team.Team(teamRecord[0], teamRecord[1])
    return team