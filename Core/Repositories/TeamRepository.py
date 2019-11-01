import sqlite3 as sql
import Core.context as db
import Core.Entities.team as Team

def getByName(name):
    abbreviation.strip(' ')
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM ? WHERE Name = ?', [db.tableName("teams"), name])
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Teams WHERE Name = ?', [name])
    teamRecord = cursor.fetchone()

    connection.close()

    team = Team.Team(id=teamRecord[0], name=teamRecord[1])
    return team

def getByAbbreviation(abbreviation):
    abbreviation.strip(' ')
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Teams WHERE Abbreviation = ?', [' ' + abbreviation])
    teamRecord = cursor.fetchone()

    connection.close()

    team = Team.Team(id=teamRecord[0], name=teamRecord[1])
    return team

def saveTeam(team):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    leagueId = None

    cursor.execute('INSERT INTO Teams (Name, Abbreviation, Location, LeagueId) VALUES (?, ?, ?, ?)', [team.Name, team.Abbreviation, team.Location, leagueId])

    connection.commit()
    connection.close
    return team
