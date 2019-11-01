import Data
import Core.Repositories.TeamRepository as teams
import Core.Entities.player as player
import Data.ImportScripts as scripts
import Core.context as db

# print(teams.getByName('Bears').Id)

#print(db.tableName('teams'))
scripts.importPlayers()

print(teams.getByName('Bears').Id)
