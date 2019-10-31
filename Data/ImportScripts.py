import sqlite3 as sql
import csv as csv
import Core.context as db
import Core.player as Player

def importPlayers():
    playercsv = []

    with open('TestData\BasicFootballRankings.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            playercsv.append(row)

    playersToImport = []
    for player in playercsv:
        name = player[1].split()
        playersToImport.append(Player(name[0], name[1], player[3], player[2], None))

    connection = sql.connect(db.DbName)
    cursor = connection.cursor()

    for player in playersToImport:
        if isNewRecord('Players', ['FirstName', 'LastName'], [player]):
            None

def isNewRecord(table, columns, values):
    connection = sql.connect(db.DbName)
    cursor = connection.cursor

    for x in range(0, len(columns)):
        cursor.execute('SELECT * FROM ? WHERE ? = ?', [table, columns[x], values[x]])

    if cursor.fetchone() is None:
        return True
    
    return False
