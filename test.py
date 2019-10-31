import Data
import Core.Repositories.TeamRepository as teams
import Core.Entities.player as player

print(teams.getByName('Bears').Id)