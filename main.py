import random

import cassiopeia as cass

cass.set_riot_api_key("RGAPI-643a698f-9b32-4447-910f-298a777b7cdf")





summoner = cass.get_summoner(name = "serene hell", region="EUW")
all_games = summoner.match_history[0]
print(all_games.participants[3].stats.win)
