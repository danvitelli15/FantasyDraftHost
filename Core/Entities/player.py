import sqlite3 as sql

class Player:
    def __init__(self, firstName, lastName, position, team, stats):
        self.FirstName = firstName
        self.LastName = lastName
        self.Position = position
        self.Team = team
        self.Stats = stats
