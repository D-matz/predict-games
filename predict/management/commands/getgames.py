from django.core.management.base import BaseCommand, CommandError
from predict.models import Game as game
import requests
import time
import glob

api_key = 'oops'


def setgame(pnum, g, name, champ, kills, deaths, assists, gold, level, runePrimary, runeSecondary, items, summonerD, summonerF):
    if pnum == 0:
        g.name0 = name
        g.champName0 = champ
        g.kills0 = kills
        g.death0 = deaths
        g.assists0 = assists
        g.gold0 = gold
        g.level0 = level
        g.runePrimary0 = runePrimary
        g.runeSecondary0 = runeSecondary
        g.slotAitem0 = items[0]
        g.slotBitem0 = items[1]
        g.slotCitem0 = items[2]
        g.slotDitem0 = items[3]
        g.slotEitem0 = items[4]
        g.slotFitem0 = items[5]
        g.summonerD0 = summonerD
        g.summonerF0 = summonerF
    if pnum == 1:
        g.name1 = name
        g.champName1 = champ
        g.kills1 = kills
        g.death1 = deaths
        g.assists1 = assists
        g.gold1 = gold
        g.level1 = level
        g.runePrimary1 = runePrimary
        g.runeSecondary1 = runeSecondary
        g.slotAitem1 = items[0]
        g.slotBitem1 = items[1]
        g.slotCitem1 = items[2]
        g.slotDitem1 = items[3]
        g.slotEitem1 = items[4]
        g.slotFitem1 = items[5]
        g.summonerD1 = summonerD
        g.summonerF1 = summonerF
    if pnum == 2:
        g.name2 = name
        g.champName2 = champ
        g.kills2 = kills
        g.death2 = deaths
        g.assists2 = assists
        g.gold2 = gold
        g.level2 = level
        g.runePrimary2 = runePrimary
        g.runeSecondary2 = runeSecondary
        g.slotAitem2 = items[0]
        g.slotBitem2 = items[1]
        g.slotCitem2 = items[2]
        g.slotDitem2 = items[3]
        g.slotEitem2 = items[4]
        g.slotFitem2 = items[5]
        g.summonerD2 = summonerD
        g.summonerF2 = summonerF
    if pnum == 3:
        g.name3 = name
        g.champName3 = champ
        g.kills3 = kills
        g.death3 = deaths
        g.assists3 = assists
        g.gold3 = gold
        g.level3 = level
        g.runePrimary3 = runePrimary
        g.runeSecondary3 = runeSecondary
        g.slotAitem3 = items[0]
        g.slotBitem3 = items[1]
        g.slotCitem3 = items[2]
        g.slotDitem3 = items[3]
        g.slotEitem3 = items[4]
        g.slotFitem3 = items[5]
        g.summonerD3 = summonerD
        g.summonerF3 = summonerF
    if pnum == 4:
        g.name4 = name
        g.champName4 = champ
        g.kills4 = kills
        g.death4 = deaths
        g.assists4 = assists
        g.gold4 = gold
        g.level4 = level
        g.runePrimary4 = runePrimary
        g.runeSecondary4 = runeSecondary
        g.slotAitem4 = items[0]
        g.slotBitem4 = items[1]
        g.slotCitem4 = items[2]
        g.slotDitem4 = items[3]
        g.slotEitem4 = items[4]
        g.slotFitem4 = items[5]
        g.summonerD4 = summonerD
        g.summonerF4 = summonerF
    if pnum == 5:
        g.name5 = name
        g.champName5 = champ
        g.kills5 = kills
        g.death5 = deaths
        g.assists5 = assists
        g.gold5 = gold
        g.level5 = level
        g.runePrimary5 = runePrimary
        g.runeSecondary5 = runeSecondary
        g.slotAitem5 = items[0]
        g.slotBitem5 = items[1]
        g.slotCitem5 = items[2]
        g.slotDitem5 = items[3]
        g.slotEitem5 = items[4]
        g.slotFitem5 = items[5]
        g.summonerD5 = summonerD
        g.summonerF5 = summonerF
    if pnum == 6:
        g.name6 = name
        g.champName6 = champ
        g.kills6 = kills
        g.death6 = deaths
        g.assists6 = assists
        g.gold6 = gold
        g.level6 = level
        g.runePrimary6 = runePrimary
        g.runeSecondary6 = runeSecondary
        g.slotAitem6 = items[0]
        g.slotBitem6 = items[1]
        g.slotCitem6 = items[2]
        g.slotDitem6 = items[3]
        g.slotEitem6 = items[4]
        g.slotFitem6 = items[5]
        g.summonerD6 = summonerD
        g.summonerF6 = summonerF
    if pnum == 7:
        g.name7 = name
        g.champName7 = champ
        g.kills7 = kills
        g.death7 = deaths
        g.assists7 = assists
        g.gold7 = gold
        g.level7 = level
        g.runePrimary7 = runePrimary
        g.runeSecondary7 = runeSecondary
        g.slotAitem7 = items[0]
        g.slotBitem7 = items[1]
        g.slotCitem7 = items[2]
        g.slotDitem7 = items[3]
        g.slotEitem7 = items[4]
        g.slotFitem7 = items[5]
        g.summonerD7 = summonerD
        g.summonerF7 = summonerF
    if pnum == 8:
        g.name8 = name
        g.champName8 = champ
        g.kills8 = kills
        g.death8 = deaths
        g.assists8 = assists
        g.gold8 = gold
        g.level8 = level
        g.runePrimary8 = runePrimary
        g.runeSecondary8 = runeSecondary
        g.slotAitem8 = items[0]
        g.slotBitem8 = items[1]
        g.slotCitem8 = items[2]
        g.slotDitem8 = items[3]
        g.slotEitem8 = items[4]
        g.slotFitem8 = items[5]
        g.summonerD8 = summonerD
        g.summonerF8 = summonerF
    if pnum == 9:
        g.name9 = name
        g.champName9 = champ
        g.kills9 = kills
        g.death9 = deaths
        g.assists9 = assists
        g.gold9 = gold
        g.level9 = level
        g.runePrimary9 = runePrimary
        g.runeSecondary9 = runeSecondary
        g.slotAitem9 = items[0]
        g.slotBitem9 = items[1]
        g.slotCitem9 = items[2]
        g.slotDitem9 = items[3]
        g.slotEitem9 = items[4]
        g.slotFitem9 = items[5]
        g.summonerD9 = summonerD
        g.summonerF9 = summonerF
    return g

class Command(BaseCommand):
    help = 'gets games'

    def add_arguments(self, parser):
        print("add no args")

    def handle(self, *args, **options):
        print("handle")

        files = glob.glob('C:/Users/Owner/Desktop/hunter/pob/*')
        for g in files:
            gameid = g[-14:]
#        gameid = 'NA1_4139672423'
            if game.objects.filter(match_id=gameid).exists():
               print("already exists", gameid)
            else:
                print("lookup", gameid)
                time.sleep(2)
                game_json = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/'+gameid+'?api_key='+api_key).json()

                g = game()
                g.match_id = gameid
                g.match_date = game_json['info']['gameCreation']
                g.teamOneWin = game_json['info']['participants'][0]['win']

                for playernum in range(0,10):
                    player = game_json['info']['participants'][playernum]
                    #print(player)
                    #print("cname", player['championName'])
                    name = player['summonerName']
                    champ = player['championName']
                    kills = player['kills']
                    deaths = player['deaths']
                    assists = player['assists']
                    gold = player['goldEarned']
                    level = player['champLevel']
                    runePrimary = player['perks']['styles'][0]['selections'][0]['perk']
                    runeSecondary = player['perks']['styles'][1]['style']
                    items = []
                    sum1 = player['summoner1Id']
                    sum2 = player['summoner2Id']
                    for i in range(0,6):
                        items.append(player['item'+str(i)])
                    g = setgame(playernum, g, name, champ, kills, deaths, assists, gold, level, runePrimary, runeSecondary, items, sum1, sum2)
                    #print(name, champ, kills, deaths, assists, gold, level, runePrimary, runeSecondary, items)
                print(g.level0, g.teamOneWin)
                print("save?", g.runeSecondary0)
                g.save()
