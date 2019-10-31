DbName = "FantasyDraftHost.db"
tables = {
    "leagues": {
        "name": "Leagues",
        "columnIndexes": {
            "Id": 0,
            "Name": 1
        }
    },
    "playerPositions": {
        "name": "PlayerPositions",
        "columnIndexes": {
            "Id": 0,
            "PlayerId": 1,
            "PositionId": 2
        }
    },
    "players": {
        "name": "Players",
        "columnIndexes": {
            "Id": 0,
            "FirstName": 1,
            "LastName": 2,
            "TeamId": 3
        }
    },
    "positions": {
        "name": "Positions",
        "columnIndexes": {
            "Id": 0,
            "Name": 1,
            "LeagueId": 2
        }
    },
    "teams": {
        "name": "Teams",
        "columnIndexes": {
            "Id": 0,
            "Name": 1,
            "Abbreviation": 2,
            "Location": 3,
            "LeagueId": 4
        }
    }
}

def indexOf(table, column):
    return tables[table]["columnIndexes"][column]

def tableName(table):
    return tables[table]["name"]
