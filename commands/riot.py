
import cassiopeia as cass

cass.set_riot_api_key("RGAPI-643a698f-9b32-4447-910f-298a777b7cdf")


def showOffLevel(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    # summoner = cass.get_summoner(name = "serene hell", region="EUW")
    return summoner.level


def showID(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    return summoner.account_id


#Function to get stats from the last match
def getMatch(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    last_match = summoner.match_history[0]
    player = last_match.participants[summoner]
    # while i < 10:
    #     if (last_match.participants[i].name == riotId):
    #         player = last_match.participants[i]
    #         break
    #     else: i += 1
    double_kills = getDoubleKills(player.stats)
    triple_kills = getTripleKills(player.stats)
    quadra_kills = getQuadraKills(player.stats)
    penta_kills = getPentaKills(player.stats)
    kda = getKDA(player.stats)
    damage = getDamageToChampions(player.stats)
    return f'While playing **{player.champion.name}** you got:\n{double_kills} double kills\n{triple_kills} triple kills\n{quadra_kills} quadra kills\n{penta_kills} penta kills\n{kda} was your kda\nYou dealt {damage} damage to champions'


def getKDA(stats):
    return f'{stats.kills}/{stats.deaths}/{stats.assists}'

def getDamageToChampions(stats):
    return stats.total_damage_dealt_to_champions

def getDoubleKills(stats):
    return stats.double_kills
def getTripleKills(stats):
    return stats.triple_kills
def getQuadraKills(stats):
    return stats.quadra_kills
def getPentaKills(stats):
    return stats.penta_kills



#HIDDEN STATS
def hiddenStats(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    last_match = summoner.match_history[0]
    player = last_match.participants[summoner]
    q_cast = getQCount(player.stats)
    w_cast = getWCount(player.stats)
    e_cast = getECount(player.stats)
    r_cast = getRCount(player.stats)
    time_dead = getTimeDead(player.stats)
    return f'While playing **{player.champion.name}** you used:\nQ {q_cast} times\nW {w_cast} times\nE {e_cast} times\nR {r_cast} times\nAnd you spent **{time_dead}** seconds dead'

def getQCount(stats):
    return stats.spell_1_casts
def getWCount(stats):
    return stats.spell_2_casts
def getECount(stats):
    return stats.spell_3_casts
def getRCount(stats):
    return stats.spell_4_casts
def getTimeDead(stats):
    return stats.total_time_spent_dead


# DEBUGGING FUNCTIONS
noti = hiddenStats("serene hell", "EUW")
print(noti)

    #
    # summoner = cass.get_summoner(name = "Romans 8 11#06020", region="EUW")
    # all_games = summoner.level
    # print(all_games)
