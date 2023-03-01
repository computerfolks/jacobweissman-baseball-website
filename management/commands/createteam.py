import decimal
from django.core.management.base import BaseCommand
from app_bb.models import team
from pybaseball import *
from pybaseball import schedule_and_record
import numpy as np
import matplotlib.pylab as plt
import mailcap
import requests
import bs4

# also throw in team record if you want, would need to be independently scraped

class Command(BaseCommand):
  def handle(self, *args, **options):
    # every time this script runs, it should delete whatever was previously in the matchup database
    # note: running this script will delete all the matchups, and anyways it has no reason to run more than once a day
    try:
      entries = team.objects.all()
      entries.delete()
    except:
      pass
    #standard stats
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=0&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular")
      name_import = statcolumnworksheet[1].text.lower()
      winningpercentbp_import = float(statcolumnworksheet[2].text) / (float(statcolumnworksheet[2].text) + float(statcolumnworksheet[3].text))
      erabp_import = float(statcolumnworksheet[4].text)
      savesbp_import = float(statcolumnworksheet[9].text)
      savepercentbp_import = savesbp_import / (savesbp_import + float(statcolumnworksheet[11].text))
      inningsbp_import = float(statcolumnworksheet[12].text)
      if inningsbp_import % 1 < 0.11 and inningsbp_import % 1 > 0.09:
        inningsbp_import = inningsbp_import + .23
      elif inningsbp_import % 1 < 0.21 and inningsbp_import % 1 > 0.19:
        inningsbp_import = inningsbp_import + .47
      battersfacedbp_import = float(statcolumnworksheet[13].text)
      hitsbp_import = float(statcolumnworksheet[14].text)
      hitsperninebp_import = hitsbp_import * 9 / inningsbp_import
      runsbp_import = float(statcolumnworksheet[15].text)
      runsaveragebp_import = float(runsbp_import) * 9 / float(inningsbp_import)
      bbhbpbp_import = float(statcolumnworksheet[18].text) + float(statcolumnworksheet[20].text)
      homerunsbp_import = float(statcolumnworksheet[17].text)
      kbp_import = float(statcolumnworksheet[23].text)
      new_team = team(
        name = name_import,
        winningpercentbp = winningpercentbp_import,
        erabp = erabp_import,
        savesbp = savesbp_import,
        savepercentbp = savepercentbp_import,
        inningsbp = inningsbp_import,
        battersfacedbp = battersfacedbp_import,
        hitsbp = hitsbp_import,
        hitsperninebp = hitsperninebp_import,
        runsbp = runsbp_import,
        runsaveragebp = runsaveragebp_import,
        bbhbpbp = bbhbpbp_import,
        homerunsbp = homerunsbp_import,
        kbp = kbp_import
      )
      new_team.save()
    
    #advanced stats
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=1&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      kperninebp_import = float(statcolumnworksheet[2].text)
      bbperninebp_import = float(statcolumnworksheet[3].text)
      kperbbbp_import = float(statcolumnworksheet[4].text)
      hrperninebp_import = float(statcolumnworksheet[5].text)
      kpercentbp_import = float(statcolumnworksheet[6].text.replace("%",""))/100
      bbpercentbp_import = float(statcolumnworksheet[7].text.replace("%",""))/100
      kpercentminusbbpercentbp_import = float(statcolumnworksheet[8].text.replace("%",""))/100
      avgbp_import = float(statcolumnworksheet[9].text)
      whipbp_import = float(statcolumnworksheet[10].text)
      babipbp_import = float(statcolumnworksheet[11].text)
      lobpercentbp_import = float(statcolumnworksheet[12].text.replace("%",""))/100
      eraminusbp_import = float(statcolumnworksheet[13].text)
      fipminusbp_import = float(statcolumnworksheet[14].text)
      xfipminusbp_import = float(statcolumnworksheet[15].text)
      fipbp_import = float(statcolumnworksheet[17].text)
      xfipbp_import = float(statcolumnworksheet[19].text)
      sierabp_import = float(statcolumnworksheet[20].text) 
      update_team = team.objects.get(name = name_import)
      update_team.kperninebp = kperninebp_import
      update_team.bbperninebp = bbperninebp_import
      update_team.kperbbbp = kperbbbp_import
      update_team.hrperninebp = hrperninebp_import
      update_team.kpercentbp = kpercentbp_import
      update_team.bbpercentbp = bbpercentbp_import
      update_team.kpercentminusbbpercentbp = kpercentminusbbpercentbp_import
      update_team.avgbp = avgbp_import
      update_team.whipbp = whipbp_import
      update_team.babipbp = babipbp_import
      update_team.lobpercentbp = lobpercentbp_import
      update_team.eraminusbp = eraminusbp_import
      update_team.fipminusbp = fipminusbp_import
      update_team.xfipminusbp = xfipminusbp_import
      update_team.fipbp = fipbp_import
      update_team.xfipbp = xfipbp_import
      update_team.sierabp = sierabp_import
      update_team.save()

    # batted ball
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=2&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      gbperfbbp_import = float(statcolumnworksheet[3].text)
      gbpercentbp_import = float(statcolumnworksheet[5].text.replace("%",""))/100
      ldpercentbp_import = float(statcolumnworksheet[4].text.replace("%",""))/100
      fbpercentbp_import = float(statcolumnworksheet[6].text.replace("%",""))/100
      iffbpercentbp_import = float(statcolumnworksheet[7].text.replace("%",""))/100
      thrownforkpercentbp_import = float(statcolumnworksheet[12].text) / float(statcolumnworksheet[13].text)
      hrperfbpercent_import = float(statcolumnworksheet[8].text.replace("%",""))/100
      softpercentbp_import = float(statcolumnworksheet[17].text.replace("%",""))/100
      mediumpercentbp_import = float(statcolumnworksheet[18].text.replace("%",""))/100
      softplusmediumpercentbp_import = softpercentbp_import + mediumpercentbp_import
      #weakpercentbp_import = float(statcolumnworksheet[12].text.replace("%",""))/100 too lazy to compute right now
      update_team = team.objects.get(name = name_import)
      update_team.gbperfbbp = gbperfbbp_import
      update_team.gbpercentbp = gbpercentbp_import
      update_team.ldpercentbp = ldpercentbp_import
      update_team.fbpercentbp = fbpercentbp_import
      update_team.iffbpercentbp = iffbpercentbp_import
      update_team.thrownforkpercentbp = thrownforkpercentbp_import
      update_team.hrperfbpercent = hrperfbpercent_import
      update_team.softpercentbp = softpercentbp_import
      update_team.mediumpercentbp = mediumpercentbp_import
      update_team.softplusmediumpercentbp = softplusmediumpercentbp_import
      update_team.save()

    # win probability
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=3&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      wpabp_import = float(statcolumnworksheet[2].text)
      retwentyfourbp_import = float(statcolumnworksheet[5].text)
      clutchbp_import = float(statcolumnworksheet[13].text)
      shutdownbp_import = float(statcolumnworksheet[14].text)
      meltdownbp_import = float(statcolumnworksheet[15].text)
      if meltdownbp_import != 0:
        shutdownpermeltdownbp_import = shutdownbp_import / meltdownbp_import
      else:
        shutdownpermeltdownbp_import = 0
      update_team = team.objects.get(name = name_import)
      update_team.wpabp = wpabp_import
      update_team.retwentyfourbp = retwentyfourbp_import
      update_team.clutchbp = clutchbp_import
      update_team.shutdownbp = shutdownbp_import
      update_team.meltdownbp = meltdownbp_import
      update_team.shutdownpermeltdownbp = shutdownpermeltdownbp_import
      update_team.save()

    #plate discipline
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=5&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      outsidezoneswingpercentbp_import = float(statcolumnworksheet[2].text.replace("%",""))/100
      firstpitchstrikepercentbp_import = float(statcolumnworksheet[9].text.replace("%",""))/100
      swingingstrikespercentbp_import = float(statcolumnworksheet[10].text.replace("%",""))/100
      cswpercentbp_import = float(statcolumnworksheet[12].text.replace("%",""))/100
      update_team = team.objects.get(name = name_import)
      update_team.outsidezoneswingpercentbp = outsidezoneswingpercentbp_import
      update_team.firstpitchstrikepercentbp = firstpitchstrikepercentbp_import
      update_team.swingingstrikespercentbp = swingingstrikespercentbp_import
      update_team.cswpercentbp = cswpercentbp_import
      update_team.save()

    #value
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=6&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      rarbp_import = float(statcolumnworksheet[6].text)
      warbp_import = float(statcolumnworksheet[7].text)
      update_team = team.objects.get(name = name_import)
      update_team.rarbp = rarbp_import
      update_team.warbp = warbp_import
      update_team.save()

    #plus
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=23&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      plus_k_per_ninebp_import = float(statcolumnworksheet[3].text)
      plus_bb_per_ninebp_import = float(statcolumnworksheet[4].text)
      plus_k_per_bbbp_import = float(statcolumnworksheet[5].text)
      plus_hr_per_ninebp_import = float(statcolumnworksheet[6].text)
      plus_avgbp_import = float(statcolumnworksheet[9].text)
      plus_whipbp_import = float(statcolumnworksheet[10].text)
      plus_babipbp_import = float(statcolumnworksheet[11].text)
      plus_lobpercentbp_import = float(statcolumnworksheet[12].text)
      plus_kpercentbp_import = float(statcolumnworksheet[7].text)
      plus_bbpercentbp_import = float(statcolumnworksheet[8].text)
      plus_ldpercentbp_import = float(statcolumnworksheet[16].text)
      plus_gbpercentbp_import = float(statcolumnworksheet[17].text)
      update_team = team.objects.get(name = name_import)
      update_team.plus_k_per_ninebp = plus_k_per_ninebp_import
      update_team.plus_bb_per_ninebp = plus_bb_per_ninebp_import
      update_team.plus_k_per_bbbp = plus_k_per_bbbp_import
      update_team.plus_hr_per_ninebp = plus_hr_per_ninebp_import
      update_team.plus_avgbp = plus_avgbp_import
      update_team.plus_whipbp = plus_whipbp_import
      update_team.plus_babipbp = plus_babipbp_import
      update_team.plus_lobpercentbp = plus_lobpercentbp_import
      update_team.plus_kpercentbp = plus_kpercentbp_import
      update_team.plus_bbpercentbp = plus_bbpercentbp_import
      update_team.plus_ldpercentbp = plus_ldpercentbp_import
      update_team.plus_gbpercentbp = plus_gbpercentbp_import
      update_team.save()
    
    #statcast new
    result = requests.get("https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=24&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    rowsworksheet = soup.select(".rgRow, .rgAltRow")
    for row in range(30):
      statcolumnworksheet = rowsworksheet[row].select(".grid_line_regular, .grid_line_break")
      name_import = statcolumnworksheet[1].text.lower()
      bbeeventsbp_import = float(statcolumnworksheet[3].text)
      barrel_percentbp_import = float(statcolumnworksheet[8].text.replace("%",""))/100
      hardhitpercentbp_import = float(statcolumnworksheet[10].text.replace("%",""))/100
      averageevbp_import = float(statcolumnworksheet[4].text)
      averagelabp_import = float(statcolumnworksheet[6].text)
      update_team = team.objects.get(name = name_import)
      update_team.bbeeventsbp = bbeeventsbp_import
      update_team.barrel_percentbp = barrel_percentbp_import
      update_team.hardhitpercentbp = hardhitpercentbp_import
      update_team.averageevbp = averageevbp_import
      update_team.averagelabp = averagelabp_import
      update_team.brl_per_pabp = decimal.Decimal(float(statcolumnworksheet[7].text)) / update_team.battersfacedbp
      update_team.save()

    #baseball savant expected and barrel unavailable because there are no quick, easy ways to get the total reliever data

    #fangraph's fielding
    data = team_fielding(2022)
    for x in range(30):
      errors_import = float(data.iat[x,9])
      doubleplays_import = float(data.iat[x,12])
      fieldingpercentage_import = float(data.iat[x,21])
      sbagainst_import = float(data.iat[x,17])
      csagainst_import = float(data.iat[x,18])
      xsbsavedagainst_import = csagainst_import - sbagainst_import * 2
      wildpitchespluspassedballs_import = float(data.iat[x,19]) + float(data.iat[x,20])
      defensiverunssaved_import = float(data.iat[x,28])
      ultimatezonerating_import = float(data.iat[x,39])
      defense_import = float(data.iat[x,43])
      update_team_name = data.iat[x,2].lower()
      #fix the team names to the standard three-letter system, as well as add logos, team names, and cities
      if update_team_name == "marlins":
        update_team_name = "mia"
        logopath_import = "logos/miami-marlins-logo-transparent.png"
        update_team_city = "Miami"
        update_team_fullname = "Marlins"
      if update_team_name == "phillies":
        update_team_name = "phi"
        logopath_import = "logos/philadelphia-phillies-logo-transparent.png"
        update_team_city = "Philadelphia"
        update_team_fullname = "Phillies"
      if update_team_name == "white sox":
        update_team_name = "chw"
        logopath_import = "logos/chicago-white-sox-logo-transparent.png"
        update_team_city = "Chicago AL"
        update_team_fullname = "White Sox"
      if update_team_name == "tigers":
        update_team_name = "det"
        logopath_import = "logos/detroit-tigers-logo-transparent.png"
        update_team_city = "Detroit"
        update_team_fullname = "Tigers"
      if update_team_name == "astros":
        update_team_name = "hou"
        logopath_import = "logos/houston-astros-logo-transparent.png"
        update_team_city = "Houston"
        update_team_fullname = "Astros"
      if update_team_name == "rangers":
        update_team_name = "tex"
        logopath_import = "logos/texas-rangers-logo-transparent.png"
        update_team_city = "Texas"
        update_team_fullname = "Rangers"
      if update_team_name == "reds":
        update_team_name = "cin"
        logopath_import = "logos/cincinnati-reds-logo-transparent.png"
        update_team_city = "Cincinnati"
        update_team_fullname = "Reds"
      if update_team_name == "diamondbacks":
        update_team_name = "ari"
        logopath_import = "logos/arizona-diamondbacks-snake-logo-transparent.png"
        update_team_city = "Arizona"
        update_team_fullname = "Diamondbacks"
      if update_team_name == "royals":
        update_team_name = "kcr"
        logopath_import = "logos/kansas-city-royals-logo-transparent.png"
        update_team_city = "Kansas City"
        update_team_fullname = "Royals"
      if update_team_name == "giants":
        update_team_name = "sfg"
        logopath_import = "logos/san-francisco-giants-logo-transparent.png"
        update_team_city = "San Francisco"
        update_team_fullname = "Giants"
      if update_team_name == "twins":
        update_team_name = "min"
        logopath_import = "logos/minnesota-twins-logo-transparent.png"
        update_team_city = "Minnesota"
        update_team_fullname = "Twins"
      if update_team_name == "mariners":
        update_team_name = "sea"
        logopath_import = "logos/seattle-mariners-logo-transparent.png"
        update_team_city = "Seattle"
        update_team_fullname = "Mariners"
      if update_team_name == "braves":
        update_team_name = "atl"
        logopath_import = "logos/atlanta-braves-logo-transparent.png"
        update_team_city = "Atlanta"
        update_team_fullname = "Braves"
      if update_team_name == "nationals":
        update_team_name = "wsn"
        logopath_import = "logos/washington-nationals-logo-transparent.png"
        update_team_city = "Washington"
        update_team_fullname = "Nationals"
      if update_team_name == "rays":
        update_team_name = "tbr"
        logopath_import = "logos/tampa-bay-rays-logo-transparent.png"
        update_team_city = "Tampa Bay"
        update_team_fullname = "Rays"
      if update_team_name == "yankees":
        update_team_name = "nyy"
        logopath_import = "logos/new-york-yankees-logo-transparent.png"
        update_team_city = "New York AL"
        update_team_fullname = "Yankees"
      if update_team_name == "orioles":
        update_team_name = "bal"
        logopath_import = "logos/baltimore-orioles-logo-transparent.png"
        update_team_city = "Baltimore"
        update_team_fullname = "Orioles"
      if update_team_name == "blue jays":
        update_team_name = "tor"
        logopath_import = "logos/toronto-blue-jays-logo-transparent.png"
        update_team_city = "Toronto"
        update_team_fullname = "Blue Jays"
      if update_team_name == "athletics":
        update_team_name = "oak"
        logopath_import = "logos/oakland-athletics-logo-transparent.png"
        update_team_city = "Oakland"
        update_team_fullname = "Atheltics"
      if update_team_name == "red sox":
        update_team_name = "bos"
        logopath_import = "logos/boston-red-sox-b-logo-cap-transparent.png"
        update_team_city = "Boston"
        update_team_fullname = "Red Sox"
      if update_team_name == "brewers":
        update_team_name = "mil"
        logopath_import = "logos/milwaukee-brewers-glove-logo.png"
        update_team_city = "Milwaukee"
        update_team_fullname = "Brewers"
      if update_team_name == "mets":
        update_team_name = "nym"
        logopath_import = "logos/new-york-mets-logo-transparent.png"
        update_team_city = "New York NL"
        update_team_fullname = "Mets"
      if update_team_name == "pirates":
        update_team_name = "pit"
        logopath_import = "logos/pittsburgh-pirates-logo-transparent.png"
        update_team_city = "Pittsburgh"
        update_team_fullname = "Pirates"
      if update_team_name == "cardinals":
        update_team_name = "stl"
        logopath_import = "logos/st-louis-cardinals-birds-on-bat-logo.png"
        update_team_city = "St. Louis"
        update_team_fullname = "Cardinals"
      if update_team_name == "padres":
        update_team_name = "sdp"
        logopath_import = "logos/san-diego-padres-logo-transparent.png"
        update_team_city = "San Diego"
        update_team_fullname = "Padres"
      if update_team_name == "cubs":
        update_team_name = "chc"
        logopath_import = "logos/chicago-cubs-logo-transparent.png"
        update_team_city = "Chicago NL"
        update_team_fullname = "Cubs"
      if update_team_name == "guardians":
        update_team_name = "cle"
        logopath_import = "logos/cleveland-indians-c-logo-transparent.png"
        update_team_city = "Cleveland"
        update_team_fullname = "Guardians"
      if update_team_name == "rockies":
        update_team_name = "col"
        logopath_import = "logos/colorado-rockies-logo-transparent.png"
        update_team_city = "Colorado"
        update_team_fullname = "Rockies"
      if update_team_name == "angels":
        update_team_name = "laa"
        logopath_import = "logos/los-angeles-angels-logo-transparent.png"
        update_team_city = "Los Angeles AL"
        update_team_fullname = "Angels"
      if update_team_name == "dodgers":
        update_team_name = "lad"
        logopath_import = "logos/los-angeles-dodgers-logo-transparent.png"
        update_team_city = "Los Angeles NL"
        update_team_fullname = "Dodgers"
      
      update_team = team.objects.get(name = update_team_name)
      update_team.errors = errors_import
      update_team.doubleplays = doubleplays_import
      update_team.fieldingpercentage = fieldingpercentage_import
      update_team.sbagainst = sbagainst_import
      update_team.csagainst = csagainst_import
      update_team.xsbsavedagainst = xsbsavedagainst_import
      update_team.wildpitchespluspassedballs = wildpitchespluspassedballs_import
      update_team.defensiverunssaved = defensiverunssaved_import
      update_team.ultimatezonerating = ultimatezonerating_import
      update_team.defense = defense_import
      update_team.logopath = logopath_import
      update_team.city = update_team_city
      update_team.fullname = update_team_fullname
      update_team.save()