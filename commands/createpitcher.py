import decimal
from django.core.management.base import BaseCommand
from app_bb.models import pitcher
from pybaseball import *
import numpy as np
import matplotlib.pylab as plt
from pybaseball.statcast_pitcher import statcast_pitcher_exitvelo_barrels
from pybaseball.statcast_pitcher import statcast_pitcher_expected_stats
import math

class Command(BaseCommand):
  def handle(self, *args, **options):

    try:
      entries = pitcher.objects.all()
      entries.delete()
    except:
      pass

    # if pitcher.objects.filter(lastname = "dummy").exists():
    #   pitcher.objects.filter(lastname = "dummy").delete()
    #takes 3:40 to run
    # LOAD 2022 DATA fangraph's
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
        loaded_k_per_bb2022 = loaded_k_per_bb2022_import,
        loaded_hrperfb2022 = loaded_hrperfb2022_import,
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


    #LOAD 2021 DATA
    data_2021 = pitching_stats(2021, qual = 5)
    number_of_players_2021 = data_2021.shape[0]
    for x in range(number_of_players_2021):
      full_name = data_2021.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
      firstname_import = full_name[0]
      lastname_import = full_name[1]
      teamname_import = data_2021.iat[x,3].replace(" ", "")
      fangraphs_id_import = data_2021.iat[x,0]
      if data_2021.iat[x,6] != 0:
        winningpercent_import = (float(data_2021.iat[x,5])) / (float(data_2021.iat[x,5])+ float(data_2021.iat[x,6]))
      war2021_import = data_2021.iat[x,7]
  
      era2021_import = float(data_2021.iat[x,8])
      shutouts2021_import = float(data_2021.iat[x,12])
      saves2021_import = float(data_2021.iat[x,13])
      if data_2021.iat[x,13] != 0:
        savepercent2021_import = (saves2021_import) / (saves2021_import + float(data_2021.iat[x,14]))
      else:
        savepercent2021_import = 0
      if data_2021.iat[x,15] % 1 < 0.11 and data_2021.iat[x,15] % 1 > 0.09:
        innings2021_import = float(data_2021.iat[x,15]) + .23
      elif data_2021.iat[x,15] % 1 < 0.21 and data_2021.iat[x,15] % 1 > 0.19:
        innings2021_import = float(data_2021.iat[x,15]) + .47
      else:
        innings2021_import = float(data_2021.iat[x,15])
      battersfaced2021_import = float(data_2021.iat[x,16])
      hits2021_import = float(data_2021.iat[x,17])
      runs2021_import = float(data_2021.iat[x,18])
      runsaverage2021_import = (runs2021_import * 9) / innings2021_import
      homeruns2021_import = float(data_2021.iat[x,20])
      bbhbp2021_import = float(data_2021.iat[x,21]) + float(data_2021.iat[x,23])
      k2021_import = float(data_2021.iat[x,26])
      thrownforkpercent2021_import = (float(data_2021.iat[x,32])) / float(data_2021.iat[x,33])
      kpernine2021_import = float(data_2021.iat[x,38])
      bbpernine2021_import = float(data_2021.iat[x,39])
      hitpernine2021_import = float(data_2021.iat[x,41])
      hrpernine2021_import = float(data_2021.iat[x,42])
      if (data_2021.iat[x,21] != 0):
        kperbb2021_import = float(data_2021.iat[x,40])
        plus_k_per_bb2021_import = float(data_2021.iat[x,304])
        loaded_k_per_bb2021_import = True
      else:
        kperbb2021_import = 0
        plus_k_per_bb2021_import = 0
        loaded_k_per_bb2021_import = False
      avg2021_import = data_2021.iat[x,43]
      whip2021_import = data_2021.iat[x,44]
      babip2021_import = data_2021.iat[x,45]
      lobpercent2021_import = data_2021.iat[x,46]
      if data_2021.iat[x,28] != 0:
        hrperfb2021_import = float(data_2021.iat[x,53])
        loaded_hrperfb2021_import = True
      else:
        hrperfb2021_import = 0
        loaded_hrperfb2021_import = False
      fip2021_import = data_2021.iat[x,47]
      gbperfb2021_import = data_2021.iat[x,48]
      gbpercent2021_import = data_2021.iat[x,50]
      iffbpercent2021_import = data_2021.iat[x,52]
      ldpercent2021_import = data_2021.iat[x,49]
      fbpercent2021_import = data_2021.iat[x,51]
      rar2021_import = float(data_2021.iat[x,60])
      tera2021_import = data_2021.iat[x,62]
      xfip2021_import = data_2021.iat[x,63]
      wpa2021_import = float(data_2021.iat[x,64])
      retwentyfour2021_import = float(data_2021.iat[x,67])
      clutch2021_import = data_2021.iat[x,75]
      outsidezoneswingpercent2021_import = data_2021.iat[x,106]
      firstpitchstrikepercent2021_import = data_2021.iat[x,113]
      swingingstrikespercent2021_import = data_2021.iat[x,114]
      shutdowns2021_import = float(data_2021.iat[x,116])
      meltdowns2021_import = float(data_2021.iat[x,117])
      eraminus2021_import = float(data_2021.iat[x,118])
      fipminus2021_import = float(data_2021.iat[x,119])
      xfipminus2021_import = float(data_2021.iat[x,120])
      bbpercent2021_import = float(data_2021.iat[x,122])
      cswpercent2021_import = float(data_2021.iat[x,332])
      siera2021_import = data_2021.iat[x,123]
      softpercent2021_import = data_2021.iat[x,222]
      mediumpercent2021_import = data_2021.iat[x,223]
      softplusmediumpercent2021_import = data_2021.iat[x,222] + data_2021.iat[x,223]
      kwera2021_import = data_2021.iat[x,225]
      kpercent2021_import = data_2021.iat[x,121]
      weakpercent2021_import = kpercent2021_import + ((gbpercent2021_import + iffbpercent2021_import) * (1 - kpercent2021_import - bbpercent2021_import))
      plus_k_per_nine2021_import = float(data_2021.iat[x,302])
      plus_bb_per_nine2021_import = float(data_2021.iat[x,303])
      plus_h_per_nine2021_import = float(data_2021.iat[x,305])
      plus_hr_per_nine2021_import = float(data_2021.iat[x,306])
      plus_avg2021_import = float(data_2021.iat[x,307])
      plus_whip2021_import = float(data_2021.iat[x,308])
      plus_babip2021_import = float(data_2021.iat[x,309])
      plus_lobpercent2021_import = float(data_2021.iat[x,310])
      plus_kpercent2021_import = float(data_2021.iat[x,311])
      plus_bbpercent2021_import = float(data_2021.iat[x,312])
      plus_ldpercent2021_import = float(data_2021.iat[x,313])
      plus_gbpercent2021_import = float(data_2021.iat[x,314])
      plus_hrperfb2021_import = float(data_2021.iat[x,316])
      plus_softpercent2021_import = float(data_2021.iat[x,320])
      plus_mediumpercent2021_import = float(data_2021.iat[x,321])
      barrel_percent2021_import = data_2021.iat[x,326]
      hardhitpercent2021_import = data_2021.iat[x,329]
      averageev2021_import = float(data_2021.iat[x,323])
      averagela2021_import = data_2021.iat[x,324]
      xera2021_import = data_2021.iat[x,333]
      
      if pitcher.objects.filter(fangraphs_id = fangraphs_id_import).exists():
        update_pitcher = pitcher.objects.get(fangraphs_id = fangraphs_id_import)
        update_pitcher.loaded_2021 = True
        update_pitcher.loaded_hrperfb2021 = loaded_hrperfb2021_import
        update_pitcher.loaded_k_per_bb2021 = loaded_k_per_bb2021_import
        update_pitcher.winningpercent2021 = winningpercent_import
        update_pitcher.war2021 = war2021_import
        update_pitcher.era2021 = era2021_import
        update_pitcher.shutouts2021 = shutouts2021_import
        update_pitcher.saves2021 = saves2021_import
        update_pitcher.savepercent2021 = savepercent2021_import
        update_pitcher.innings2021 = innings2021_import
        update_pitcher.battersfaced2021 = battersfaced2021_import
        update_pitcher.hits2021 = hits2021_import
        update_pitcher.runs2021 = runs2021_import
        update_pitcher.runsaverage2021 = runsaverage2021_import
        update_pitcher.homeruns2021 = homeruns2021_import
        update_pitcher.bbhbp2021 = bbhbp2021_import
        update_pitcher.k2021 = k2021_import
        update_pitcher.thrownforkpercent2021 = thrownforkpercent2021_import
        update_pitcher.kpernine2021 = kpernine2021_import
        update_pitcher.bbpernine2021 = bbpernine2021_import
        update_pitcher.hitpernine2021 = hitpernine2021_import
        update_pitcher.hrpernine2021 = hrpernine2021_import
        update_pitcher.kperbb2021 = kperbb2021_import
        update_pitcher.avg2021 = avg2021_import
        update_pitcher.whip2021 = whip2021_import
        update_pitcher.babip2021 = babip2021_import
        update_pitcher.lobpercent2021 = lobpercent2021_import
        update_pitcher.hrperfb2021 = hrperfb2021_import
        update_pitcher.fip2021 = fip2021_import
        update_pitcher.gbperfb2021 = gbperfb2021_import
        update_pitcher.gbpercent2021 = gbpercent2021_import
        update_pitcher.iffbpercent2021 = iffbpercent2021_import
        update_pitcher.ldpercent2021 = ldpercent2021_import
        update_pitcher.fbpercent2021 = fbpercent2021_import
        update_pitcher.rar2021 = rar2021_import
        update_pitcher.tera2021 = tera2021_import
        update_pitcher.xfip2021 = xfip2021_import
        update_pitcher.wpa2021 = wpa2021_import
        update_pitcher.retwentyfour2021 = retwentyfour2021_import
        update_pitcher.clutch2021 = clutch2021_import
        update_pitcher.outsidezoneswingpercent2021 = outsidezoneswingpercent2021_import
        update_pitcher.firstpitchstrikepercent2021 = firstpitchstrikepercent2021_import
        update_pitcher.swingingstrikespercent2021 = swingingstrikespercent2021_import
        update_pitcher.shutdowns2021 = shutdowns2021_import
        update_pitcher.meltdowns2021 = meltdowns2021_import
        update_pitcher.eraminus2021 = eraminus2021_import
        update_pitcher.fipminus2021 = fipminus2021_import
        update_pitcher.xfipminus2021 = xfipminus2021_import
        update_pitcher.bbpercent2021 = bbpercent2021_import
        update_pitcher.cswpercent2021 = cswpercent2021_import
        update_pitcher.siera2021 = siera2021_import
        update_pitcher.softpercent2021 = softpercent2021_import
        update_pitcher.mediumpercent2021 = mediumpercent2021_import
        update_pitcher.softplusmediumpercent2021 = softplusmediumpercent2021_import
        update_pitcher.kwera2021 = kwera2021_import
        update_pitcher.kpercent2021 = kpercent2021_import
        update_pitcher.weakpercent2021 = weakpercent2021_import
        update_pitcher.plus_k_per_nine2021 = plus_k_per_nine2021_import
        update_pitcher.plus_bb_per_nine2021 = plus_bb_per_nine2021_import
        update_pitcher.plus_k_per_bb2021 = plus_k_per_bb2021_import
        update_pitcher.plus_h_per_nine2021 = plus_h_per_nine2021_import
        update_pitcher.plus_hr_per_nine2021 = plus_hr_per_nine2021_import
        update_pitcher.plus_avg2021 = plus_avg2021_import
        update_pitcher.plus_whip2021 = plus_whip2021_import
        update_pitcher.plus_babip2021 = plus_babip2021_import
        update_pitcher.plus_lobpercent2021 = plus_lobpercent2021_import
        update_pitcher.plus_kpercent2021 = plus_kpercent2021_import
        update_pitcher.plus_bbpercent2021 = plus_bbpercent2021_import
        update_pitcher.plus_ldpercent2021 = plus_ldpercent2021_import
        update_pitcher.plus_gbpercent2021 = plus_gbpercent2021_import
        update_pitcher.plus_hrperfb2021 = plus_hrperfb2021_import
        update_pitcher.plus_softpercent2021 = plus_softpercent2021_import
        update_pitcher.plus_mediumpercent2021 = plus_mediumpercent2021_import
        update_pitcher.barrel_percent2021 = barrel_percent2021_import
        update_pitcher.hardhitpercent2021 = hardhitpercent2021_import
        update_pitcher.averageev2021 = averageev2021_import
        update_pitcher.averagela2021 = averagela2021_import
        update_pitcher.xera2021 = xera2021_import
        update_pitcher.save()

      else:
        new_pitcher = pitcher(
          loaded_2021 = True,
          firstname = firstname_import,
          lastname = lastname_import,
          teamname = teamname_import,
          fangraphs_id = fangraphs_id_import,
          winningpercent2021 = winningpercent_import,
          war2021 = war2021_import,
          era2021 = era2021_import,
          shutouts2021 = shutouts2021_import,
          saves2021 = saves2021_import,
          savepercent2021 = savepercent2021_import,
          innings2021 = innings2021_import,
          battersfaced2021 = battersfaced2021_import,
          hits2021 = hits2021_import,
          runs2021 = runs2021_import,
          runsaverage2021 = runsaverage2021_import,
          homeruns2021 = homeruns2021_import,
          bbhbp2021 = bbhbp2021_import,
          k2021 = k2021_import,
          thrownforkpercent2021 = thrownforkpercent2021_import,
          loaded_k_per_bb2021 = loaded_k_per_bb2021_import,
          loaded_hrperfb2021 = loaded_hrperfb2021_import,
          kpernine2021 = kpernine2021_import,
          bbpernine2021 = bbpernine2021_import,
          hitpernine2021 = hitpernine2021_import,
          hrpernine2021 = hrpernine2021_import,
          kperbb2021 = kperbb2021_import,
          avg2021 = avg2021_import,
          whip2021 = whip2021_import,
          babip2021 = babip2021_import,
          lobpercent2021 = lobpercent2021_import,
          hrperfb2021 = hrperfb2021_import,
          fip2021 = fip2021_import,
          gbperfb2021 = gbperfb2021_import,
          gbpercent2021 = gbpercent2021_import,
          iffbpercent2021 = iffbpercent2021_import,
          ldpercent2021 = ldpercent2021_import,
          fbpercent2021 = fbpercent2021_import,
          rar2021 = rar2021_import,
          tera2021 = tera2021_import,
          xfip2021 = xfip2021_import,
          wpa2021 = wpa2021_import,
          retwentyfour2021 = retwentyfour2021_import,
          clutch2021 = clutch2021_import,
          outsidezoneswingpercent2021 = outsidezoneswingpercent2021_import,
          firstpitchstrikepercent2021 = firstpitchstrikepercent2021_import,
          swingingstrikespercent2021 = swingingstrikespercent2021_import,
          shutdowns2021 = shutdowns2021_import,
          meltdowns2021 = meltdowns2021_import,
          eraminus2021 = eraminus2021_import,
          fipminus2021 = fipminus2021_import,
          xfipminus2021 = xfipminus2021_import,
          bbpercent2021 = bbpercent2021_import,
          cswpercent2021 = cswpercent2021_import,
          siera2021 = siera2021_import,
          softpercent2021 = softpercent2021_import,
          mediumpercent2021 = mediumpercent2021_import,
          softplusmediumpercent2021 = softplusmediumpercent2021_import,
          kwera2021 = kwera2021_import,
          kpercent2021 = kpercent2021_import,
          weakpercent2021 = weakpercent2021_import,
          plus_k_per_nine2021 = plus_k_per_nine2021_import,
          plus_bb_per_nine2021 = plus_bb_per_nine2021_import,
          plus_k_per_bb2021 = plus_k_per_bb2021_import,
          plus_h_per_nine2021 = plus_h_per_nine2021_import,
          plus_hr_per_nine2021 = plus_hr_per_nine2021_import,
          plus_avg2021 = plus_avg2021_import,
          plus_whip2021 = plus_whip2021_import,
          plus_babip2021 = plus_babip2021_import,
          plus_lobpercent2021 = plus_lobpercent2021_import,
          plus_kpercent2021 = plus_kpercent2021_import,
          plus_bbpercent2021 = plus_bbpercent2021_import,
          plus_ldpercent2021 = plus_ldpercent2021_import,
          plus_gbpercent2021 = plus_gbpercent2021_import,
          plus_hrperfb2021 = plus_hrperfb2021_import,
          plus_softpercent2021 = plus_softpercent2021_import,
          plus_mediumpercent2021 = plus_mediumpercent2021_import,
          barrel_percent2021 = barrel_percent2021_import,
          hardhitpercent2021 = hardhitpercent2021_import,
          averageev2021 = averageev2021_import,
          averagela2021 = averagela2021_import,
          xera2021 = xera2021_import
      )
      new_pitcher.save()

    #LOAD 2020 DATA
    data_2020 = pitching_stats(2020, qual = 5)
    number_of_players_2020 = data_2020.shape[0]
    for x in range(number_of_players_2020):
      full_name = data_2020.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
      firstname_import = full_name[0]
      lastname_import = full_name[1]
      teamname_import = data_2020.iat[x,3].replace(" ", "")
      fangraphs_id_import = data_2020.iat[x,0]
      if data_2020.iat[x,6] != 0:
        winningpercent_import = (float(data_2020.iat[x,5])) / (float(data_2020.iat[x,5])+ float(data_2020.iat[x,6]))
      war2020_import = data_2020.iat[x,7]
  
      era2020_import = float(data_2020.iat[x,8])
      shutouts2020_import = float(data_2020.iat[x,12])
      saves2020_import = float(data_2020.iat[x,13])
      if data_2020.iat[x,13] != 0:
        savepercent2020_import = (saves2020_import) / (saves2020_import + float(data_2020.iat[x,14]))
      else:
        savepercent2020_import = 0
      if data_2020.iat[x,15] % 1 < 0.11 and data_2020.iat[x,15] % 1 > 0.09:
        innings2020_import = float(data_2020.iat[x,15]) + .23
      elif data_2020.iat[x,15] % 1 < 0.21 and data_2020.iat[x,15] % 1 > 0.19:
        innings2020_import = float(data_2020.iat[x,15]) + .47
      else:
        innings2020_import = float(data_2020.iat[x,15])
      battersfaced2020_import = float(data_2020.iat[x,16])
      hits2020_import = float(data_2020.iat[x,17])
      runs2020_import = float(data_2020.iat[x,18])
      runsaverage2020_import = (runs2020_import * 9) / innings2020_import
      homeruns2020_import = float(data_2020.iat[x,20])
      bbhbp2020_import = float(data_2020.iat[x,21]) + float(data_2020.iat[x,23])
      k2020_import = float(data_2020.iat[x,26])
      thrownforkpercent2020_import = (float(data_2020.iat[x,32])) / float(data_2020.iat[x,33])
      kpernine2020_import = float(data_2020.iat[x,38])
      bbpernine2020_import = float(data_2020.iat[x,39])
      hitpernine2020_import = float(data_2020.iat[x,41])
      hrpernine2020_import = float(data_2020.iat[x,42])
      if (data_2020.iat[x,21] != 0):
        kperbb2020_import = float(data_2020.iat[x,40])
        plus_k_per_bb2020_import = float(data_2020.iat[x,304])
        loaded_k_per_bb2020_import = True
      else:
        kperbb2020_import = 0
        plus_k_per_bb2020_import = 0
        loaded_k_per_bb2020_import = False
      avg2020_import = data_2020.iat[x,43]
      whip2020_import = data_2020.iat[x,44]
      babip2020_import = data_2020.iat[x,45]
      lobpercent2020_import = data_2020.iat[x,46]
      if data_2020.iat[x,28] != 0:
        hrperfb2020_import = float(data_2020.iat[x,53])
        loaded_hrperfb2020_import = True
      else:
        hrperfb2020_import = 0
        loaded_hrperfb2020_import = False
      fip2020_import = data_2020.iat[x,47]
      gbperfb2020_import = data_2020.iat[x,48]
      gbpercent2020_import = data_2020.iat[x,50]
      iffbpercent2020_import = data_2020.iat[x,52]
      ldpercent2020_import = data_2020.iat[x,49]
      fbpercent2020_import = data_2020.iat[x,51]
      rar2020_import = float(data_2020.iat[x,60])
      tera2020_import = data_2020.iat[x,62]
      xfip2020_import = data_2020.iat[x,63]
      wpa2020_import = float(data_2020.iat[x,64])
      retwentyfour2020_import = float(data_2020.iat[x,67])
      clutch2020_import = data_2020.iat[x,75]
      outsidezoneswingpercent2020_import = data_2020.iat[x,106]
      firstpitchstrikepercent2020_import = data_2020.iat[x,113]
      swingingstrikespercent2020_import = data_2020.iat[x,114]
      shutdowns2020_import = float(data_2020.iat[x,116])
      meltdowns2020_import = float(data_2020.iat[x,117])
      eraminus2020_import = float(data_2020.iat[x,118])
      fipminus2020_import = float(data_2020.iat[x,119])
      xfipminus2020_import = float(data_2020.iat[x,120])
      bbpercent2020_import = float(data_2020.iat[x,122])
      cswpercent2020_import = float(data_2020.iat[x,332])
      siera2020_import = data_2020.iat[x,123]
      softpercent2020_import = data_2020.iat[x,222]
      mediumpercent2020_import = data_2020.iat[x,223]
      softplusmediumpercent2020_import = data_2020.iat[x,222] + data_2020.iat[x,223]
      kwera2020_import = data_2020.iat[x,225]
      kpercent2020_import = data_2020.iat[x,121]
      weakpercent2020_import = kpercent2020_import + ((gbpercent2020_import + iffbpercent2020_import) * (1 - kpercent2020_import - bbpercent2020_import))
      plus_k_per_nine2020_import = float(data_2020.iat[x,302])
      plus_bb_per_nine2020_import = float(data_2020.iat[x,303])
      plus_h_per_nine2020_import = float(data_2020.iat[x,305])
      plus_hr_per_nine2020_import = float(data_2020.iat[x,306])
      plus_avg2020_import = float(data_2020.iat[x,307])
      plus_whip2020_import = float(data_2020.iat[x,308])
      plus_babip2020_import = float(data_2020.iat[x,309])
      plus_lobpercent2020_import = float(data_2020.iat[x,310])
      plus_kpercent2020_import = float(data_2020.iat[x,311])
      plus_bbpercent2020_import = float(data_2020.iat[x,312])
      plus_ldpercent2020_import = float(data_2020.iat[x,313])
      plus_gbpercent2020_import = float(data_2020.iat[x,314])
      plus_hrperfb2020_import = float(data_2020.iat[x,316])
      plus_softpercent2020_import = float(data_2020.iat[x,320])
      plus_mediumpercent2020_import = float(data_2020.iat[x,321])
      barrel_percent2020_import = data_2020.iat[x,326]
      hardhitpercent2020_import = data_2020.iat[x,329]
      averageev2020_import = float(data_2020.iat[x,323])
      averagela2020_import = data_2020.iat[x,324]
      xera2020_import = data_2020.iat[x,333]
        
      if pitcher.objects.filter(fangraphs_id = fangraphs_id_import).exists():
        update_pitcher = pitcher.objects.get(fangraphs_id = fangraphs_id_import)
        update_pitcher.loaded_2020 = True
        update_pitcher.loaded_k_per_bb2020 = loaded_k_per_bb2020_import
        update_pitcher.loaded_hrperfb2020 = loaded_hrperfb2020_import
        update_pitcher.winningpercent2020 = winningpercent_import
        update_pitcher.war2020 = war2020_import
        update_pitcher.era2020 = era2020_import
        update_pitcher.shutouts2020 = shutouts2020_import
        update_pitcher.saves2020 = saves2020_import
        update_pitcher.savepercent2020 = savepercent2020_import
        update_pitcher.innings2020 = innings2020_import
        update_pitcher.battersfaced2020 = battersfaced2020_import
        update_pitcher.hits2020 = hits2020_import
        update_pitcher.runs2020 = runs2020_import
        update_pitcher.runsaverage2020 = runsaverage2020_import
        update_pitcher.homeruns2020 = homeruns2020_import
        update_pitcher.bbhbp2020 = bbhbp2020_import
        update_pitcher.k2020 = k2020_import
        update_pitcher.thrownforkpercent2020 = thrownforkpercent2020_import
        update_pitcher.kpernine2020 = kpernine2020_import
        update_pitcher.bbpernine2020 = bbpernine2020_import
        update_pitcher.hitpernine2020 = hitpernine2020_import
        update_pitcher.hrpernine2020 = hrpernine2020_import
        update_pitcher.kperbb2020 = kperbb2020_import
        update_pitcher.avg2020 = avg2020_import
        update_pitcher.whip2020 = whip2020_import
        update_pitcher.babip2020 = babip2020_import
        update_pitcher.lobpercent2020 = lobpercent2020_import
        update_pitcher.hrperfb2020 = hrperfb2020_import
        update_pitcher.fip2020 = fip2020_import
        update_pitcher.gbperfb2020 = gbperfb2020_import
        update_pitcher.gbpercent2020 = gbpercent2020_import
        update_pitcher.iffbpercent2020 = iffbpercent2020_import
        update_pitcher.ldpercent2020 = ldpercent2020_import
        update_pitcher.fbpercent2020 = fbpercent2020_import
        update_pitcher.rar2020 = rar2020_import
        update_pitcher.tera2020 = tera2020_import
        update_pitcher.xfip2020 = xfip2020_import
        update_pitcher.wpa2020 = wpa2020_import
        update_pitcher.retwentyfour2020 = retwentyfour2020_import
        update_pitcher.clutch2020 = clutch2020_import
        update_pitcher.outsidezoneswingpercent2020 = outsidezoneswingpercent2020_import
        update_pitcher.firstpitchstrikepercent2020 = firstpitchstrikepercent2020_import
        update_pitcher.swingingstrikespercent2020 = swingingstrikespercent2020_import
        update_pitcher.shutdowns2020 = shutdowns2020_import
        update_pitcher.meltdowns2020 = meltdowns2020_import
        update_pitcher.eraminus2020 = eraminus2020_import
        update_pitcher.fipminus2020 = fipminus2020_import
        update_pitcher.xfipminus2020 = xfipminus2020_import
        update_pitcher.bbpercent2020 = bbpercent2020_import
        update_pitcher.cswpercent2020 = cswpercent2020_import
        update_pitcher.siera2020 = siera2020_import
        update_pitcher.softpercent2020 = softpercent2020_import
        update_pitcher.mediumpercent2020 = mediumpercent2020_import
        update_pitcher.softplusmediumpercent2020 = softplusmediumpercent2020_import
        update_pitcher.kwera2020 = kwera2020_import
        update_pitcher.kpercent2020 = kpercent2020_import
        update_pitcher.weakpercent2020 = weakpercent2020_import
        update_pitcher.plus_k_per_nine2020 = plus_k_per_nine2020_import
        update_pitcher.plus_bb_per_nine2020 = plus_bb_per_nine2020_import
        update_pitcher.plus_k_per_bb2020 = plus_k_per_bb2020_import
        update_pitcher.plus_h_per_nine2020 = plus_h_per_nine2020_import
        update_pitcher.plus_hr_per_nine2020 = plus_hr_per_nine2020_import
        update_pitcher.plus_avg2020 = plus_avg2020_import
        update_pitcher.plus_whip2020 = plus_whip2020_import
        update_pitcher.plus_babip2020 = plus_babip2020_import
        update_pitcher.plus_lobpercent2020 = plus_lobpercent2020_import
        update_pitcher.plus_kpercent2020 = plus_kpercent2020_import
        update_pitcher.plus_bbpercent2020 = plus_bbpercent2020_import
        update_pitcher.plus_ldpercent2020 = plus_ldpercent2020_import
        update_pitcher.plus_gbpercent2020 = plus_gbpercent2020_import
        update_pitcher.plus_hrperfb2020 = plus_hrperfb2020_import
        update_pitcher.plus_softpercent2020 = plus_softpercent2020_import
        update_pitcher.plus_mediumpercent2020 = plus_mediumpercent2020_import
        update_pitcher.barrel_percent2020 = barrel_percent2020_import
        update_pitcher.hardhitpercent2020 = hardhitpercent2020_import
        update_pitcher.averageev2020 = averageev2020_import
        update_pitcher.averagela2020 = averagela2020_import
        update_pitcher.xera2020 = xera2020_import
        update_pitcher.save()
  
      else:
        new_pitcher = pitcher(
          loaded_2020 = True,
          firstname = firstname_import,
          lastname = lastname_import,
          teamname = teamname_import,
          fangraphs_id = fangraphs_id_import,
          winningpercent2020 = winningpercent_import,
          war2020 = war2020_import,
          era2020 = era2020_import,
          shutouts2020 = shutouts2020_import,
          saves2020 = saves2020_import,
          savepercent2020 = savepercent2020_import,
          innings2020 = innings2020_import,
          battersfaced2020 = battersfaced2020_import,
          hits2020 = hits2020_import,
          runs2020 = runs2020_import,
          runsaverage2020 = runsaverage2020_import,
          homeruns2020 = homeruns2020_import,
          bbhbp2020 = bbhbp2020_import,
          k2020 = k2020_import,
          thrownforkpercent2020 = thrownforkpercent2020_import,
          loaded_k_per_bb2020 = loaded_k_per_bb2020_import,
          loaded_hrperfb2020 = loaded_hrperfb2020_import,
          kpernine2020 = kpernine2020_import,
          bbpernine2020 = bbpernine2020_import,
          hitpernine2020 = hitpernine2020_import,
          hrpernine2020 = hrpernine2020_import,
          kperbb2020 = kperbb2020_import,
          avg2020 = avg2020_import,
          whip2020 = whip2020_import,
          babip2020 = babip2020_import,
          lobpercent2020 = lobpercent2020_import,
          hrperfb2020 = hrperfb2020_import,
          fip2020 = fip2020_import,
          gbperfb2020 = gbperfb2020_import,
          gbpercent2020 = gbpercent2020_import,
          iffbpercent2020 = iffbpercent2020_import,
          ldpercent2020 = ldpercent2020_import,
          fbpercent2020 = fbpercent2020_import,
          rar2020 = rar2020_import,
          tera2020 = tera2020_import,
          xfip2020 = xfip2020_import,
          wpa2020 = wpa2020_import,
          retwentyfour2020 = retwentyfour2020_import,
          clutch2020 = clutch2020_import,
          outsidezoneswingpercent2020 = outsidezoneswingpercent2020_import,
          firstpitchstrikepercent2020 = firstpitchstrikepercent2020_import,
          swingingstrikespercent2020 = swingingstrikespercent2020_import,
          shutdowns2020 = shutdowns2020_import,
          meltdowns2020 = meltdowns2020_import,
          eraminus2020 = eraminus2020_import,
          fipminus2020 = fipminus2020_import,
          xfipminus2020 = xfipminus2020_import,
          bbpercent2020 = bbpercent2020_import,
          cswpercent2020 = cswpercent2020_import,
          siera2020 = siera2020_import,
          softpercent2020 = softpercent2020_import,
          mediumpercent2020 = mediumpercent2020_import,
          softplusmediumpercent2020 = softplusmediumpercent2020_import,
          kwera2020 = kwera2020_import,
          kpercent2020 = kpercent2020_import,
          weakpercent2020 = weakpercent2020_import,
          plus_k_per_nine2020 = plus_k_per_nine2020_import,
          plus_bb_per_nine2020 = plus_bb_per_nine2020_import,
          plus_k_per_bb2020 = plus_k_per_bb2020_import,
          plus_h_per_nine2020 = plus_h_per_nine2020_import,
          plus_hr_per_nine2020 = plus_hr_per_nine2020_import,
          plus_avg2020 = plus_avg2020_import,
          plus_whip2020 = plus_whip2020_import,
          plus_babip2020 = plus_babip2020_import,
          plus_lobpercent2020 = plus_lobpercent2020_import,
          plus_kpercent2020 = plus_kpercent2020_import,
          plus_bbpercent2020 = plus_bbpercent2020_import,
          plus_ldpercent2020 = plus_ldpercent2020_import,
          plus_gbpercent2020 = plus_gbpercent2020_import,
          plus_hrperfb2020 = plus_hrperfb2020_import,
          plus_softpercent2020 = plus_softpercent2020_import,
          plus_mediumpercent2020 = plus_mediumpercent2020_import,
          barrel_percent2020 = barrel_percent2020_import,
          hardhitpercent2020 = hardhitpercent2020_import,
          averageev2020 = averageev2020_import,
          averagela2020 = averagela2020_import,
          xera2020 = xera2020_import
      )
      new_pitcher.save()


    #get ID's loaded in

    #load player_ids for each of the websites for each pitcher
    for iterate_pitcher in pitcher.objects.all():
      my_list = []
      my_list.append(iterate_pitcher.fangraphs_id)
      if len(my_list) == 1 and (iterate_pitcher.loaded_2021 or iterate_pitcher.loaded_2020): 
        # notice: pybaseball is currently returning error for players who have only played in 2022, 
        # hence the conditions where a pitcher must have 2020/2021 stats to gather the different id's from all the websites
        all_ids = playerid_reverse_lookup(my_list, key_type='fangraphs')
        iterate_pitcher.key_bbref = all_ids.iat[0,4]
        iterate_pitcher.key_retro = all_ids.iat[0,3]
        iterate_pitcher.key_mlbam = all_ids.iat[0,2]
        iterate_pitcher.save()

    #It is not, at the present moment, worth the effort of gathering anything from bref. perhaps at a later date

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
        # except update_pitcher.DoesNotExist:
        except:
          print("updating DNE" + lastname_import_2022 + " " + firstname_import_2022)
          k = 2
    
    #barrel 2021
    data_2021_barrel = statcast_pitcher_exitvelo_barrels(2021, 20)
    number_of_players_2021 = data_2021_barrel.shape[0]
    #print(number_of_players_2021)
    for x in range(number_of_players_2021):
      lastname_import_2021 = data_2021_barrel.iat[x,0].replace(" ", "")
      firstname_import_2021 = data_2021_barrel.iat[x,1].replace(" ", "")
      key_mlbam_check_2021 = data_2021_barrel.iat[x,2]
      bbevents2021_import = float(data_2021_barrel.iat[x,3])
      #avghitangle2021_import = float(data_2021_barrel.iat[x,4])
      anglesweetspotpercent2021_import = float(data_2021_barrel.iat[x,5]) / 100
      #anglehitspeed2021_import = float(data_2021_barrel.iat[x,7])
      #bsgbpercent2021_import = data_2021_barrel.iat[x,9] / bbevents2021_import
      avgdistance2021_import = float(data_2021_barrel.iat[x,11])
      ev95plus2021_import = float(data_2021_barrel.iat[x,13])
      ev95pluspercent2021_import = float(data_2021_barrel.iat[x,14]) / 100
      #brlpercent2021_import = float(data_2021_barrel.iat[x,16])
      brlperpa2021_import = float(data_2021_barrel.iat[x,17])
      #print("inspecting " + lastname_import_2021 + " " + firstname_import_2021)
      if pitcher.objects.filter(key_mlbam = key_mlbam_check_2021).exists():
        #print("updating veteran " + lastname_import_2021 + " " + firstname_import_2021)
        update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2021)
        update_pitcher.loaded_bs_barrel_2021 = True
        update_pitcher.bbevents2021 = bbevents2021_import
        #update_pitcher.avghitangle2021 = avghitangle2021_import
        update_pitcher.anglesweetspotpercent2021 = anglesweetspotpercent2021_import
        #update_pitcher.anglehitspeed2021 = anglehitspeed2021_import
        #update_pitcher.bsgbpercent2021 = bsgbpercent2021_import
        update_pitcher.avgdistance2021 = avgdistance2021_import
        update_pitcher.ev95plus2021 = ev95plus2021_import
        update_pitcher.ev95pluspercent2021 = ev95pluspercent2021_import
        #update_pitcher.brlpercent2021 = brlpercent2021_import
        update_pitcher.brlperpa2021 = brlperpa2021_import
        update_pitcher.save()

    #barrel 2020
    data_2020_barrel = statcast_pitcher_exitvelo_barrels(2020, 20)
    number_of_players_2020 = data_2020_barrel.shape[0]
    #print(number_of_players_2020)
    for x in range(number_of_players_2020):
      lastname_import_2020 = data_2020_barrel.iat[x,0].replace(" ", "")
      firstname_import_2020 = data_2020_barrel.iat[x,1].replace(" ", "")
      key_mlbam_check_2020 = data_2020_barrel.iat[x,2]
      bbevents2020_import = float(data_2020_barrel.iat[x,3])
      #avghitangle2020_import = float(data_2020_barrel.iat[x,4])
      anglesweetspotpercent2020_import = float(data_2020_barrel.iat[x,5]) / 100
      #anglehitspeed2020_import = float(data_2020_barrel.iat[x,7])
      # if bbevents2020_import != 0:
      #   bsgbpercent2020_import = data_2020_barrel.iat[x,9] / bbevents2020_import
      # else:
      #   bsgbpercent2020_import = 0
      avgdistance2020_import = float(data_2020_barrel.iat[x,11])
      ev95plus2020_import = float(data_2020_barrel.iat[x,13])
      ev95pluspercent2020_import = float(data_2020_barrel.iat[x,14]) / 100
      #brlpercent2020_import = float(data_2020_barrel.iat[x,16])
      brlperpa2020_import = float(data_2020_barrel.iat[x,17])
      #print("inspecting " + lastname_import_2020 + " " + firstname_import_2020)
      if pitcher.objects.filter(key_mlbam = key_mlbam_check_2020).exists():
        #print("updating veteran " + lastname_import_2020 + " " + firstname_import_2020)
        update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2020)
        update_pitcher.loaded_bs_barrel_2020 = True
        update_pitcher.bbevents2020 = bbevents2020_import
        #update_pitcher.avghitangle2020 = avghitangle2020_import
        update_pitcher.anglesweetspotpercent2020 = anglesweetspotpercent2020_import
        #update_pitcher.anglehitspeed2020 = anglehitspeed2020_import
        #update_pitcher.bsgbpercent2020 = bsgbpercent2020_import
        update_pitcher.avgdistance2020 = avgdistance2020_import
        update_pitcher.ev95plus2020 = ev95plus2020_import
        update_pitcher.ev95pluspercent2020 = ev95pluspercent2020_import
        #update_pitcher.brlpercent2020 = brlpercent2020_import
        update_pitcher.brlperpa2020 = brlperpa2020_import
        update_pitcher.save()

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

#statcast expected 2021
    data_2021_expected = statcast_pitcher_expected_stats(2021, 20)
    number_of_players_2021 = data_2021_expected.shape[0]
    for x in range(number_of_players_2021):
     key_mlbam_check_2021 = data_2021_expected.iat[x,2]
     if pitcher.objects.filter(key_mlbam = key_mlbam_check_2021).exists():
       update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2021)
       bip2021_import = float(data_2021_expected.iat[x,5])
       xavg2021_import = data_2021_expected.iat[x,7]
       xavgdiff2021_import = data_2021_expected.iat[x,8]
       slg2021_import = data_2021_expected.iat[x,9]
       xslg2021_import = data_2021_expected.iat[x,10]
       xslgdiff2021_import = data_2021_expected.iat[x,11]
       woba2021_import = data_2021_expected.iat[x,12]
       xwoba2021_import = data_2021_expected.iat[x,13]
       xwobadiff2021_import = data_2021_expected.iat[x,14]
       #bsera2021_import = float(data_2021_expected.iat[x,15])
       #bsxera2021_import = float(data_2021_expected.iat[x,16])
       xeradiff2021_import = data_2021_expected.iat[x,17]
       update_pitcher.bip2021 = bip2021_import
       update_pitcher.xavg2021 = xavg2021_import
       update_pitcher.xavgdiff2021 = xavgdiff2021_import
       update_pitcher.xslg2021 = xslg2021_import
       update_pitcher.slg2021 = slg2021_import
       update_pitcher.xslgdiff2021 = xslgdiff2021_import
       update_pitcher.woba2021 = woba2021_import
       update_pitcher.xwoba2021 = xwoba2021_import
       update_pitcher.xwobadiff2021 = xwobadiff2021_import
       #update_pitcher.bsera2021 = bsera2021_import
       #update_pitcher.bsxera2021 = bsxera2021_import
       update_pitcher.xeradiff2021 = xeradiff2021_import
       update_pitcher.loaded_bs_x_2021 = True
       update_pitcher.save()

    #statcast expected 2020
    data_2020_expected = statcast_pitcher_expected_stats(2020, 20)
    number_of_players_2020 = data_2020_expected.shape[0]
    for x in range(number_of_players_2020):
     key_mlbam_check_2020 = data_2020_expected.iat[x,2]
     if pitcher.objects.filter(key_mlbam = key_mlbam_check_2020).exists():
       update_pitcher = pitcher.objects.get(key_mlbam = key_mlbam_check_2020)
       bip2020_import = float(data_2020_expected.iat[x,5])
       xavg2020_import = data_2020_expected.iat[x,7]
       xavgdiff2020_import = data_2020_expected.iat[x,8]
       slg2020_import = data_2020_expected.iat[x,9]
       xslg2020_import = data_2020_expected.iat[x,10]
       xslgdiff2020_import = data_2020_expected.iat[x,11]
       woba2020_import = data_2020_expected.iat[x,12]
       xwoba2020_import = data_2020_expected.iat[x,13]
       xwobadiff2020_import = data_2020_expected.iat[x,14]
       #bsera2020_import = float(data_2020_expected.iat[x,15])
       #bsxera2020_import = float(data_2020_expected.iat[x,16])
       xeradiff2020_import = data_2020_expected.iat[x,17]
       update_pitcher.bip2020 = bip2020_import
       update_pitcher.xavg2020 = xavg2020_import
       update_pitcher.xavgdiff2020 = xavgdiff2020_import
       update_pitcher.xslg2020 = xslg2020_import
       update_pitcher.slg2020 = slg2020_import
       update_pitcher.xslgdiff2020 = xslgdiff2020_import
       update_pitcher.woba2020 = woba2020_import
       update_pitcher.xwoba2020 = xwoba2020_import
       update_pitcher.xwobadiff2020 = xwobadiff2020_import
       #update_pitcher.bsera2020 = bsera2020_import
       #update_pitcher.bsxera2020 = bsxera2020_import
       update_pitcher.xeradiff2020 = xeradiff2020_import
       update_pitcher.loaded_bs_x_2020 = True
       update_pitcher.save()
