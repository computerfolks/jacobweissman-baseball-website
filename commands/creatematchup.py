import decimal
from django.core.management.base import BaseCommand
from app_bb.models import matchup
from app_bb.models import pitcher
from app_bb.models import batter
from app_bb.models import team
from pybaseball import *
import numpy as np
import matplotlib.pylab as plt
import requests
import bs4
from app_bb.baseball_functions import three_letter

class Command(BaseCommand):
  def handle(self, *args, **options):
    # removed to change deletion to game-by-game
    # try:
    #   entries = matchup.objects.all()
    #   entries.delete()
    # except:
    #   pass
    #access daily lineups from baseball press https://www.baseballpress.com/lineups?q=%2Flineups
    # result = requests.get("https://www.baseballpress.com/lineups?q=%2Flineups")
    result = requests.get("https://www.baseballpress.com/lineups/2022-09-06")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    # each of these represents a game
    games = soup.select(".lineup-card")
    for game in games:
      temp = game.select(".lineup-card-header")[0]
      gametime_import = temp.select(".c")[1].text.split('\n')[2]
      gamedate_import = temp.select(".c")[1].text.split('\n')[1].replace(",","")
      awayteamworksheet = game.select(".mlb-team-logo")[0]
      hometeamworksheet = game.select(".mlb-team-logo")[1]  
      awayteam_import = awayteamworksheet.text.replace("\n","").lower()
      hometeam_import = hometeamworksheet.text.replace("\n","").lower()
      awayteam_import = three_letter(awayteam_import)
      hometeam_import = three_letter(hometeam_import)

      awayteam_import = team.objects.get(name = awayteam_import)
      hometeam_import = team.objects.get(name = hometeam_import)

      #error-check to see if the lineup is loaded yet or not
      lineupworksheetsoup = game.select(".lineup-card-body")[0]
      awaylineupsoup = lineupworksheetsoup.select(".col--min")[0]
      homelineupsoup = lineupworksheetsoup.select(".col--min")[1]
      temperatureworksheetsoup = game.select(".lineup-card-footer")[0].text.split("Temp: ")[1]
      gametimetemp_import = temperatureworksheetsoup.split("°")[0] 
      rainworksheetsoup = game.select(".lineup-card-footer")[0].text.split("Precip: ")[1]
      chanceofrain_import = rainworksheetsoup.split("%")[0]
      if awaylineupsoup.text.replace("\n","").replace(" ","").lower() == "nolineupreleased":
        awaylineupposted_import = False
      else:
        awaylineupposted_import = True

      if homelineupsoup.text.replace("\n","").replace(" ","").lower() == "nolineupreleased":
        homelineupposted_import = False
      else:
        homelineupposted_import = True


      # delete the old version of the matchup, use gametime to not immediately delete doubleheaders
      # NOTE: this has a potential flaw of the gametime switching causing the program to think it is a doubleheader
      if matchup.objects.filter(awayteam = awayteam_import, gametime = gametime_import).exists():
        # print("deleting matchup")
        # print(matchup.objects.filter(awayteam = awayteam_import, gametime = gametime_import))
        # print("deleted", awayteam_import, gametime_import)
        matchup.objects.filter(awayteam = awayteam_import, gametime = gametime_import).delete()
      # elif matchup.objects.filter(awayteam = awayteam_import).exists():
      #   print("deleting matchup no gametime")
      #   print(matchup.objects.filter(awayteam = awayteam_import))
      #   matchup.objects.filter(awayteam = awayteam_import).delete()

      
      #delete a matchup if it was delayed, because that means it will otherwise show up as a duplicate
      #this will run if and only if the new matchup time has already been loaded, and will fix the duplicate problem
      for delaymatchup in matchup.objects.all():
        if delaymatchup.awayteam == awayteam_import and 'delay' in delaymatchup.gamedate.lower():
          delaymatchup.delete()
        


      doubleheadergametwo_import = False
      #double-header check
      for doubleheadermatchupcheck in matchup.objects.all():
          # if the matchup already exists, and (the first game starts earlier than the second game (and game we are currently importing)) or (game starts with 10 or 11, so game really does start later even though 2 > 10 for these purposes)
        if (doubleheadermatchupcheck.awayteam == awayteam_import) and ((doubleheadermatchupcheck.gametime < gametime_import) or (gametime_import.startswith('10') or gametime_import.startswith('11'))):
          # print(doubleheadermatchupcheck, " ", awayteam_import)
          # print(doubleheadermatchupcheck.gametime, " ", gametime_import)
          doubleheadermatchupcheck.doubleheadergameone = True
          doubleheadermatchupcheck.save()
          doubleheadergametwo_import = True
      
      #the rest of the code should only run if both lineups are loaded

      if homelineupposted_import == True and awaylineupposted_import == True:
        #print(hometeam_import + " " + awayteam_import)
        #continue filling in matchup data
        awaypitcher_import = game.select(".player")[0] 
        homepitcher_import = game.select(".player")[1]
        awaypitchername = awaypitcher_import.text # do not use name becaues different desktop/mobile names
        homepitchername = homepitcher_import.text
        awaypitchermlbamid = awaypitcher_import.find("a")["data-mlb"] # only use ID's
        homepitchermlbamid = homepitcher_import.find("a")["data-mlb"]
        awaypitcherkey_bbref = awaypitcher_import.find("a")["data-bref"]
        homepitcherkey_bbref = homepitcher_import.find("a")["data-bref"]
        awaypositions_import = ""
        homepositions_import = ""

        #access the pitchers
        try:
          awaypitcher_using_mlbamid = pitcher.objects.get(key_mlbam = awaypitchermlbamid)
        except:
          awaypitcher_using_mlbamid = pitcher.objects.get(lastname = "dummy", firstname = "dummy") # to be replaced by dummy pitcher
        try:
          homepitcher_using_mlbamid = pitcher.objects.get(key_mlbam = homepitchermlbamid)
        except:
          homepitcher_using_mlbamid = pitcher.objects.get(lastname = "dummy", firstname = "dummy") # to be replaced by dummy pitcher
        # get all 9 batters for each side, away first
        awayplayeronesoup = awaylineupsoup.select(".player")[0]
        awayplayeronekey_mlbam = awayplayeronesoup.find("a")["data-mlb"]
        awaypositions_import += awayplayeronesoup.text[-2:] # the catcher takes two spots with one being an empty space, which makes future code EASIER so leave it be
        try:
          awayplayerone = batter.objects.get(key_mlbam = awayplayeronekey_mlbam)
        except:
          awayplayerone = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayertwosoup = awaylineupsoup.select(".player")[1]
        awayplayertwokey_mlbam = awayplayertwosoup.find("a")["data-mlb"]
        awaypositions_import += awayplayertwosoup.text[-2:]
        try:
          awayplayertwo = batter.objects.get(key_mlbam = awayplayertwokey_mlbam)
        except:
          awayplayertwo = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayerthreesoup = awaylineupsoup.select(".player")[2]
        awayplayerthreekey_mlbam = awayplayerthreesoup.find("a")["data-mlb"]
        awaypositions_import += awayplayerthreesoup.text[-2:]
        try:
          awayplayerthree = batter.objects.get(key_mlbam = awayplayerthreekey_mlbam)
        except:
          awayplayerthree = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayerfoursoup = awaylineupsoup.select(".player")[3]
        awayplayerfourkey_mlbam = awayplayerfoursoup.find("a")["data-mlb"]
        awaypositions_import += awayplayerfoursoup.text[-2:]
        #print(awayplayerfourkey_mlbam)
        try:
          awayplayerfour = batter.objects.get(key_mlbam = awayplayerfourkey_mlbam)
        except:
          awayplayerfour = batter.objects.get(lastname = "dummy", firstname = "dummy")
        # if awayplayerfour == None:
        #   awayplayerfour = batter.objects.get(key_mlbam = 592450)
        # print(awayplayerfour.id)
        # print(awayplayerfour.lastname)

        awayplayerfivesoup = awaylineupsoup.select(".player")[4]
        awayplayerfivekey_mlbam = awayplayerfivesoup.find("a")["data-mlb"]
        awaypositions_import += awayplayerfivesoup.text[-2:]
        try:
          awayplayerfive = batter.objects.get(key_mlbam = awayplayerfivekey_mlbam)
        except:
          awayplayerfive = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayersixsoup = awaylineupsoup.select(".player")[5]
        awayplayersixkey_mlbam = awayplayersixsoup.find("a")["data-mlb"]
        awaypositions_import += awayplayersixsoup.text[-2:]
        try:
          awayplayersix = batter.objects.get(key_mlbam = awayplayersixkey_mlbam)
        except:
          awayplayersix = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayersevensoup = awaylineupsoup.select(".player")[6]
        awayplayersevenkey_mlbam = awayplayersevensoup.find("a")["data-mlb"]
        awaypositions_import += awayplayersevensoup.text[-2:]
        try:
          awayplayerseven = batter.objects.get(key_mlbam = awayplayersevenkey_mlbam)
        except:
          awayplayerseven = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayereightsoup = awaylineupsoup.select(".player")[7]
        awayplayereightkey_mlbam = awayplayereightsoup.find("a")["data-mlb"]
        awaypositions_import += awayplayereightsoup.text[-2:]
        try:
          awayplayereight = batter.objects.get(key_mlbam = awayplayereightkey_mlbam)
        except:
          awayplayereight = batter.objects.get(lastname = "dummy", firstname = "dummy")

        awayplayerninesoup = awaylineupsoup.select(".player")[8]
        awayplayerninekey_mlbam = awayplayerninesoup.find("a")["data-mlb"]
        awaypositions_import += awayplayerninesoup.text[-2:]
        try:
          awayplayernine = batter.objects.get(key_mlbam = awayplayerninekey_mlbam)
        except:
          awayplayernine = batter.objects.get(lastname = "dummy", firstname = "dummy")

        # get all 9 batters for each side, home second
        homeplayeronesoup = homelineupsoup.select(".player")[0]
        homeplayeronekey_mlbam = homeplayeronesoup.find("a")["data-mlb"]
        homepositions_import += homeplayeronesoup.text[-2:] # the catcher takes two spots with one being an empty space, which makes future code EASIER so leave it be
        try:
          homeplayerone = batter.objects.get(key_mlbam = homeplayeronekey_mlbam)
        except:
          homeplayerone = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayertwosoup = homelineupsoup.select(".player")[1]
        homeplayertwokey_mlbam = homeplayertwosoup.find("a")["data-mlb"]
        homepositions_import += homeplayertwosoup.text[-2:]
        try:
          homeplayertwo = batter.objects.get(key_mlbam = homeplayertwokey_mlbam)
        except:
          homeplayertwo = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayerthreesoup = homelineupsoup.select(".player")[2]
        homeplayerthreekey_mlbam = homeplayerthreesoup.find("a")["data-mlb"]
        homepositions_import += homeplayerthreesoup.text[-2:]
        try:
          homeplayerthree = batter.objects.get(key_mlbam = homeplayerthreekey_mlbam)
        except:
          homeplayerthree = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayerfoursoup = homelineupsoup.select(".player")[3]
        homeplayerfourkey_mlbam = homeplayerfoursoup.find("a")["data-mlb"]
        homepositions_import += homeplayerfoursoup.text[-2:]
        #print(homeplayerfourkey_mlbam)
        try:
          homeplayerfour = batter.objects.get(key_mlbam = homeplayerfourkey_mlbam)
        except:
          homeplayerfour = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayerfivesoup = homelineupsoup.select(".player")[4]
        homeplayerfivekey_mlbam = homeplayerfivesoup.find("a")["data-mlb"]
        homepositions_import += homeplayerfivesoup.text[-2:]
        try:
          homeplayerfive = batter.objects.get(key_mlbam = homeplayerfivekey_mlbam)
        except:
          homeplayerfive = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayersixsoup = homelineupsoup.select(".player")[5]
        homeplayersixkey_mlbam = homeplayersixsoup.find("a")["data-mlb"]
        homepositions_import += homeplayersixsoup.text[-2:]
        try:
          homeplayersix = batter.objects.get(key_mlbam = homeplayersixkey_mlbam)
        except:
          homeplayersix = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayersevensoup = homelineupsoup.select(".player")[6]
        homeplayersevenkey_mlbam = homeplayersevensoup.find("a")["data-mlb"]
        homepositions_import += homeplayersevensoup.text[-2:]
        try:
          homeplayerseven = batter.objects.get(key_mlbam = homeplayersevenkey_mlbam)
        except:
          homeplayerseven = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayereightsoup = homelineupsoup.select(".player")[7]
        homeplayereightkey_mlbam = homeplayereightsoup.find("a")["data-mlb"]
        homepositions_import += homeplayereightsoup.text[-2:]
        try:
          homeplayereight = batter.objects.get(key_mlbam = homeplayereightkey_mlbam)
        except:
          homeplayereight = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        homeplayerninesoup = homelineupsoup.select(".player")[8]
        homeplayerninekey_mlbam = homeplayerninesoup.find("a")["data-mlb"]
        homepositions_import += homeplayerninesoup.text[-2:]
        try:
          homeplayernine = batter.objects.get(key_mlbam = homeplayerninekey_mlbam)
        except:
          homeplayernine = batter.objects.get(lastname = "dummy", firstname = "dummy")

        #delete a matchup if it was delayed, because that means it will otherwise show up as a duplicate. use starting pitchers as a guide
        #fixes the issue of if baseball press does not announce the word delay with the game; just test two games with identical pitcher matchup but different start times and get one of them to delete
        if matchup.objects.filter(awayteam = awayteam_import, awaypitcher = awaypitcher_using_mlbamid, homepitcher = homepitcher_using_mlbamid).exclude(gametime = gametime_import).exists():
          # print("matchup exists")
          matchup.objects.filter(awayteam = awayteam_import, awaypitcher = awaypitcher_using_mlbamid, homepitcher = homepitcher_using_mlbamid).exclude(gametime = gametime_import).delete()

        #I also need to fix if a gamestart time was changed by like five minutes, and the lineup was not yet loaded so that didn't help anything. not sure how to do this though in an elegent fashion


        #create the matchup
        new_matchup = matchup(
          awaylineupposted = awaylineupposted_import,
          homelineupposted = homelineupposted_import,
          gametime = gametime_import,
          gamedate = gamedate_import,
          doubleheadergametwo = doubleheadergametwo_import,
          awaypositions = awaypositions_import,
          homepositions = homepositions_import,
          awayteam = awayteam_import,
          hometeam = hometeam_import,
          awaypitcher = awaypitcher_using_mlbamid,
          homepitcher = homepitcher_using_mlbamid,
          awaybatterone = awayplayerone,
          awaybattertwo = awayplayertwo,
          awaybatterthree = awayplayerthree,
          awaybatterfour = awayplayerfour,
          awaybatterfive = awayplayerfive,
          awaybattersix = awayplayersix,
          awaybatterseven = awayplayerseven,
          awaybattereight = awayplayereight,
          awaybatternine = awayplayernine,
          homebatterone = homeplayerone,
          homebattertwo = homeplayertwo,
          homebatterthree = homeplayerthree,
          homebatterfour = homeplayerfour,
          homebatterfive = homeplayerfive,
          homebattersix = homeplayersix,
          homebatterseven = homeplayerseven,
          homebattereight = homeplayereight,
          homebatternine = homeplayernine,
          gametimetemp = gametimetemp_import,
          chanceofrain = chanceofrain_import
        )

        new_matchup.save()

      # if at least one of the lineups was not loaded
      else:
        new_matchup = matchup(
          awaylineupposted = awaylineupposted_import,
          homelineupposted = homelineupposted_import,
          gametime = gametime_import,
          gamedate = gamedate_import,
          doubleheadergametwo = doubleheadergametwo_import,
          awayteam = awayteam_import,
          hometeam = hometeam_import,
          gametimetemp = gametimetemp_import,
          chanceofrain = chanceofrain_import
        )
        new_matchup.save()