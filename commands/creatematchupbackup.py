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
from bs4 import BeautifulSoup
from app_bb.baseball_functions import three_letter

class Command(BaseCommand):
  def handle(self, *args, **options):
    #test 1 -passed
    #result = requests.get("https://web.archive.org/web/20220618162717/https://www.mlb.com/starting-lineups")
    #result = requests.get("https://web.archive.org/web/20220618231629/https://www.mlb.com/starting-lineups")
    #result = requests.get("https://web.archive.org/web/20220619002123/https://www.mlb.com/starting-lineups")
    # test 2 : missed the houstan game bc it was final from the start, no worries becausae in real life that would never happen - ptherwise pass
    #result = requests.get("https://web.archive.org/web/20220807202803/https://www.mlb.com/starting-lineups")
    #result = requests.get("https://web.archive.org/web/20220807232129/https://www.mlb.com/starting-lineups")
    # test 3 - interaction with main baseballpress scraper, does not necessarily have to pass
    # PLACED IN creatematchup result = requests.get("https://web.archive.org/web/20220803162051/https://www.baseballpress.com/lineups?q=%2Flineups")
    result = requests.get("https://web.archive.org/web/20220803181617/https://www.mlb.com/starting-lineups")
    soup = BeautifulSoup(result.text, "lxml")

    gamedate_import = soup.find(class_ = "starting-lineups__date-title--current").text.split(',')[0].replace("th", "")
    #print(gamedate_import)
    games = soup.find_all(class_="starting-lineups__matchup")

    for game in games:
      # Find the start time of the game
      gametime_import = game.find(class_ = "starting-lineups__game-date-time").text.replace(" ", "").replace('\n',"").lower()
      print(gametime_import[:3])
      if gametime_import[:3] == "war":
        #game is in warmups
        gametime_import = "Warmups"
      if gametime_import == "tbd":
        gametime_import = "TBD"
      #print(gametime_import)
      # Find the home and away team names
      teams = game.find_all(class_ = "starting-lineups__team-name--link")
      hometeam_import = teams[1].text.replace("\n","").lower().replace(" ", "")
      awayteam_import = teams[0].text.replace("\n","").lower().replace(" ", "")
      awayteam_import = three_letter(awayteam_import)
      hometeam_import = three_letter(hometeam_import)
      
      #print(awayteam_import)
      #print(hometeam_import)
      awayteam_import = team.objects.get(name = awayteam_import)
      hometeam_import = team.objects.get(name = hometeam_import)
      
      awaypitcherloaded = True
      homepitcherloaded = True
      #if the pitcher is TBD, call it unloaded
      pitchersnames = game.select(".starting-lineups__pitcher-name")
      if pitchersnames[0].text.replace(" ","").replace("\n","") == "TBD":
        awaypitcherloaded = False
        #print(awaypitcherloaded)
        print(awayteam_import)
      if pitchersnames[1].text.replace(" ","").replace("\n","") == "TBD":
        homepitcherloaded = False
        print(hometeam_import)
      pitchers = game.select(".starting-lineups__pitcher--link")
      if awaypitcherloaded == True:
        awaypitchermlbamid = pitchers[0]['href'][-6:]
        print(awaypitchermlbamid)
      if homepitcherloaded == True:
        homepitchermlbamid = pitchers[-1]['href'][-6:]
        print(homepitchermlbamid)

      #check if lineups are loaded
      away_loaded_lineups = game.find_all(class_ = "starting-lineups__team--away")
      if away_loaded_lineups[0].text.replace("\n", "") == "TBD":
        awaylineupposted_import = False
      else:
        awaylineupposted_import = True
      #print(awaylineupposted_import)

      home_loaded_lineups = game.find_all(class_ = "starting-lineups__team--home")
      if home_loaded_lineups[0].text.replace("\n", "") == "TBD":
        homelineupposted_import = False
      else:
        homelineupposted_import = True
      #print(homelineupposted_import)

      #delete old version of the matchup if matchup still has not entered into warmups
      if matchup.objects.filter(awayteam = awayteam_import, gametime = gametime_import).exists():
        matchup.objects.filter(awayteam = awayteam_import, gametime = gametime_import).delete()

      if awaypitcherloaded == False:
        awaylineupposted_import = False
      if homepitcherloaded == False:
        homelineupposted_import = False

      #access the pitchers
      if awaypitcherloaded:
        try:
          awaypitcher_using_mlbamid = pitcher.objects.get(key_mlbam = awaypitchermlbamid)
        except:
          awaypitcher_using_mlbamid = pitcher.objects.get(lastname = "dummy", firstname = "dummy") # to be replaced by dummy pitcher
      if homepitcherloaded:
        try:
          homepitcher_using_mlbamid = pitcher.objects.get(key_mlbam = homepitchermlbamid)
        except:
          homepitcher_using_mlbamid = pitcher.objects.get(lastname = "dummy", firstname = "dummy") # to be replaced by dummy pitcher

      #delete old version of the matchup if matchup has entered into warmups or has ended
      print(awayteam_import)
      print(hometeam_import)
      print(awaypitchermlbamid)
      print(gametime_import)
      if (gametime_import == "Warmups" or gametime_import == "final") and matchup.objects.filter(awayteam = awayteam_import, hometeam = hometeam_import, awaypitcher = awaypitcher_using_mlbamid).exists():
        print("deleting matchup in warmups or final")
        gametime_import = matchup.objects.get(awayteam = awayteam_import, hometeam = hometeam_import, awaypitcher = awaypitcher_using_mlbamid).gametime
        matchup.objects.filter(awayteam = awayteam_import, hometeam = hometeam_import, awaypitcher = awaypitcher_using_mlbamid).delete()

      #code here that will handle what happens when the game is delayed (see original script)
      #still must handle the case where the game is delayed, but need to wait until season starts and I see what the page looks like

      #handle doubleheaders
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

        #away lineup
        awaylineup = game.find(class_ = "starting-lineups__team--away")
        awaypositions_import = ''
        #righty/lefty/switch-hit
        away_rls = ''
        char1 = '('
        char2 = ')'
        away_players = awaylineup.find_all(class_ = "starting-lineups__player--link")
        awayplayerkey_mlbam_list = []
        for away_player in away_players:
          awayplayerkey_mlbam_list.append(away_player['href'][-6:])

        away_players_positions = awaylineup.find_all(class_ = "starting-lineups__player--position")
        for away_player in away_players_positions:
          awaypositions_import += away_player.text[-2:]
          away_rls += away_player.text[away_player.text.find(char1)+1 : away_player.text.find(char2)]
        #print(awaypositions_import)
        #print(away_rls)

        #home lineup
        homelineup = game.find(class_ = "starting-lineups__team--home")
        homepositions_import = ''
        #righty/lefty/switch-hit
        home_rls = ''
        home_players = homelineup.find_all(class_ = "starting-lineups__player--link")
        homeplayerkey_mlbam_list = []
        for home_player in home_players:
          homeplayerkey_mlbam_list.append(home_player['href'][-6:])
    
        home_players_positions = homelineup.find_all(class_ = "starting-lineups__player--position")
        for home_player in home_players_positions:
          homepositions_import += home_player.text[-2:]
          home_rls += home_player.text[home_player.text.find(char1)+1 : home_player.text.find(char2)]
        #print(homepositions_import)
        #print(home_rls)

        #gather the away batters
        awayplayeronekey_mlbam = awayplayerkey_mlbam_list[0]
        awayplayertwokey_mlbam = awayplayerkey_mlbam_list[1]
        awayplayerthreekey_mlbam = awayplayerkey_mlbam_list[2]
        awayplayerfourkey_mlbam = awayplayerkey_mlbam_list[3]
        awayplayerfivekey_mlbam = awayplayerkey_mlbam_list[4]
        awayplayersixkey_mlbam = awayplayerkey_mlbam_list[5]
        awayplayersevenkey_mlbam = awayplayerkey_mlbam_list[6]
        awayplayereightkey_mlbam = awayplayerkey_mlbam_list[7]
        awayplayerninekey_mlbam = awayplayerkey_mlbam_list[8]

        #gather the home batters
        homeplayeronekey_mlbam = homeplayerkey_mlbam_list[0]
        homeplayertwokey_mlbam = homeplayerkey_mlbam_list[1]
        homeplayerthreekey_mlbam = homeplayerkey_mlbam_list[2]
        homeplayerfourkey_mlbam = homeplayerkey_mlbam_list[3]
        homeplayerfivekey_mlbam = homeplayerkey_mlbam_list[4]
        homeplayersixkey_mlbam = homeplayerkey_mlbam_list[5]
        homeplayersevenkey_mlbam = homeplayerkey_mlbam_list[6]
        homeplayereightkey_mlbam = homeplayerkey_mlbam_list[7]
        homeplayerninekey_mlbam = homeplayerkey_mlbam_list[8]

        try:
          awayplayerone = batter.objects.get(key_mlbam = awayplayeronekey_mlbam)
        except:
          awayplayerone = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayertwo = batter.objects.get(key_mlbam = awayplayertwokey_mlbam)
        except:
          awayplayertwo = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayerthree = batter.objects.get(key_mlbam = awayplayerthreekey_mlbam)
        except:
          awayplayerthree = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayerfour = batter.objects.get(key_mlbam = awayplayerfourkey_mlbam)
        except:
          awayplayerfour = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayerfive = batter.objects.get(key_mlbam = awayplayerfivekey_mlbam)
        except:
          awayplayerfive = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayersix = batter.objects.get(key_mlbam = awayplayersixkey_mlbam)
        except:
          awayplayersix = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayerseven = batter.objects.get(key_mlbam = awayplayersevenkey_mlbam)
        except:
          awayplayerseven = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayereight = batter.objects.get(key_mlbam = awayplayereightkey_mlbam)
        except:
          awayplayereight = batter.objects.get(lastname = "dummy", firstname = "dummy")

        try:
          awayplayernine = batter.objects.get(key_mlbam = awayplayerninekey_mlbam)
        except:
          awayplayernine = batter.objects.get(lastname = "dummy", firstname = "dummy")


        #gather the home batters
        try:
         homeplayerone = batter.objects.get(key_mlbam = homeplayeronekey_mlbam)
        except:
          homeplayerone = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayertwo = batter.objects.get(key_mlbam = homeplayertwokey_mlbam)
        except:
          homeplayertwo = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayerthree = batter.objects.get(key_mlbam = homeplayerthreekey_mlbam)
        except:
          homeplayerthree = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayerfour = batter.objects.get(key_mlbam = homeplayerfourkey_mlbam)
        except:
          homeplayerfour = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayerfive = batter.objects.get(key_mlbam = homeplayerfivekey_mlbam)
        except:
          homeplayerfive = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayersix = batter.objects.get(key_mlbam = homeplayersixkey_mlbam)
        except:
          homeplayersix = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayerseven = batter.objects.get(key_mlbam = homeplayersevenkey_mlbam)
        except:
          homeplayerseven = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayereight = batter.objects.get(key_mlbam = homeplayereightkey_mlbam)
        except:
          homeplayereight = batter.objects.get(lastname = "dummy", firstname = "dummy")
  
        try:
          homeplayernine = batter.objects.get(key_mlbam = homeplayerninekey_mlbam)
        except:
          homeplayernine = batter.objects.get(lastname = "dummy", firstname = "dummy")


        #delete a matchup if it was delayed, because that means it will otherwise show up as a duplicate. use starting pitchers as a guide
        if matchup.objects.filter(awayteam = awayteam_import, awaypitcher = awaypitcher_using_mlbamid, homepitcher = homepitcher_using_mlbamid).exclude(gametime = gametime_import).exists():
          # print("matchup exists")
          matchup.objects.filter(awayteam = awayteam_import, awaypitcher = awaypitcher_using_mlbamid, homepitcher = homepitcher_using_mlbamid).exclude(gametime = gametime_import).delete()

      #missing gametimetemp and chanceofrain
      #can add rls in the future
        #create the matchup
        print("creating matchup")
        print(awaypitcher_using_mlbamid)
        print(awayplayerthree)
        print(homeplayerthree)
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
        )

        new_matchup.save()

      elif awaypitcherloaded and homepitcherloaded:
        new_matchup = matchup(
          awaylineupposted = awaylineupposted_import,
          homelineupposted = homelineupposted_import,
          awaypitcher = awaypitcher_using_mlbamid,
          homepitcher = homepitcher_using_mlbamid,
          gametime = gametime_import,
          gamedate = gamedate_import,
          doubleheadergametwo = doubleheadergametwo_import,
          awayteam = awayteam_import,
          hometeam = hometeam_import,
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
        )
        new_matchup.save()

      


    

  # def three_letter(self, team_import):
  #   #fix the team names to the standard three-letter system
  #   #fix the team names to the standard three-letter system
  #   if team_import == "marlins":
  #    team_import = "mia"
  #   if team_import == "phillies":
  #     team_import = "phi"
  #   if team_import == "white sox" or team_import == "whitesox":
  #     team_import = "chw"
  #   if team_import == "tigers":
  #     team_import = "det"
  #   if team_import == "astros":
  #     team_import = "hou"
  #   if team_import == "rangers":
  #     team_import = "tex"
  #   if team_import == "reds":
  #     team_import = "cin"
  #   if team_import == "diamondbacks" or team_import == "d-backs":
  #     team_import = "ari"
  #   if team_import == "royals":
  #     team_import = "kcr"
  #   if team_import == "giants":
  #     team_import = "sfg"
  #   if team_import == "twins":
  #     team_import = "min"
  #   if team_import == "mariners":
  #     team_import = "sea"
  #   if team_import == "braves":
  #     team_import = "atl"
  #   if team_import == "nationals":
  #     team_import = "wsn"
  #   if team_import == "rays":
  #     team_import = "tbr"
  #   if team_import == "yankees":
  #     team_import = "nyy"
  #   if team_import == "orioles":
  #     team_import = "bal"
  #   if team_import == "blue jays" or team_import == "bluejays":
  #     team_import = "tor"
  #   if team_import == "athletics":
  #     team_import = "oak"
  #   if team_import == "red sox" or team_import == "redsox":
  #     team_import = "bos"
  #   if team_import == "brewers":
  #     team_import = "mil"
  #   if team_import == "mets":
  #     team_import = "nym"
  #   if team_import == "pirates":
  #     team_import = "pit"
  #   if team_import == "cardinals":
  #     team_import = "stl"
  #   if team_import == "padres":
  #     team_import = "sdp"
  #   if team_import == "cubs":
  #     team_import = "chc"
  #   if team_import == "guardians" or team_import == "indians":
  #     team_import = "cle"
  #   if team_import == "rockies":
  #     team_import = "col"
  #   if team_import == "angels":
  #     team_import = "laa"
  #   if team_import == "dodgers":
  #     team_import = "lad"
  #   return team_import