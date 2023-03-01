from aifc import Error
import decimal
import math
from django.core.management.base import BaseCommand
from app_bb.models import pitcher
from pybaseball import *
import numpy as np
import matplotlib.pylab as plt
from pybaseball.statcast_pitcher import statcast_pitcher_exitvelo_barrels
from pybaseball.statcast_pitcher import statcast_pitcher_expected_stats

#takes 4:15 to run which basically renders it useless, you can just recreate the pitcher every day and write in a delete function at the start like you have with matchup and teams

class Command(BaseCommand):
  def handle(self, *args, **options):
    if pitcher.objects.filter(lastname = "dummy").exists():
      pitcher.objects.filter(lastname = "dummy").delete()
    #UPDATE FANGRAPHS
    data_2022 = pitching_stats(2022, qual = 5)
    number_of_players_2022 = data_2022.shape[0]
    for x in range(number_of_players_2022):
      full_name = data_2022.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
      firstname_import = full_name[0]
      lastname_import = full_name[1]
      teamname_import = data_2022.iat[x,3].replace(" ", "")
      fangraphs_id_import = data_2022.iat[x,0]
      if data_2022.iat[x,6] != 0:
        winningpercent_import = (float(data_2022.iat[x,5])) / (float(data_2022.iat[x,5])+ float(data_2022.iat[x,6]))
      war2022_import = data_2022.iat[x,7]

      era2022_import = float(data_2022.iat[x,8])
      shutouts2022_import = float(data_2022.iat[x,12])
      saves2022_import = float(data_2022.iat[x,13])
      if data_2022.iat[x,13] != 0:
        savepercent2022_import = (saves2022_import) / (saves2022_import + float(data_2022.iat[x,14]))
      else:
        savepercent2022_import = 0
      if data_2022.iat[x,15] % 1 < 0.11 and data_2022.iat[x,15] % 1 > 0.09:
        innings2022_import = float(data_2022.iat[x,15]) + .23
      elif data_2022.iat[x,15] % 1 < 0.21 and data_2022.iat[x,15] % 1 > 0.19:
        innings2022_import = float(data_2022.iat[x,15]) + .47
      else:
        innings2022_import = float(data_2022.iat[x,15])
      battersfaced2022_import = float(data_2022.iat[x,16])
      hits2022_import = float(data_2022.iat[x,17])
      runs2022_import = float(data_2022.iat[x,18])
      runsaverage2022_import = (runs2022_import * 9) / innings2022_import
      homeruns2022_import = float(data_2022.iat[x,20])
      bbhbp2022_import = float(data_2022.iat[x,21]) + float(data_2022.iat[x,23])
      k2022_import = float(data_2022.iat[x,26])
      thrownforkpercent2022_import = (float(data_2022.iat[x,32])) / float(data_2022.iat[x,33])
      kpernine2022_import = float(data_2022.iat[x,38])
      bbpernine2022_import = float(data_2022.iat[x,39]) 
      hitpernine2022_import = float(data_2022.iat[x,41])
      hrpernine2022_import = float(data_2022.iat[x,42])
      if (data_2022.iat[x,21] != 0):
        kperbb2022_import = float(data_2022.iat[x,40])
        plus_k_per_bb2022_import = float(data_2022.iat[x,304])
        loaded_k_per_bb2022_import = True
      else:
        kperbb2022_import = 0
        plus_k_per_bb2022_import = 0
        loaded_k_per_bb2022_import = False
      avg2022_import = data_2022.iat[x,43]
      whip2022_import = data_2022.iat[x,44]
      babip2022_import = data_2022.iat[x,45]
      lobpercent2022_import = data_2022.iat[x,46]
      if data_2022.iat[x,28] != 0:
        hrperfb2022_import = float(data_2022.iat[x,53])
        loaded_hrperfb2022_import = True
      else: 
        hrperfb2022_import = 0
        loaded_hrperfb2022_import = False
      fip2022_import = data_2022.iat[x,47]
      gbperfb2022_import = data_2022.iat[x,48]
      gbpercent2022_import = data_2022.iat[x,50]
      iffbpercent2022_import = data_2022.iat[x,52]
      ldpercent2022_import = data_2022.iat[x,49]
      fbpercent2022_import = data_2022.iat[x,51]
      rar2022_import = float(data_2022.iat[x,60])
      tera2022_import = data_2022.iat[x,62]
      xfip2022_import = data_2022.iat[x,63]
      wpa2022_import = float(data_2022.iat[x,64])
      retwentyfour2022_import = float(data_2022.iat[x,67])
      clutch2022_import = data_2022.iat[x,75]
      outsidezoneswingpercent2022_import = data_2022.iat[x,106]
      firstpitchstrikepercent2022_import = data_2022.iat[x,113]
      swingingstrikespercent2022_import = data_2022.iat[x,114]
      shutdowns2022_import = float(data_2022.iat[x,116])
      meltdowns2022_import = float(data_2022.iat[x,117])
      eraminus2022_import = float(data_2022.iat[x,118])
      fipminus2022_import = float(data_2022.iat[x,119])
      xfipminus2022_import = float(data_2022.iat[x,120])
      bbpercent2022_import = float(data_2022.iat[x,122])
      cswpercent2022_import = float(data_2022.iat[x,332])
      siera2022_import = data_2022.iat[x,123]
      softpercent2022_import = data_2022.iat[x,222]
      mediumpercent2022_import = data_2022.iat[x,223]
      softplusmediumpercent2022_import = data_2022.iat[x,222] + data_2022.iat[x,223]
      kwera2022_import = data_2022.iat[x,225]
      kpercent2022_import = data_2022.iat[x,121]
      weakpercent2022_import = kpercent2022_import + ((gbpercent2022_import + iffbpercent2022_import) * (1 - kpercent2022_import - bbpercent2022_import))
      plus_k_per_nine2022_import = float(data_2022.iat[x,302])
      plus_bb_per_nine2022_import = float(data_2022.iat[x,303])
      plus_h_per_nine2022_import = float(data_2022.iat[x,305])
      plus_hr_per_nine2022_import = float(data_2022.iat[x,306])
      plus_avg2022_import = float(data_2022.iat[x,307])
      plus_whip2022_import = float(data_2022.iat[x,308])
      plus_babip2022_import = float(data_2022.iat[x,309])
      plus_lobpercent2022_import = float(data_2022.iat[x,310])
      plus_kpercent2022_import = float(data_2022.iat[x,311])
      plus_bbpercent2022_import = float(data_2022.iat[x,312])
      plus_ldpercent2022_import = float(data_2022.iat[x,313])
      plus_gbpercent2022_import = float(data_2022.iat[x,314])
      plus_hrperfb2022_import = float(data_2022.iat[x,316])
      plus_softpercent2022_import = float(data_2022.iat[x,320])
      plus_mediumpercent2022_import = float(data_2022.iat[x,321])
      barrel_percent2022_import = data_2022.iat[x,326]
      hardhitpercent2022_import = data_2022.iat[x,329]
      averageev2022_import = float(data_2022.iat[x,323])
      averagela2022_import = data_2022.iat[x,324]
      xera2022_import = data_2022.iat[x,333]
      if math.isnan(xera2022_import):
        xera2022_import = era2022_import
      if pitcher.objects.filter(fangraphs_id = fangraphs_id_import).exists():
       update_pitcher = pitcher.objects.get(fangraphs_id = fangraphs_id_import)
       update_pitcher.loaded_2022 = True
       update_pitcher.loaded_hrperfb2022 = loaded_hrperfb2022_import
       update_pitcher.loaded_k_per_bb2022 = loaded_k_per_bb2022_import
       update_pitcher.winningpercent2022 = winningpercent_import
       update_pitcher.war2022 = war2022_import
       update_pitcher.era2022 = era2022_import
       update_pitcher.shutouts2022 = shutouts2022_import
       update_pitcher.saves2022 = saves2022_import
       update_pitcher.savepercent2022 = savepercent2022_import
       update_pitcher.innings2022 = innings2022_import
       update_pitcher.battersfaced2022 = battersfaced2022_import
       update_pitcher.hits2022 = hits2022_import
       update_pitcher.runs2022 = runs2022_import
       update_pitcher.runsaverage2022 = runsaverage2022_import
       update_pitcher.homeruns2022 = homeruns2022_import
       update_pitcher.bbhbp2022 = bbhbp2022_import
       update_pitcher.k2022 = k2022_import
       update_pitcher.thrownforkpercent2022 = thrownforkpercent2022_import
       update_pitcher.kpernine2022 = kpernine2022_import
       update_pitcher.bbpernine2022 = bbpernine2022_import
       update_pitcher.hitpernine2022 = hitpernine2022_import
       update_pitcher.hrpernine2022 = hrpernine2022_import
       update_pitcher.kperbb2022 = kperbb2022_import
       update_pitcher.avg2022 = avg2022_import
       update_pitcher.whip2022 = whip2022_import
       update_pitcher.babip2022 = babip2022_import
       update_pitcher.lobpercent2022 = lobpercent2022_import
       update_pitcher.hrperfb2022 = hrperfb2022_import
       update_pitcher.fip2022 = fip2022_import
       update_pitcher.gbperfb2022 = gbperfb2022_import
       update_pitcher.gbpercent2022 = gbpercent2022_import
       update_pitcher.iffbpercent2022 = iffbpercent2022_import
       update_pitcher.ldpercent2022 = ldpercent2022_import
       update_pitcher.fbpercent2022 = fbpercent2022_import
       update_pitcher.rar2022 = rar2022_import
       update_pitcher.tera2022 = tera2022_import
       update_pitcher.xfip2022 = xfip2022_import
       update_pitcher.wpa2022 = wpa2022_import
       update_pitcher.retwentyfour2022 = retwentyfour2022_import
       update_pitcher.clutch2022 = clutch2022_import
       update_pitcher.outsidezoneswingpercent2022 = outsidezoneswingpercent2022_import
       update_pitcher.firstpitchstrikepercent2022 = firstpitchstrikepercent2022_import
       update_pitcher.swingingstrikespercent2022 = swingingstrikespercent2022_import
       update_pitcher.shutdowns2022 = shutdowns2022_import
       update_pitcher.meltdowns2022 = meltdowns2022_import
       update_pitcher.eraminus2022 = eraminus2022_import
       update_pitcher.fipminus2022 = fipminus2022_import
       update_pitcher.xfipminus2022 = xfipminus2022_import
       update_pitcher.bbpercent2022 = bbpercent2022_import
       update_pitcher.cswpercent2022 = cswpercent2022_import
       update_pitcher.siera2022 = siera2022_import
       update_pitcher.softpercent2022 = softpercent2022_import
       update_pitcher.mediumpercent2022 = mediumpercent2022_import
       update_pitcher.softplusmediumpercent2022 = softplusmediumpercent2022_import
       update_pitcher.kwera2022 = kwera2022_import
       update_pitcher.kpercent2022 = kpercent2022_import
       update_pitcher.weakpercent2022 = weakpercent2022_import
       update_pitcher.plus_k_per_nine2022 = plus_k_per_nine2022_import
       update_pitcher.plus_bb_per_nine2022 = plus_bb_per_nine2022_import
       update_pitcher.plus_k_per_bb2022 = plus_k_per_bb2022_import
       update_pitcher.plus_h_per_nine2022 = plus_h_per_nine2022_import
       update_pitcher.plus_hr_per_nine2022 = plus_hr_per_nine2022_import
       update_pitcher.plus_avg2022 = plus_avg2022_import
       update_pitcher.plus_whip2022 = plus_whip2022_import
       update_pitcher.plus_babip2022 = plus_babip2022_import
       update_pitcher.plus_lobpercent2022 = plus_lobpercent2022_import
       update_pitcher.plus_kpercent2022 = plus_kpercent2022_import
       update_pitcher.plus_bbpercent2022 = plus_bbpercent2022_import
       update_pitcher.plus_ldpercent2022 = plus_ldpercent2022_import
       update_pitcher.plus_gbpercent2022 = plus_gbpercent2022_import
       update_pitcher.plus_hrperfb2022 = plus_hrperfb2022_import
       update_pitcher.plus_softpercent2022 = plus_softpercent2022_import
       update_pitcher.plus_mediumpercent2022 = plus_mediumpercent2022_import
       update_pitcher.barrel_percent2022 = barrel_percent2022_import
       update_pitcher.hardhitpercent2022 = hardhitpercent2022_import
       update_pitcher.averageev2022 = averageev2022_import
       update_pitcher.averagela2022 = averagela2022_import
       update_pitcher.xera2022 = xera2022_import
       update_pitcher.save()
      else:
       new_pitcher = pitcher(
         loaded_2022 = True,
         firstname = firstname_import,
         lastname = lastname_import,
         teamname = teamname_import,
         fangraphs_id = fangraphs_id_import,
         winningpercent2022 = winningpercent_import,
         war2022 = war2022_import,
         era2022 = era2022_import,
         shutouts2022 = shutouts2022_import,
         saves2022 = saves2022_import,
         savepercent2022 = savepercent2022_import,
         innings2022 = innings2022_import,
         battersfaced2022 = battersfaced2022_import,
         hits2022 = hits2022_import,
         runs2022 = runs2022_import,
         runsaverage2022 = runsaverage2022_import,
         homeruns2022 = homeruns2022_import,
         bbhbp2022 = bbhbp2022_import,
         k2022 = k2022_import,
         thrownforkpercent2022 = thrownforkpercent2022_import,
         loaded_k_per_bb2022 = loaded_k_per_bb2022_import,
         loaded_hrperfb2022 = loaded_hrperfb2022_import,
         kpernine2022 = kpernine2022_import,
         bbpernine2022 = bbpernine2022_import,
         hitpernine2022 = hitpernine2022_import,
         hrpernine2022 = hrpernine2022_import,
         kperbb2022 = kperbb2022_import,
         avg2022 = avg2022_import,
         whip2022 = whip2022_import,
         babip2022 = babip2022_import,
         lobpercent2022 = lobpercent2022_import,
         hrperfb2022 = hrperfb2022_import,
         fip2022 = fip2022_import,
         gbperfb2022 = gbperfb2022_import,
         gbpercent2022 = gbpercent2022_import,
         iffbpercent2022 = iffbpercent2022_import,
         ldpercent2022 = ldpercent2022_import,
         fbpercent2022 = fbpercent2022_import,
         rar2022 = rar2022_import,
         tera2022 = tera2022_import,
         xfip2022 = xfip2022_import,
         wpa2022 = wpa2022_import,
         retwentyfour2022 = retwentyfour2022_import,
         clutch2022 = clutch2022_import,
         outsidezoneswingpercent2022 = outsidezoneswingpercent2022_import,
         firstpitchstrikepercent2022 = firstpitchstrikepercent2022_import,
         swingingstrikespercent2022 = swingingstrikespercent2022_import,
         shutdowns2022 = shutdowns2022_import,
         meltdowns2022 = meltdowns2022_import,
         eraminus2022 = eraminus2022_import,
         fipminus2022 = fipminus2022_import,
         xfipminus2022 = xfipminus2022_import,
         bbpercent2022 = bbpercent2022_import,
         cswpercent2022 = cswpercent2022_import,
         siera2022 = siera2022_import,
         softpercent2022 = softpercent2022_import,
         mediumpercent2022 = mediumpercent2022_import,
         softplusmediumpercent2022 = softplusmediumpercent2022_import,
         kwera2022 = kwera2022_import,
         kpercent2022 = kpercent2022_import,
         weakpercent2022 = weakpercent2022_import,
         plus_k_per_nine2022 = plus_k_per_nine2022_import,
         plus_bb_per_nine2022 = plus_bb_per_nine2022_import,
         plus_k_per_bb2022 = plus_k_per_bb2022_import,
         plus_h_per_nine2022 = plus_h_per_nine2022_import,
         plus_hr_per_nine2022 = plus_hr_per_nine2022_import,
         plus_avg2022 = plus_avg2022_import,
         plus_whip2022 = plus_whip2022_import,
         plus_babip2022 = plus_babip2022_import,
         plus_lobpercent2022 = plus_lobpercent2022_import,
         plus_kpercent2022 = plus_kpercent2022_import,
         plus_bbpercent2022 = plus_bbpercent2022_import,
         plus_ldpercent2022 = plus_ldpercent2022_import,
         plus_gbpercent2022 = plus_gbpercent2022_import,
         plus_hrperfb2022 = plus_hrperfb2022_import,
         plus_softpercent2022 = plus_softpercent2022_import,
         plus_mediumpercent2022 = plus_mediumpercent2022_import,
         barrel_percent2022 = barrel_percent2022_import,
         hardhitpercent2022 = hardhitpercent2022_import,
         averageev2022 = averageev2022_import,
         averagela2022 = averagela2022_import,
         xera2022 = xera2022_import
     )
       new_pitcher.save()

    #since player id's only work for 2020/2021 players, no need to bother, since those players will already have been loaded in
    
    
    #barrel 2022
    data_2022_barrel = statcast_pitcher_exitvelo_barrels(2022, 20)
    number_of_players_2022 = data_2022_barrel.shape[0]
    #print(number_of_players_2022)
    for x in range(number_of_players_2022):
      lastname_import_2022 = data_2022_barrel.iat[x,0].replace(" ", "")
      firstname_import_2022 = data_2022_barrel.iat[x,1].replace(" ", "")
      teamname_import = data_2022.iat[x,3].replace(" ", "")
      key_mlbam_check_2022 = data_2022_barrel.iat[x,2]
      bbevents2022_import = float(data_2022_barrel.iat[x,3])
      #avghitangle2022_import = float(data_2022_barrel.iat[x,4])
      anglesweetspotpercent2022_import = float(data_2022_barrel.iat[x,5]) / 100
      #anglehitspeed2022_import = float(data_2022_barrel.iat[x,7])
      #bsgbpercent2022_import = data_2022_barrel.iat[x,9] / bbevents2022_import
      avgdistance2022_import = float(data_2022_barrel.iat[x,11])
      ev95plus2022_import = float(data_2022_barrel.iat[x,13])
      ev95pluspercent2022_import = float(data_2022_barrel.iat[x,14]) / 100
      #brlpercent2022_import = float(data_2022_barrel.iat[x,16])
      brlperpa2022_import = float(data_2022_barrel.iat[x,17])
      #print("inspecting " + lastname_import_2022 + " " + firstname_import_2022)
      if pitcher.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        #print("updating veteran " + lastname_import_2022 + " " + firstname_import_2022)
        update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2022)
        update_pitcher.loaded_bs_barrel_2022 = True
        update_pitcher.bbevents2022 = bbevents2022_import
        #update_pitcher.avghitangle2022 = avghitangle2022_import
        update_pitcher.anglesweetspotpercent2022 = anglesweetspotpercent2022_import
        #update_pitcher.anglehitspeed2022 = anglehitspeed2022_import
        #update_pitcher.bsgbpercent2022 = bsgbpercent2022_import
        update_pitcher.avgdistance2022 = avgdistance2022_import
        update_pitcher.ev95plus2022 = ev95plus2022_import
        update_pitcher.ev95pluspercent2022 = ev95pluspercent2022_import
        #update_pitcher.brlpercent2022 = brlpercent2022_import
        update_pitcher.brlperpa2022 = brlperpa2022_import
        update_pitcher.save()
      # if the player is a rookie and their ID is not currently loaded
      else: 
        try:
          #print("we will try")
          update_pitcher = pitcher.objects.get(lastname = lastname_import_2022, firstname = firstname_import_2022)
          #("updating rookie" + lastname_import_2022 + " " + firstname_import_2022)
          update_pitcher.key_mlbam = key_mlbam_check_2022
          update_pitcher.loaded_bs_barrel_2022 = True
          update_pitcher.bbevents2022 = bbevents2022_import
          #update_pitcher.avghitangle2022 = avghitangle2022_import
          update_pitcher.anglesweetspotpercent2022 = anglesweetspotpercent2022_import
          #update_pitcher.anglehitspeed2022 = anglehitspeed2022_import
          #update_pitcher.bsgbpercent2022 = bsgbpercent2022_import
          update_pitcher.avgdistance2022 = avgdistance2022_import
          update_pitcher.ev95plus2022 = ev95plus2022_import
          update_pitcher.ev95pluspercent2022 = ev95pluspercent2022_import
          #update_pitcher.brlpercent2022 = brlpercent2022_import
          update_pitcher.brlperpa2022 = brlperpa2022_import
          update_pitcher.save()
        except (update_pitcher.DoesNotExist, update_pitcher.MultipleObjectsReturned) as error:
          print(error)
          print("updating DNE" + lastname_import_2022 + " " + firstname_import_2022)
          k = 2
      
    #statcast expected 2022
    data_2022_expected = statcast_pitcher_expected_stats(2022, 20)
    number_of_players_2022 = data_2022_expected.shape[0]
    for x in range(number_of_players_2022):
      key_mlbam_check_2022 = data_2022_expected.iat[x,2]
      if pitcher.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2022)
        bip2022_import = float(data_2022_expected.iat[x,5])
        xavg2022_import = data_2022_expected.iat[x,7]
        xavgdiff2022_import = data_2022_expected.iat[x,8]
        slg2022_import = data_2022_expected.iat[x,9]
        xslg2022_import = data_2022_expected.iat[x,10]
        xslgdiff2022_import = data_2022_expected.iat[x,11]
        woba2022_import = data_2022_expected.iat[x,12]
        xwoba2022_import = data_2022_expected.iat[x,13]
        xwobadiff2022_import = data_2022_expected.iat[x,14]
        #bsera2022_import = float(data_2022_expected.iat[x,15])
        #bsxera2022_import = float(data_2022_expected.iat[x,16])
        xeradiff2022_import = data_2022_expected.iat[x,17]
        update_pitcher.bip2022 = bip2022_import
        update_pitcher.xavg2022 = xavg2022_import
        update_pitcher.xavgdiff2022 = xavgdiff2022_import
        update_pitcher.xslg2022 = xslg2022_import
        update_pitcher.slg2022 = slg2022_import
        update_pitcher.xslgdiff2022 = xslgdiff2022_import
        update_pitcher.woba2022 = woba2022_import
        update_pitcher.xwoba2022 = xwoba2022_import
        update_pitcher.xwobadiff2022 = xwobadiff2022_import
        #update_pitcher.bsera2022 = bsera2022_import
        #update_pitcher.bsxera2022 = bsxera2022_import
        update_pitcher.xeradiff2022 = xeradiff2022_import
        update_pitcher.loaded_bs_x_2022 = True
        update_pitcher.save()