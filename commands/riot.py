
import cassiopeia as cass

cass.set_riot_api_key("RGAPI-4bc2c2fc-1076-4acb-9054-74196c6072e4")


"""Function to get summoner given the RiotId and region"""
def getSummoner(riotId, region):
    return cass.get_summoner(name = riotId, region = region.upper())

# Given a champion returns the image data of that champion
def getChampImage(champion):
    return champion.skins[0].splash_url

#Given a summoner return the stats of the summoner in his last match
def lastMatchStat(summoner):
    return summoner.match_history[0].participants[summoner]


def showOffLevel(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    # summoner = cass.get_summoner(name = "serene hell", region="EUW")
    return summoner.level


def showID(riotId, region):
    summoner = cass.get_summoner(name = riotId, region = region.upper())
    return summoner.account_id


#Function to get stats from the last match
def getMatch(matchstats):
    player = matchstats
    double_kills = getDoubleKills(player.stats)
    triple_kills = getTripleKills(player.stats)
    quadra_kills = getQuadraKills(player.stats)
    penta_kills = getPentaKills(player.stats)
    kda = getKDA(player.stats)
    damage = getDamageToChampions(player.stats)
    msg = (
f'''While playing **{player.champion.name}** you got:
>>> {double_kills} double kills
{triple_kills} triple kills
{quadra_kills} quadra kills
{penta_kills} penta kills
{kda} was your kda
You dealt {damage} damage to champions'''
        )    
    return msg


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
def hiddenStats(participant):
    player = participant
    q_cast = getQCount(player.stats)
    w_cast = getWCount(player.stats)
    e_cast = getECount(player.stats)
    r_cast = getRCount(player.stats)
    time_dead = getTimeDead(player.stats)
    return (
f'''While playing **{player.champion.name}** you used:
>>> Q {q_cast} times
W {w_cast} times
E {e_cast} times
R {r_cast} times
And you spent **{time_dead}** seconds dead'''
            )

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
if __name__ == "__main__":
    summoner = getSummoner("serene hell", "euw")
    test_sum = hiddenStats(lastMatchStat(summoner))
    win = lastMatchStat(summoner).champion.skins[0].splash_url
    # noti = test_sum.match_history[0].participants[test_sum].champion.name
    print(win)

    #
    # summoner = cass.get_summoner(name = "Romans 8 11#06020", region="EUW")
    # all_games = summoner.level
    # print(all_games)
