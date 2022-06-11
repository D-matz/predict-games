from django.db import models

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    currently_guessing = models.CharField(max_length=14, default='none')
    guesses_wrong = models.IntegerField(default=0)
    guesses_right = models.IntegerField(default=0)
    prediction_skill = models.IntegerField(default=0)

#class Player(models.Model):
#    name = models.CharField(max_length=200)
#    winrate = models.CharField(max_length=200)
#    def __str__(self):
#        return self.name

class Game(models.Model):
    match_id = models.CharField(max_length=14)
    match_date = models.CharField(max_length=13)
    teamOneWin = models.BooleanField()

    name0 = models.CharField(max_length=16)
    champName0 = models.CharField(max_length=16)
    kills0 = models.IntegerField()
    death0 = models.IntegerField()
    assists0 = models.IntegerField()
    death0 = models.IntegerField()
    runePrimary0 = models.IntegerField()
    runeSecondary0 = models.IntegerField()
    slotAitem0 = models.IntegerField()
    slotBitem0 = models.IntegerField()
    slotCitem0 = models.IntegerField()
    slotDitem0 = models.IntegerField()
    slotEitem0 = models.IntegerField()
    slotFitem0 = models.IntegerField()
    gold0 = models.IntegerField()
    level0 = models.IntegerField()
    summonerD0 = models.IntegerField()
    summonerF0 = models.IntegerField()

    name1 = models.CharField(max_length=16)
    champName1 = models.CharField(max_length=16)
    kills1 = models.IntegerField()
    death1 = models.IntegerField()
    assists1 = models.IntegerField()
    death1 = models.IntegerField()
    runePrimary1 = models.IntegerField()
    runeSecondary1 = models.IntegerField()
    slotAitem1 = models.IntegerField()
    slotBitem1 = models.IntegerField()
    slotCitem1 = models.IntegerField()
    slotDitem1 = models.IntegerField()
    slotEitem1 = models.IntegerField()
    slotFitem1 = models.IntegerField()
    gold1 = models.IntegerField()
    level1 = models.IntegerField()
    summonerD1 = models.IntegerField()
    summonerF1 = models.IntegerField()

    name2 = models.CharField(max_length=16)
    champName2 = models.CharField(max_length=16)
    kills2 = models.IntegerField()
    death2 = models.IntegerField()
    assists2 = models.IntegerField()
    death2 = models.IntegerField()
    runePrimary2 = models.IntegerField()
    runeSecondary2 = models.IntegerField()
    slotAitem2 = models.IntegerField()
    slotBitem2 = models.IntegerField()
    slotCitem2 = models.IntegerField()
    slotDitem2 = models.IntegerField()
    slotEitem2 = models.IntegerField()
    slotFitem2 = models.IntegerField()
    gold2 = models.IntegerField()
    level2 = models.IntegerField()
    summonerD2 = models.IntegerField()
    summonerF2 = models.IntegerField()

    name3 = models.CharField(max_length=16)
    champName3 = models.CharField(max_length=16)
    kills3 = models.IntegerField()
    death3 = models.IntegerField()
    assists3 = models.IntegerField()
    death3 = models.IntegerField()
    runePrimary3 = models.IntegerField()
    runeSecondary3 = models.IntegerField()
    slotAitem3 = models.IntegerField()
    slotBitem3 = models.IntegerField()
    slotCitem3 = models.IntegerField()
    slotDitem3 = models.IntegerField()
    slotEitem3 = models.IntegerField()
    slotFitem3 = models.IntegerField()
    gold3 = models.IntegerField()
    level3 = models.IntegerField()
    summonerD3 = models.IntegerField()
    summonerF3 = models.IntegerField()

    name4 = models.CharField(max_length=16)
    champName4 = models.CharField(max_length=16)
    kills4 = models.IntegerField()
    death4 = models.IntegerField()
    assists4 = models.IntegerField()
    death4 = models.IntegerField()
    runePrimary4 = models.IntegerField()
    runeSecondary4 = models.IntegerField()
    slotAitem4 = models.IntegerField()
    slotBitem4 = models.IntegerField()
    slotCitem4 = models.IntegerField()
    slotDitem4 = models.IntegerField()
    slotEitem4 = models.IntegerField()
    slotFitem4 = models.IntegerField()
    gold4 = models.IntegerField()
    level4 = models.IntegerField()
    summonerD4 = models.IntegerField()
    summonerF4 = models.IntegerField()

    name5 = models.CharField(max_length=16)
    champName5 = models.CharField(max_length=16)
    kills5 = models.IntegerField()
    death5 = models.IntegerField()
    assists5 = models.IntegerField()
    death5 = models.IntegerField()
    runePrimary5 = models.IntegerField()
    runeSecondary5 = models.IntegerField()
    slotAitem5 = models.IntegerField()
    slotBitem5 = models.IntegerField()
    slotCitem5 = models.IntegerField()
    slotDitem5 = models.IntegerField()
    slotEitem5 = models.IntegerField()
    slotFitem5 = models.IntegerField()
    gold5 = models.IntegerField()
    level5 = models.IntegerField()
    summonerD5 = models.IntegerField()
    summonerF5 = models.IntegerField()

    name6 = models.CharField(max_length=16)
    champName6 = models.CharField(max_length=16)
    kills6 = models.IntegerField()
    death6 = models.IntegerField()
    assists6 = models.IntegerField()
    death6 = models.IntegerField()
    runePrimary6 = models.IntegerField()
    runeSecondary6 = models.IntegerField()
    slotAitem6 = models.IntegerField()
    slotBitem6 = models.IntegerField()
    slotCitem6 = models.IntegerField()
    slotDitem6 = models.IntegerField()
    slotEitem6 = models.IntegerField()
    slotFitem6 = models.IntegerField()
    gold6 = models.IntegerField()
    level6 = models.IntegerField()
    summonerD6 = models.IntegerField()
    summonerF6 = models.IntegerField()

    name7 = models.CharField(max_length=16)
    champName7 = models.CharField(max_length=16)
    kills7 = models.IntegerField()
    death7 = models.IntegerField()
    assists7 = models.IntegerField()
    death7 = models.IntegerField()
    runePrimary7 = models.IntegerField()
    runeSecondary7 = models.IntegerField()
    slotAitem7 = models.IntegerField()
    slotBitem7 = models.IntegerField()
    slotCitem7 = models.IntegerField()
    slotDitem7 = models.IntegerField()
    slotEitem7 = models.IntegerField()
    slotFitem7 = models.IntegerField()
    gold7 = models.IntegerField()
    level7 = models.IntegerField()
    summonerD7 = models.IntegerField()
    summonerF7 = models.IntegerField()

    name8 = models.CharField(max_length=16)
    champName8 = models.CharField(max_length=16)
    kills8 = models.IntegerField()
    death8 = models.IntegerField()
    assists8 = models.IntegerField()
    death8 = models.IntegerField()
    runePrimary8 = models.IntegerField()
    runeSecondary8 = models.IntegerField()
    slotAitem8 = models.IntegerField()
    slotBitem8 = models.IntegerField()
    slotCitem8 = models.IntegerField()
    slotDitem8 = models.IntegerField()
    slotEitem8 = models.IntegerField()
    slotFitem8 = models.IntegerField()
    gold8 = models.IntegerField()
    level8 = models.IntegerField()
    summonerD8 = models.IntegerField()
    summonerF8 = models.IntegerField()

    name9 = models.CharField(max_length=16)
    champName9 = models.CharField(max_length=16)
    kills9 = models.IntegerField()
    death9 = models.IntegerField()
    assists9 = models.IntegerField()
    death9 = models.IntegerField()
    runePrimary9 = models.IntegerField()
    runeSecondary9 = models.IntegerField()
    slotAitem9 = models.IntegerField()
    slotBitem9 = models.IntegerField()
    slotCitem9 = models.IntegerField()
    slotDitem9 = models.IntegerField()
    slotEitem9 = models.IntegerField()
    slotFitem9 = models.IntegerField()
    gold9 = models.IntegerField()
    level9 = models.IntegerField()
    summonerD9 = models.IntegerField()
    summonerF9 = models.IntegerField()

    def __str__(self):
        return self.match_id