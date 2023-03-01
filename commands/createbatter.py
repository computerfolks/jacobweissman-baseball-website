import decimal
from django.core.management.base import BaseCommand
from app_bb.models import batter
from pybaseball import *
from pybaseball.statcast_batter import statcast_batter_expected_stats
from pybaseball.statcast_batter import statcast_batter_exitvelo_barrels
from pybaseball.statcast_fielding import statcast_outs_above_average
from pybaseball.statcast_running import statcast_sprint_speed
import numpy as np
import matplotlib.pylab as plt

#takes 18:30 minutes


class Command(BaseCommand):
  def handle(self, *args, **options):

    try:
      entries = batter.objects.all()
      entries.delete()
    except:
      pass

    # if batter.objects.filter(lastname = "dummy").exists():
    #   batter.objects.filter(lastname = "dummy").delete()

    # LOAD 2022 DATA
    data_2022 = batting_stats(2022, qual = 30) 
    # note: it seems that the above minimum qual being set at 1 caused issues of dividing by 0 because of runs etc being scored without ab, so do not go too low, changing to 30 fixed everything
    number_of_players_2022 = data_2022.shape[0]
    for x in range(number_of_players_2022):
      fangraphs_id_import = data_2022.iat[x,0]
      pa2022_import = float(data_2022.iat[x,7])
      full_name = data_2022.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
      firstname_import = full_name[0]
      lastname_import = full_name[1]
      teamname_import = data_2022.iat[x,3].replace(" ", "")
      avg2022_import = data_2022.iat[x,24]
      plus_avg2022_import = float(data_2022.iat[x,289])
      obp2022_import = data_2022.iat[x,38] 
      plus_obp2022_import = float(data_2022.iat[x,292])
      slg2022_import = data_2022.iat[x,39]
      plus_slg2022_import = float(data_2022.iat[x,293])
      ops2022_import = data_2022.iat[x,40]
      bb_per_pa2022_import = data_2022.iat[x,35]
      plus_bb_per_pa2022_import = float(data_2022.iat[x,290])
      k_per_pa2022_import = data_2022.iat[x,36]
      plus_k_per_pa2022_import = float(data_2022.iat[x,291])
      r_per_pa2022_import = data_2022.iat[x,13]/pa2022_import
      rbi_per_pa2022_import = data_2022.iat[x,14]/pa2022_import
      gdp_per_pa2022_import = data_2022.iat[x,21]/pa2022_import
      xSB_added2022_import = float(data_2022.iat[x,22]) - (float(data_2022.iat[x,23]) * 2)
      xSB_added_percent2022_import = xSB_added2022_import / pa2022_import
      wRAA2022_import = float(data_2022.iat[x,52])
      wOBA2022_import = float(data_2022.iat[x,51])
      wRC2022_import = float(data_2022.iat[x,53])
      plus_wRC2022_import = float(data_2022.iat[x,62])
      iso2022_import = data_2022.iat[x,41]
      plus_iso2022_import = float(data_2022.iat[x,294])
      babip2022_import = data_2022.iat[x,42]
      plus_babip2022_import = float(data_2022.iat[x,295])
      ld_per_bip2022_import = data_2022.iat[x,44]
      plus_ld_per_bip2022_import = float(data_2022.iat[x,296])
      gb_per_bip2022_import = data_2022.iat[x,45]
      plus_gb_per_bip2022_import = float(data_2022.iat[x,297])
      fb_per_bip2022_import = data_2022.iat[x,46]
      plus_fb_per_bip2022_import = float(data_2022.iat[x,298])
      iffb_per_bip2022_import = data_2022.iat[x,47]
      hr_per_fb2022_import = data_2022.iat[x,48]
      plus_hr_per_fb2022_import = float(data_2022.iat[x,299])
      loaded_hr_per_fb2022_import = True
      if np.isnan(hr_per_fb2022_import):
        hr_per_fb2022_import = 0
        plus_hr_per_fb2022_import = 0
        loaded_hr_per_fb2022_import = False
      if np.isnan(plus_hr_per_fb2022_import):
        hr_per_fb2022_import = 0
        plus_hr_per_fb2022_import = 0
        loaded_hr_per_fb2022_import = False
      spd2022_import = data_2022.iat[x,61]
      bsr2022_import = data_2022.iat[x,112]
      clutch2022_import = data_2022.iat[x,72] 
      fwar2022_import = data_2022.iat[x,59]
      hardpercent2022_import = float(data_2022.iat[x,212])
      plus_hardpercent2022_import = float(data_2022.iat[x,305])
      #barrel_percent2022_import = float(data_2022.iat[x,309])
      #maxEV2022_import = float(data_2022.iat[x,310])
      hardhitpercent2022_import = float(data_2022.iat[x,312])
      #xBA2022_import = float(data_2022.iat[x,316])
      #fgxSLG2022_import = float(data_2022.iat[x,317])
      #fgxWOBA2022_import = float(data_2022.iat[x,318])
      fwar_per_pa2022_import = fwar2022_import / pa2022_import
      bsr_per_pa2022_import = bsr2022_import / pa2022_import
      outsidezoneswingpercent2022_import = float(data_2022.iat[x,103])
      firstpitchstrikepercent2022_import = float(data_2022.iat[x,110])
      swingcontactpercent2022_import = float(data_2022.iat[x,108])
      swingingstrikespercent2022_import = float(data_2022.iat[x,111])
      foff2022_import = float(data_2022.iat[x,204])
      fdef2022_import = float(data_2022.iat[x,200])
      foff_per_pa2022_import = foff2022_import / pa2022_import
      fdef_per_pa2022_import = fdef2022_import / pa2022_import
      ffld2022_import = float(data_2022.iat[x,55])
      fldloaded_2022_import = True
      if np.isnan(ffld2022_import):
        fdef2022_import = 0
        fdef_per_pa2022_import = 0
        ffld2022_import = 0
        fldloaded_2022_import = False
      fbat2022_import = float(data_2022.iat[x,54])
      ffld_per_pa2022_import = ffld2022_import / pa2022_import
      fbat_per_pa2022_import = fbat2022_import / pa2022_import
      new_batter = batter(
        fangraphs_id = fangraphs_id_import,
        pa2022=pa2022_import,
        loaded_2022 = True,
        teamname = teamname_import,
        lastname = lastname_import, 
        firstname = firstname_import,
       
        avg2022 = avg2022_import, 
        plus_avg2022 = plus_avg2022_import,
        obp2022 = obp2022_import,
        plus_obp2022 = plus_obp2022_import,
        slg2022 = slg2022_import,
        plus_slg2022 = plus_slg2022_import,
        ops2022 = ops2022_import,
        bb_per_pa2022 = bb_per_pa2022_import,
        plus_bb_per_pa2022 = plus_bb_per_pa2022_import,
        k_per_pa2022 = k_per_pa2022_import,
        plus_k_per_pa2022 = plus_k_per_pa2022_import,
        r_per_pa2022 = r_per_pa2022_import,
        rbi_per_pa2022 = rbi_per_pa2022_import,
        gdp_per_pa2022 = gdp_per_pa2022_import,
        xSB_added2022 = xSB_added2022_import,
        xSB_added_percent2022 = xSB_added_percent2022_import,
        wRAA2022 = wRAA2022_import,
        wOBA2022 = wOBA2022_import,
        wRC2022 = wRC2022_import,
        plus_wRC2022 = plus_wRC2022_import,
        iso2022 = iso2022_import,
        plus_iso2022 = plus_iso2022_import,
        babip2022 = babip2022_import,
        plus_babip2022 = plus_babip2022_import,
        ld_per_bip2022 = ld_per_bip2022_import,
        # plus_ld_per_bip2022 = plus_ld_per_bip2022_import, #note: seems to be messed up
        gb_per_bip2022 = gb_per_bip2022_import,
        plus_gb_per_bip2022 = plus_gb_per_bip2022_import,
        fb_per_bip2022 = fb_per_bip2022_import,
        plus_fb_per_bip2022 = plus_fb_per_bip2022_import,
        iffb_per_bip2022 = iffb_per_bip2022_import,
        hr_per_fb2022 = hr_per_fb2022_import,
        plus_hr_per_fb2022 = plus_hr_per_fb2022_import,
        spd2022 = spd2022_import,
        bsr2022 = bsr2022_import,
        clutch2022 = clutch2022_import,
        fwar2022 = fwar2022_import,
        hardpercent2022 = hardpercent2022_import,
        plus_hardpercent2022 = plus_hardpercent2022_import,
        #barrel_percent2022 = barrel_percent2022_import,
        #maxEV2022 = maxEV2022_import,
        hardhitpercent2022 = hardhitpercent2022_import,
        #xBA2022 = xBA2022_import,
        #fgxSLG2022 = fgxSLG2022_import,
        #fgxWOBA2022 = fgxWOBA2022_import,
        fwar_per_pa2022 = fwar_per_pa2022_import,
        bsr_per_pa2022 = bsr_per_pa2022_import,
        outsidezoneswingpercent2022 = outsidezoneswingpercent2022_import,
        firstpitchstrikepercent2022 = firstpitchstrikepercent2022_import,
        swingcontactpercent2022 = swingcontactpercent2022_import,
        swingingstrikespercent2022 = swingingstrikespercent2022_import,
        foff2022 = foff2022_import,
        fdef2022 = fdef2022_import,
        foff_per_pa2022 = foff_per_pa2022_import,
        fdef_per_pa2022 = fdef_per_pa2022_import,
        ffld2022 = ffld2022_import,
        fbat2022 = fbat2022_import,
        ffld_per_pa2022 = ffld_per_pa2022_import,
        fbat_per_pa2022 = fbat_per_pa2022_import,
        fldloaded_2022 = fldloaded_2022_import,
        loaded_hr_per_fb2022 = loaded_hr_per_fb2022_import
        )
      new_batter.save()
    
    # LOAD 2021 DATA
    data_2021 = batting_stats(2021, qual = 30)  # tried 30 minimum, gave me the float/int error
    number_of_players_2021 = data_2021.shape[0]
    for x in range(number_of_players_2021):

      # load 2021 stats
      pa2021_import = float(data_2021.iat[x,7])
      full_name = data_2021.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
      firstname_import = full_name[0]
      lastname_import = full_name[1]
      teamname_import = data_2021.iat[x,3].replace(" ", "")
      avg2021_import = data_2021.iat[x,24]
      plus_avg2021_import = float(data_2021.iat[x,289])
      obp2021_import = data_2021.iat[x,38]
      plus_obp2021_import = float(data_2021.iat[x,292])
      slg2021_import = data_2021.iat[x,39]
      plus_slg2021_import = float(data_2021.iat[x,293])
      ops2021_import = data_2021.iat[x,40]
      bb_per_pa2021_import = data_2021.iat[x,35]
      plus_bb_per_pa2021_import = float(data_2021.iat[x,290])
      k_per_pa2021_import = data_2021.iat[x,36]
      plus_k_per_pa2021_import = float(data_2021.iat[x,291])
      r_per_pa2021_import = data_2021.iat[x,13]/pa2021_import
      rbi_per_pa2021_import = data_2021.iat[x,14]/pa2021_import
      gdp_per_pa2021_import = data_2021.iat[x,21]/pa2021_import
      xSB_added2021_import = float(data_2021.iat[x,22]) - (float(data_2021.iat[x,23]) * 2)
      xSB_added_percent2021_import = xSB_added2021_import / pa2021_import
      wRAA2021_import = float(data_2021.iat[x,52])
      wOBA2021_import = float(data_2021.iat[x,51])
      wRC2021_import = float(data_2021.iat[x,53])
      plus_wRC2021_import = float(data_2021.iat[x,62])
      iso2021_import = data_2021.iat[x,41]
      plus_iso2021_import = float(data_2021.iat[x,294])
      babip2021_import = data_2021.iat[x,42]
      plus_babip2021_import = float(data_2021.iat[x,295])
      ld_per_bip2021_import = data_2021.iat[x,44]
      plus_ld_per_bip2021_import = float(data_2021.iat[x,296])
      gb_per_bip2021_import = data_2021.iat[x,45]
      plus_gb_per_bip2021_import = float(data_2021.iat[x,297])
      fb_per_bip2021_import = data_2021.iat[x,46]
      plus_fb_per_bip2021_import = float(data_2021.iat[x,298])
      iffb_per_bip2021_import = data_2021.iat[x,47]
      hr_per_fb2021_import = data_2021.iat[x,48]
      plus_hr_per_fb2021_import = float(data_2021.iat[x,299])
      loaded_hr_per_fb2021_import = True
      if np.isnan(hr_per_fb2021_import):
        hr_per_fb2021_import = 0
        plus_hr_per_fb2021_import = 0
        loaded_hr_per_fb2021_import = False
      if np.isnan(plus_hr_per_fb2021_import):
        hr_per_fb2021_import = 0
        plus_hr_per_fb2021_import = 0
        loaded_hr_per_fb2021_import = False
      spd2021_import = data_2021.iat[x,61]
      bsr2021_import = data_2021.iat[x,112]
      clutch2021_import = data_2021.iat[x,72]
      fwar2021_import = data_2021.iat[x,59]
      hardpercent2021_import = float(data_2021.iat[x,212])
      plus_hardpercent2021_import = float(data_2021.iat[x,305])
      #barrel_percent2021_import = float(data_2021.iat[x,309])
      #maxEV2021_import = float(data_2021.iat[x,310])
      hardhitpercent2021_import = float(data_2021.iat[x,312])
      #xBA2021_import = float(data_2021.iat[x,316])
      #fgxSLG2021_import = float(data_2021.iat[x,317])
      #fgxWOBA2021_import = float(data_2021.iat[x,318])
      fwar_per_pa2021_import = fwar2021_import / pa2021_import
      bsr_per_pa2021_import = bsr2021_import / pa2021_import
      outsidezoneswingpercent2021_import = float(data_2021.iat[x,103])
      firstpitchstrikepercent2021_import = float(data_2021.iat[x,110])
      swingcontactpercent2021_import = float(data_2021.iat[x,108])
      swingingstrikespercent2021_import = float(data_2021.iat[x,111])
      foff2021_import = float(data_2021.iat[x,204])
      fdef2021_import = float(data_2021.iat[x,200])
      foff_per_pa2021_import = foff2021_import / pa2021_import
      fdef_per_pa2021_import = fdef2021_import / pa2021_import
      ffld2021_import = float(data_2021.iat[x,55])
      fldloaded_2021_import = True
      if np.isnan(ffld2021_import):
        fdef2021_import = 0
        fdef_per_pa2021_import = 0
        ffld2021_import = 0
        fldloaded_2021_import = False
      fbat2021_import = float(data_2021.iat[x,54])
      ffld_per_pa2021_import = ffld2021_import / pa2021_import
      fbat_per_pa2021_import = fbat2021_import / pa2021_import
      # check for the id
      fangraphs_id_check_2021 = data_2021.iat[x,0]
      if batter.objects.filter(fangraphs_id = fangraphs_id_check_2021).exists():
        update_batter = batter.objects.get(fangraphs_id = fangraphs_id_check_2021)
        # update the stats for the batter
        update_batter.pa2021 = pa2021_import
        update_batter.avg2021 = avg2021_import
        update_batter.plus_avg2021 = plus_avg2021_import
        update_batter.obp2021 = obp2021_import
        update_batter.plus_obp2021 = plus_obp2021_import
        update_batter.slg2021 = slg2021_import
        update_batter.plus_slg2021 = plus_slg2021_import
        update_batter.ops2021 = ops2021_import
        update_batter.bb_per_pa2021 = bb_per_pa2021_import
        update_batter.plus_bb_per_pa2021 = plus_bb_per_pa2021_import
        update_batter.k_per_pa2021 = k_per_pa2021_import
        update_batter.plus_k_per_pa2021 = plus_k_per_pa2021_import
        update_batter.r_per_pa2021 = r_per_pa2021_import
        update_batter.rbi_per_pa2021 = rbi_per_pa2021_import
        update_batter.gdp_per_pa2021 = gdp_per_pa2021_import
        update_batter.xSB_added2021 = xSB_added2021_import
        update_batter.xSB_added_percent2021 = xSB_added_percent2021_import
        update_batter.wRAA2021 = wRAA2021_import
        update_batter.wOBA2021 = wOBA2021_import
        update_batter.wRC2021 = wRC2021_import
        update_batter.plus_wRC2021 = plus_wRC2021_import
        update_batter.iso2021 = iso2021_import
        update_batter.plus_iso2021 = plus_iso2021_import
        update_batter.babip2021 = babip2021_import
        update_batter.plus_babip2021 = plus_babip2021_import
        update_batter.ld_per_bip2021 = ld_per_bip2021_import
        # update_batter.plus_ld_per_bip2021 = plus_ld_per_bip2021_import, #note: seems to be messed up
        update_batter.gb_per_bip2021 = gb_per_bip2021_import
        update_batter.plus_gb_per_bip2021 = plus_gb_per_bip2021_import
        update_batter.fb_per_bip2021 = fb_per_bip2021_import
        update_batter.plus_fb_per_bip2021 = plus_fb_per_bip2021_import
        update_batter.iffb_per_bip2021 = iffb_per_bip2021_import
        update_batter.hr_per_fb2021 = hr_per_fb2021_import
        update_batter.plus_hr_per_fb2021 = plus_hr_per_fb2021_import
        update_batter.spd2021 = spd2021_import
        update_batter.bsr2021 = bsr2021_import
        update_batter.clutch2021 = clutch2021_import
        update_batter.fwar2021 = fwar2021_import
        update_batter.hardpercent2021 = hardpercent2021_import
        update_batter.plus_hardpercent2021 = plus_hardpercent2021_import
        #update_batter.barrel_percent2021 = barrel_percent2021_import
        #update_batter.maxEV2021= maxEV2021_import
        update_batter.hardhitpercent2021 = hardhitpercent2021_import
        #update_batter.xBA2021 = xBA2021_import
        #update_batter.fgxSLG2021 = fgxSLG2021_import
        #update_batter.fgxWOBA2021 = fgxWOBA2021_import
        update_batter.loaded_2021 = True
        update_batter.fwar_per_pa2021 = fwar_per_pa2021_import
        update_batter.bsr_per_pa2021 = bsr_per_pa2021_import
        update_batter.outsidezoneswingpercent2021 = outsidezoneswingpercent2021_import
        update_batter.firstpitchstrikepercent2021 = firstpitchstrikepercent2021_import
        update_batter.swingcontactpercent2021 = swingcontactpercent2021_import
        update_batter.swingingstrikespercent2021 = swingingstrikespercent2021_import
        update_batter.foff2021 = foff2021_import
        update_batter.fdef2021 = fdef2021_import
        update_batter.foff_per_pa2021 = foff_per_pa2021_import
        update_batter.fdef_per_pa2021 = fdef_per_pa2021_import
        update_batter.ffld2021 = ffld2021_import
        update_batter.fbat2021 = fbat2021_import
        update_batter.ffld_per_pa2021 = ffld_per_pa2021_import
        update_batter.fbat_per_pa2021 = fbat_per_pa2021_import
        update_batter.fldloaded_2021 = fldloaded_2021_import
        update_batter.loaded_hr_per_fb2021 = loaded_hr_per_fb2021_import
        # save the updates
        update_batter.save()
        # except:
        #   print(firstname_import + " " + lastname_import + " with ")
        #   print(pa2021_import)
        #   print("plate appearances and ")
        #   print(fangraphs_id_check_2021)
        #   print("fangraphs ID \nthe type of object for the ID is ")
        #   print(type(fangraphs_id_check_2021))
        #   print("the type of object for the temp is ")
        #   print(type(temp))
        #   print("fangraphs ID the type of object for the native stored ID is ")
        #   print(type(update_batter.fangraphs_id))


      #if the batter did not exist in the 2022 data pull, we must create the batter now
      else:
        new_batter = batter(
        fangraphs_id = fangraphs_id_check_2021,
        pa2021=pa2021_import,
        loaded_2021 = True,
        lastname = lastname_import,
        firstname = firstname_import,
        teamname = teamname_import,
        avg2021 = avg2021_import,
        plus_avg2021 = plus_avg2021_import,
        obp2021 = obp2021_import,
        plus_obp2021 = plus_obp2021_import,
        slg2021 = slg2021_import,
        plus_slg2021 = plus_slg2021_import,
        ops2021 = ops2021_import,
        bb_per_pa2021 = bb_per_pa2021_import,
        plus_bb_per_pa2021 = plus_bb_per_pa2021_import,
        k_per_pa2021 = k_per_pa2021_import,
        plus_k_per_pa2021 = plus_k_per_pa2021_import,
        r_per_pa2021 = r_per_pa2021_import,
        rbi_per_pa2021 = rbi_per_pa2021_import,
        gdp_per_pa2021 = gdp_per_pa2021_import,
        xSB_added2021 = xSB_added2021_import,
        xSB_added_percent2021 = xSB_added_percent2021_import,
        wRAA2021 = wRAA2021_import,
        wOBA2021 = wOBA2021_import,
        wRC2021 = wRC2021_import,
        plus_wRC2021 = plus_wRC2021_import,
        iso2021 = iso2021_import,
        plus_iso2021 = plus_iso2021_import,
        babip2021 = babip2021_import,
        plus_babip2021 = plus_babip2021_import,
        ld_per_bip2021 = ld_per_bip2021_import,
        # # plus_ld_per_bip2021 = plus_ld_per_bip2021_import, #note: seems to be messed up
        gb_per_bip2021 = gb_per_bip2021_import,
        plus_gb_per_bip2021 = plus_gb_per_bip2021_import,
        fb_per_bip2021 = fb_per_bip2021_import,
        plus_fb_per_bip2021 = plus_fb_per_bip2021_import,
        iffb_per_bip2021 = iffb_per_bip2021_import,
        hr_per_fb2021 = hr_per_fb2021_import,
        plus_hr_per_fb2021 = plus_hr_per_fb2021_import,
        spd2021 = spd2021_import,
        bsr2021 = bsr2021_import,
        clutch2021 = clutch2021_import,
        fwar2021 = fwar2021_import,
        hardpercent2021 = hardpercent2021_import,
        plus_hardpercent2021 = plus_hardpercent2021_import,
        #barrel_percent2021 = barrel_percent2021_import,
        #maxEV2021 = maxEV2021_import,
        hardhitpercent2021 = hardhitpercent2021_import,
        #xBA2021 = xBA2021_import,
        #fgxSLG2021 = fgxSLG2021_import,
        #fgxWOBA2021 = fgxWOBA2021_import,
        fwar_per_pa2021 = fwar_per_pa2021_import,
        bsr_per_pa2021 = bsr_per_pa2021_import,
        outsidezoneswingpercent2021 = outsidezoneswingpercent2021_import,
        firstpitchstrikepercent2021 = firstpitchstrikepercent2021_import,
        swingcontactpercent2021 = swingcontactpercent2021_import,
        swingingstrikespercent2021 = swingingstrikespercent2021_import,
        foff2021 = foff2021_import,
        fdef2021 = fdef2021_import,
        foff_per_pa2021 = foff_per_pa2021_import,
        fdef_per_pa2021 = fdef_per_pa2021_import,
        ffld2021 = ffld2021_import,
        fbat2021 = fbat2021_import,
        ffld_per_pa2021 = ffld_per_pa2021_import,
        fbat_per_pa2021 = fbat_per_pa2021_import,
        fldloaded_2021 = fldloaded_2021_import,
        loaded_hr_per_fb2021 = loaded_hr_per_fb2021_import
        )
        new_batter.save()

    # LOAD 2020 DATA
    data_2020 = batting_stats(2020, qual = 30)
    number_of_players_2020 = data_2020.shape[0]
    for x in range(number_of_players_2020):
 
     # load 2020 stats
     pa2020_import = float(data_2020.iat[x,7])
     full_name = data_2020.iat[x,2].split(" ") #row, column (keep 0 fixed in 2nd spot you will keep getting names)
     firstname_import = full_name[0]
     lastname_import = full_name[1]
     teamname_import = data_2020.iat[x,3].replace(" ", "")
     avg2020_import = data_2020.iat[x,24]
     plus_avg2020_import = float(data_2020.iat[x,289])
     obp2020_import = data_2020.iat[x,38]
     plus_obp2020_import = float(data_2020.iat[x,292])
     slg2020_import = data_2020.iat[x,39]
     plus_slg2020_import = float(data_2020.iat[x,293])
     ops2020_import = data_2020.iat[x,40]
     bb_per_pa2020_import = data_2020.iat[x,35]
     plus_bb_per_pa2020_import = float(data_2020.iat[x,290])
     k_per_pa2020_import = data_2020.iat[x,36]
     plus_k_per_pa2020_import = float(data_2020.iat[x,291])
     r_per_pa2020_import = data_2020.iat[x,13]/pa2020_import
     rbi_per_pa2020_import = data_2020.iat[x,14]/pa2020_import
     gdp_per_pa2020_import = data_2020.iat[x,21]/pa2020_import
     xSB_added2020_import = float(data_2020.iat[x,22]) - (float(data_2020.iat[x,23]) * 2)
     xSB_added_percent2020_import = xSB_added2020_import / pa2020_import
     wRAA2020_import = float(data_2020.iat[x,52])
     wOBA2020_import = float(data_2020.iat[x,51])
     wRC2020_import = float(data_2020.iat[x,53])
     plus_wRC2020_import = float(data_2020.iat[x,62])
     iso2020_import = data_2020.iat[x,41]
     plus_iso2020_import = float(data_2020.iat[x,294])
     babip2020_import = data_2020.iat[x,42]
     plus_babip2020_import = float(data_2020.iat[x,295])
     ld_per_bip2020_import = data_2020.iat[x,44]
     plus_ld_per_bip2020_import = float(data_2020.iat[x,296])
     gb_per_bip2020_import = data_2020.iat[x,45]
     plus_gb_per_bip2020_import = float(data_2020.iat[x,297])
     fb_per_bip2020_import = data_2020.iat[x,46]
     plus_fb_per_bip2020_import = float(data_2020.iat[x,298])
     iffb_per_bip2020_import = data_2020.iat[x,47]
     hr_per_fb2020_import = data_2020.iat[x,48]
     plus_hr_per_fb2020_import = float(data_2020.iat[x,299])
     loaded_hr_per_fb2020_import = True
     if np.isnan(hr_per_fb2020_import):
       hr_per_fb2020_import = 0
       plus_hr_per_fb2020_import = 0
       loaded_hr_per_fb2020_import = False
     if np.isnan(plus_hr_per_fb2020_import):
       hr_per_fb2020_import = 0
       plus_hr_per_fb2020_import = 0
       loaded_hr_per_fb2020_import = False
     spd2020_import = data_2020.iat[x,61]
     bsr2020_import = data_2020.iat[x,112]
     clutch2020_import = data_2020.iat[x,72]
     fwar2020_import = data_2020.iat[x,59]
     hardpercent2020_import = float(data_2020.iat[x,212])
     plus_hardpercent2020_import = float(data_2020.iat[x,305])
     #barrel_percent2020_import = float(data_2020.iat[x,309])
     #maxEV2020_import = float(data_2020.iat[x,310])
     hardhitpercent2020_import = float(data_2020.iat[x,312])
     #xBA2020_import = float(data_2020.iat[x,316])
     #fgxSLG2020_import = float(data_2020.iat[x,317])
     #fgxWOBA2020_import = float(data_2020.iat[x,318])
     fwar_per_pa2020_import = fwar2020_import / pa2020_import
     bsr_per_pa2020_import = bsr2020_import / pa2020_import
     outsidezoneswingpercent2020_import = float(data_2020.iat[x,103])
     firstpitchstrikepercent2020_import = float(data_2020.iat[x,110])
     swingcontactpercent2020_import = float(data_2020.iat[x,108])
     swingingstrikespercent2020_import = float(data_2020.iat[x,111])
     foff2020_import = float(data_2020.iat[x,204])
     fdef2020_import = float(data_2020.iat[x,200])
     foff_per_pa2020_import = foff2020_import / pa2020_import
     fdef_per_pa2020_import = fdef2020_import / pa2020_import
     ffld2020_import = float(data_2020.iat[x,55])
     fldloaded_2020_import = True
     if np.isnan(ffld2020_import):
       fdef2020_import = 0
       fdef_per_pa2020_import = 0
       ffld2020_import = 0
       fldloaded_2020_import = False
     fbat2020_import = float(data_2020.iat[x,54])
     ffld_per_pa2020_import = ffld2020_import / pa2020_import
     fbat_per_pa2020_import = fbat2020_import / pa2020_import
     # check for the id
     fangraphs_id_check_2020 = data_2020.iat[x,0]
     if batter.objects.filter(fangraphs_id = fangraphs_id_check_2020).exists():
       update_batter = batter.objects.get(fangraphs_id = fangraphs_id_check_2020)
       # update the stats for the batter
       update_batter.pa2020 = pa2020_import
       update_batter.avg2020 = avg2020_import
       update_batter.plus_avg2020 = plus_avg2020_import
       update_batter.obp2020 = obp2020_import
       update_batter.plus_obp2020 = plus_obp2020_import
       update_batter.slg2020 = slg2020_import
       update_batter.plus_slg2020 = plus_slg2020_import
       update_batter.ops2020 = ops2020_import
       update_batter.bb_per_pa2020 = bb_per_pa2020_import
       update_batter.plus_bb_per_pa2020 = plus_bb_per_pa2020_import
       update_batter.k_per_pa2020 = k_per_pa2020_import
       update_batter.plus_k_per_pa2020 = plus_k_per_pa2020_import
       update_batter.r_per_pa2020 = r_per_pa2020_import
       update_batter.rbi_per_pa2020 = rbi_per_pa2020_import
       update_batter.gdp_per_pa2020 = gdp_per_pa2020_import
       update_batter.xSB_added2020 = xSB_added2020_import
       update_batter.xSB_added_percent2020 = xSB_added_percent2020_import
       update_batter.wRAA2020 = wRAA2020_import
       update_batter.wOBA2020 = wOBA2020_import
       update_batter.wRC2020 = wRC2020_import
       update_batter.plus_wRC2020 = plus_wRC2020_import
       update_batter.iso2020 = iso2020_import
       update_batter.plus_iso2020 = plus_iso2020_import
       update_batter.babip2020 = babip2020_import
       update_batter.plus_babip2020 = plus_babip2020_import
       update_batter.ld_per_bip2020 = ld_per_bip2020_import
       # update_batter.plus_ld_per_bip2020 = plus_ld_per_bip2020_import, #note: seems to be messed up
       update_batter.gb_per_bip2020 = gb_per_bip2020_import
       update_batter.plus_gb_per_bip2020 = plus_gb_per_bip2020_import
       update_batter.fb_per_bip2020 = fb_per_bip2020_import
       update_batter.plus_fb_per_bip2020 = plus_fb_per_bip2020_import
       update_batter.iffb_per_bip2020 = iffb_per_bip2020_import
       update_batter.hr_per_fb2020 = hr_per_fb2020_import
       update_batter.plus_hr_per_fb2020 = plus_hr_per_fb2020_import
       update_batter.spd2020 = spd2020_import
       update_batter.bsr2020 = bsr2020_import
       update_batter.clutch2020 = clutch2020_import
       update_batter.fwar2020 = fwar2020_import
       update_batter.hardpercent2020 = hardpercent2020_import
       update_batter.plus_hardpercent2020 = plus_hardpercent2020_import
       #update_batter.barrel_percent2020 = barrel_percent2020_import
       #update_batter.maxEV2020= maxEV2020_import
       update_batter.hardhitpercent2020 = hardhitpercent2020_import
       #update_batter.xBA2020 = xBA2020_import
       #update_batter.fgxSLG2020 = fgxSLG2020_import
       #update_batter.fgxWOBA2020 = fgxWOBA2020_import
       update_batter.loaded_2020 = True
       update_batter.fwar_per_pa2020 = fwar_per_pa2020_import
       update_batter.bsr_per_pa2020 = bsr_per_pa2020_import
       update_batter.outsidezoneswingpercent2020 = outsidezoneswingpercent2020_import
       update_batter.firstpitchstrikepercent2020 = firstpitchstrikepercent2020_import
       update_batter.swingcontactpercent2020 = swingcontactpercent2020_import
       update_batter.swingingstrikespercent2020 = swingingstrikespercent2020_import
       update_batter.foff2020 = foff2020_import
       update_batter.fdef2020 = fdef2020_import
       update_batter.foff_per_pa2020 = foff_per_pa2020_import
       update_batter.fdef_per_pa2020 = fdef_per_pa2020_import
       update_batter.ffld2020 = ffld2020_import
       update_batter.fbat2020 = fbat2020_import
       update_batter.ffld_per_pa2020 = ffld_per_pa2020_import
       update_batter.fbat_per_pa2020 = fbat_per_pa2020_import
       update_batter.fldloaded_2020 = fldloaded_2020_import
       update_batter.loaded_hr_per_fb2020 = loaded_hr_per_fb2020_import
 
       # save the updates
       update_batter.save()
 
     #if the batter did not exist in the 2022 data pull, we must create the batter now
     else:
       new_batter = batter(
       fangraphs_id = fangraphs_id_check_2020,
       pa2020=pa2020_import,
       loaded_2020 = True,
       teamname = teamname_import,
       lastname = lastname_import,
       firstname = firstname_import,
       avg2020 = avg2020_import,
       plus_avg2020 = plus_avg2020_import,
       obp2020 = obp2020_import,
       plus_obp2020 = plus_obp2020_import,
       slg2020 = slg2020_import,
       plus_slg2020 = plus_slg2020_import,
       ops2020 = ops2020_import,
       bb_per_pa2020 = bb_per_pa2020_import,
       plus_bb_per_pa2020 = plus_bb_per_pa2020_import,
       k_per_pa2020 = k_per_pa2020_import,
       plus_k_per_pa2020 = plus_k_per_pa2020_import,
       r_per_pa2020 = r_per_pa2020_import,
       rbi_per_pa2020 = rbi_per_pa2020_import,
       gdp_per_pa2020 = gdp_per_pa2020_import,
       xSB_added2020 = xSB_added2020_import,
       xSB_added_percent2020 = xSB_added_percent2020_import,
       wRAA2020 = wRAA2020_import,
       wOBA2020 = wOBA2020_import,
       wRC2020 = wRC2020_import,
       plus_wRC2020 = plus_wRC2020_import,
       iso2020 = iso2020_import,
       plus_iso2020 = plus_iso2020_import,
       babip2020 = babip2020_import,
       plus_babip2020 = plus_babip2020_import,
       ld_per_bip2020 = ld_per_bip2020_import,
       # # plus_ld_per_bip2020 = plus_ld_per_bip2020_import, #note: seems to be messed up
       gb_per_bip2020 = gb_per_bip2020_import,
       plus_gb_per_bip2020 = plus_gb_per_bip2020_import,
       fb_per_bip2020 = fb_per_bip2020_import,
       plus_fb_per_bip2020 = plus_fb_per_bip2020_import,
       iffb_per_bip2020 = iffb_per_bip2020_import,
       hr_per_fb2020 = hr_per_fb2020_import,
       plus_hr_per_fb2020 = plus_hr_per_fb2020_import,
       spd2020 = spd2020_import,
       bsr2020 = bsr2020_import,
       clutch2020 = clutch2020_import,
       fwar2020 = fwar2020_import,
       hardpercent2020 = hardpercent2020_import,
       plus_hardpercent2020 = plus_hardpercent2020_import,
       #barrel_percent2020 = barrel_percent2020_import,
       #maxEV2020 = maxEV2020_import,
       hardhitpercent2020 = hardhitpercent2020_import,
       #xBA2020 = xBA2020_import,
       #fgxSLG2020 = fgxSLG2020_import,
       #fgxWOBA2020 = fgxWOBA2020_import,
       fwar_per_pa2020 = fwar_per_pa2020_import,
       bsr_per_pa2020 = bsr_per_pa2020_import,
       outsidezoneswingpercent2020 = outsidezoneswingpercent2020_import,
       firstpitchstrikepercent2020 = firstpitchstrikepercent2020_import,
       swingcontactpercent2020 = swingcontactpercent2020_import,
       swingingstrikespercent2020 = swingingstrikespercent2020_import,
       foff2020 = foff2020_import,
       fdef2020 = fdef2020_import,
       foff_per_pa2020 = foff_per_pa2020_import,
       fdef_per_pa2020 = fdef_per_pa2020_import,
       ffld2020 = ffld2020_import,
       fbat2020 = fbat2020_import,
       ffld_per_pa2020 = ffld_per_pa2020_import,
       fbat_per_pa2020 = fbat_per_pa2020_import,
       fldloaded_2020 = fldloaded_2020_import,
       loaded_hr_per_fb2020 = loaded_hr_per_fb2020_import
       )
       new_batter.save()
    

    #load player_ids for each of the websites for each batter
    for iterate_batter in batter.objects.all():
      #fg_id = [iterate_batter.fangraphs_id]
      my_list = []
      my_list.append(iterate_batter.fangraphs_id)
      #my_list.append(14344)
      if len(my_list) == 1 and (iterate_batter.loaded_2021 or iterate_batter.loaded_2020): 
        # notice: pybaseball is currently returning error for players who have only played in 2022, 
        # hence the conditions where a batter must have 2020/2021 stats to gather the different id's from all the websites
        all_ids = playerid_reverse_lookup(my_list, key_type='fangraphs')
        iterate_batter.key_bbref = all_ids.iat[0,4]
        iterate_batter.key_retro = all_ids.iat[0,3]
        iterate_batter.key_mlbam = all_ids.iat[0,2]
        iterate_batter.save()



    #skip load baseball ref basic data, nothing there that isn't covered by fangraphs
    #load bwar_bat
    data = bwar_bat(2022)
    data = data[(data.year_ID >= 2020) & (data.PA >= 30)]
    data_2022 = data[(data.year_ID == 2022)]
    data_2021 = data[(data.year_ID == 2021) & (data.PA >= 45)] # matches the qual from fangraphs for 2021
    data_2020 = data[(data.year_ID == 2020) & (data.PA >= 45)] # matches the qual from fangraphs for 2020
    number_of_players_2022 = data_2022.shape[0]
    number_of_players_2021 = data_2021.shape[0]
    number_of_players_2020 = data_2020.shape[0]

    # 2022 stats
    for x in range(number_of_players_2022):
      pa_check_for_rookies_import_2022 = float(data_2022.iat[x,8]) # a way of synchronizing data for the rookies where reverse id lookup does not work, currently not being employed
      year_import_2022 = data_2022.iat[x,4]
      full_name_2022 = data_2022.iat[x,0].split(" ")
      firstname_import_2022 = full_name_2022[0]
      lastname_import_2022 = full_name_2022[1]
      key_mlbam_import_2022 = data_2022.iat[x,2]
      key_bbref_import_2022 = data_2022.iat[x,3]
      bref_batting_runs_import_2022 = data_2022.iat[x,11]
      bref_bsr_runs_import_2022 = data_2022.iat[x,12]
      bref_gdp_runs_import_2022 = data_2022.iat[x,13] # Runs added or lost due to Grounding into Double Plays in DP situations
      bref_runs_above_avg_import_2022 = data_2022.iat[x,24]
      bref_runs_above_avg_def_import_2022 = data_2022.iat[x,26]
      bref_runs_above_avg_off_import_2022 = data_2022.iat[x,25]
      bref_war_import_2022 = data_2022.iat[x,30]
      bref_war_def_import_2022 = data_2022.iat[x,31]
      bref_war_off_import_2022 = data_2022.iat[x,32]
      plus_ops_import_2022 = data_2022.iat[x,46]
      # per pa
      bref_batting_runs_per_pa_import_2022 = bref_batting_runs_import_2022 / pa_check_for_rookies_import_2022
      bref_bsr_runs_per_pa_import_2022 = bref_bsr_runs_import_2022 / pa_check_for_rookies_import_2022
      bref_gdp_runs_per_pa_import_2022 = bref_gdp_runs_import_2022 / pa_check_for_rookies_import_2022
      bref_runs_above_avg_per_pa_import_2022 = bref_runs_above_avg_import_2022 / pa_check_for_rookies_import_2022
      bref_runs_above_avg_def_per_pa_import_2022 = bref_runs_above_avg_def_import_2022 / pa_check_for_rookies_import_2022
      bref_runs_above_avg_off_per_pa_import_2022 = bref_runs_above_avg_off_import_2022 / pa_check_for_rookies_import_2022
      bref_war_per_pa_import_2022 = bref_war_import_2022 / pa_check_for_rookies_import_2022
      bref_war_def_per_pa_import_2022 = bref_war_def_import_2022 / pa_check_for_rookies_import_2022
      bref_war_off_per_pa_import_2022 = bref_war_off_import_2022 / pa_check_for_rookies_import_2022
      # find the batter and load in the stats
      if batter.objects.filter(key_mlbam = key_mlbam_import_2022).exists():
        iterate_batter = batter.objects.get(key_mlbam = key_mlbam_import_2022)
        # update all the stats
        iterate_batter.bref_batting_runs2022 = bref_batting_runs_import_2022
        iterate_batter.bref_bsr_runs2022 = bref_bsr_runs_import_2022
        iterate_batter.bref_gdp_runs2022 = bref_gdp_runs_import_2022
        iterate_batter.bref_runs_above_avg2022 = bref_runs_above_avg_import_2022
        iterate_batter.bref_runs_above_avg_def2022 = bref_runs_above_avg_def_import_2022
        iterate_batter.bref_runs_above_avg_off2022 = bref_runs_above_avg_off_import_2022
        iterate_batter.bref_war2022 = bref_war_import_2022
        iterate_batter.bref_war_def2022 = bref_war_def_import_2022
        iterate_batter.bref_war_off2022 = bref_war_off_import_2022
        iterate_batter.plus_ops2022 = plus_ops_import_2022
        iterate_batter.bref_batting_runs_per_pa2022 = bref_batting_runs_per_pa_import_2022
        iterate_batter.bref_bsr_runs_per_pa2022 = bref_bsr_runs_per_pa_import_2022
        iterate_batter.bref_gdp_runs_per_pa2022 = bref_gdp_runs_per_pa_import_2022
        iterate_batter.bref_runs_above_avg_per_pa2022 = bref_runs_above_avg_per_pa_import_2022
        iterate_batter.bref_runs_above_avg_def_per_pa2022 = bref_runs_above_avg_def_per_pa_import_2022
        iterate_batter.bref_runs_above_avg_off_per_pa2022 = bref_runs_above_avg_off_per_pa_import_2022
        iterate_batter.bref_war_per_pa2022 = bref_war_per_pa_import_2022
        iterate_batter.bref_war_def_per_pa2022 = bref_war_def_per_pa_import_2022
        iterate_batter.bref_war_off_per_pa2022 = bref_war_off_per_pa_import_2022
        iterate_batter.loaded_bref_2022 = True
        iterate_batter.save()
      # if the player is a rookie and their ID is not currently loaded
      else: 
        try:
          iterate_batter = batter.objects.get(lastname = lastname_import_2022, firstname = firstname_import_2022)
          # udpate id's
          iterate_batter.key_bbref = key_bbref_import_2022
          iterate_batter.key_mlbam = key_mlbam_import_2022
          # everything else as normal
          iterate_batter.bref_batting_runs2022 = bref_batting_runs_import_2022
          iterate_batter.bref_bsr_runs2022 = bref_bsr_runs_import_2022
          iterate_batter.bref_gdp_runs2022 = bref_gdp_runs_import_2022
          iterate_batter.bref_runs_above_avg2022 = bref_runs_above_avg_import_2022
          iterate_batter.bref_runs_above_avg_def2022 = bref_runs_above_avg_def_import_2022
          iterate_batter.bref_runs_above_avg_off2022 = bref_runs_above_avg_off_import_2022
          iterate_batter.bref_war2022 = bref_war_import_2022
          iterate_batter.bref_war_def2022 = bref_war_def_import_2022
          iterate_batter.bref_war_off2022 = bref_war_off_import_2022
          iterate_batter.plus_ops2022 = plus_ops_import_2022
          iterate_batter.bref_batting_runs_per_pa2022 = bref_batting_runs_per_pa_import_2022
          iterate_batter.bref_bsr_runs_per_pa2022 = bref_bsr_runs_per_pa_import_2022
          iterate_batter.bref_gdp_runs_per_pa2022 = bref_gdp_runs_per_pa_import_2022
          iterate_batter.bref_runs_above_avg_per_pa2022 = bref_runs_above_avg_per_pa_import_2022
          iterate_batter.bref_runs_above_avg_def_per_pa2022 = bref_runs_above_avg_def_per_pa_import_2022
          iterate_batter.bref_runs_above_avg_off_per_pa2022 = bref_runs_above_avg_off_per_pa_import_2022
          iterate_batter.bref_war_per_pa2022 = bref_war_per_pa_import_2022
          iterate_batter.bref_war_def_per_pa2022 = bref_war_def_per_pa_import_2022
          iterate_batter.bref_war_off_per_pa2022 = bref_war_off_per_pa_import_2022
          iterate_batter.loaded_bref_2022 = True
          #get retro id as well
          # my_list = []
          # my_list.append(iterate_batter.key_bbref)
          # all_ids = playerid_reverse_lookup(my_list, key_type='bbref')
          # iterate_batter.key_retro = all_ids.iat[0,3]
          iterate_batter.save()
        except update_batter.DoesNotExist:
          #print("updating DNE" + lastname_import_2022 + " " + firstname_import_2022)
          k = 2









    # 2021 stats
    for x in range(number_of_players_2021):
     pa_check_for_rookies_import_2021 = float(data_2021.iat[x,8])
     year_import_2021 = data_2021.iat[x,4]
     full_name_2021 = data_2021.iat[x,0].split(" ")
     firstname_import_2021 = full_name_2021[0]
     lastname_import_2021 = full_name_2021[1]
     mlb_id_import_2021 = data_2021.iat[x,2]
     bbref_id_import_2021 = data_2021.iat[x,3]
     bref_batting_runs_import_2021 = data_2021.iat[x,11]
     bref_bsr_runs_import_2021 = data_2021.iat[x,12]
     bref_gdp_runs_import_2021 = data_2021.iat[x,13] # Runs added or lost due to Grounding into Double Plays in DP situations
     bref_runs_above_avg_import_2021 = data_2021.iat[x,24]
     bref_runs_above_avg_def_import_2021 = data_2021.iat[x,26]
     bref_runs_above_avg_off_import_2021 = data_2021.iat[x,25]
     bref_war_import_2021 = data_2021.iat[x,30]
     bref_war_def_import_2021 = data_2021.iat[x,31]
     bref_war_off_import_2021 = data_2021.iat[x,32]
     plus_ops_import_2021 = data_2021.iat[x,46]
     # per pa
     bref_batting_runs_per_pa_import_2021 = bref_batting_runs_import_2021 / pa_check_for_rookies_import_2021
     bref_bsr_runs_per_pa_import_2021 = bref_bsr_runs_import_2021 / pa_check_for_rookies_import_2021
     bref_gdp_runs_per_pa_import_2021 = bref_gdp_runs_import_2021 / pa_check_for_rookies_import_2021
     bref_runs_above_avg_per_pa_import_2021 = bref_runs_above_avg_import_2021 / pa_check_for_rookies_import_2021
     bref_runs_above_avg_def_per_pa_import_2021 = bref_runs_above_avg_def_import_2021 / pa_check_for_rookies_import_2021
     bref_runs_above_avg_off_per_pa_import_2021 = bref_runs_above_avg_off_import_2021 / pa_check_for_rookies_import_2021
     bref_war_per_pa_import_2021 = bref_war_import_2021 / pa_check_for_rookies_import_2021
     bref_war_def_per_pa_import_2021 = bref_war_def_import_2021 / pa_check_for_rookies_import_2021
     bref_war_off_per_pa_import_2021 = bref_war_off_import_2021 / pa_check_for_rookies_import_2021
     # find the batter and load in the stats
     if batter.objects.filter(key_mlbam = mlb_id_import_2021).exists():
      #print("updating veteran " + lastname_import_2021 + " " + firstname_import_2021)
      iterate_batter= batter.objects.get(key_mlbam = mlb_id_import_2021)
       # update all the stats
      iterate_batter.bref_batting_runs2021 = bref_batting_runs_import_2021
      iterate_batter.bref_bsr_runs2021 = bref_bsr_runs_import_2021
      iterate_batter.bref_gdp_runs2021 = bref_gdp_runs_import_2021
      iterate_batter.bref_runs_above_avg2021 = bref_runs_above_avg_import_2021
      iterate_batter.bref_runs_above_avg_def2021 = bref_runs_above_avg_def_import_2021
      iterate_batter.bref_runs_above_avg_off2021 = bref_runs_above_avg_off_import_2021
      iterate_batter.bref_war2021 = bref_war_import_2021
      iterate_batter.bref_war_def2021 = bref_war_def_import_2021
      iterate_batter.bref_war_off2021 = bref_war_off_import_2021
      iterate_batter.plus_ops2021 = plus_ops_import_2021
      iterate_batter.bref_batting_runs_per_pa2021 = bref_batting_runs_per_pa_import_2021
      iterate_batter.bref_bsr_runs_per_pa2021 = bref_bsr_runs_per_pa_import_2021
      iterate_batter.bref_gdp_runs_per_pa2021 = bref_gdp_runs_per_pa_import_2021
      iterate_batter.bref_runs_above_avg_per_pa2021 = bref_runs_above_avg_per_pa_import_2021
      iterate_batter.bref_runs_above_avg_def_per_pa2021 = bref_runs_above_avg_def_per_pa_import_2021
      iterate_batter.bref_runs_above_avg_off_per_pa2021 = bref_runs_above_avg_off_per_pa_import_2021
      iterate_batter.bref_war_per_pa2021 = bref_war_per_pa_import_2021
      iterate_batter.bref_war_def_per_pa2021 = bref_war_def_per_pa_import_2021
      iterate_batter.bref_war_off_per_pa2021 = bref_war_off_per_pa_import_2021
      iterate_batter.loaded_bref_2021 = True
      iterate_batter.save()


    # 2020 stats
    for x in range(number_of_players_2020):
     pa_check_for_rookies_import_2020 = float(data_2020.iat[x,8])
     year_import_2020 = data_2020.iat[x,4]
     full_name_2020 = data_2020.iat[x,0].split(" ")
     firstname_import_2020 = full_name_2020[0]
     lastname_import_2020 = full_name_2020[1]
     mlb_id_import_2020 = data_2020.iat[x,2]
     bbref_id_import_2020 = data_2020.iat[x,3]
     bref_batting_runs_import_2020 = data_2020.iat[x,11]
     bref_bsr_runs_import_2020 = data_2020.iat[x,12]
     bref_gdp_runs_import_2020 = data_2020.iat[x,13] # Runs added or lost due to Grounding into Double Plays in DP situations
     bref_runs_above_avg_import_2020 = data_2020.iat[x,24]
     bref_runs_above_avg_def_import_2020 = data_2020.iat[x,26]
     bref_runs_above_avg_off_import_2020 = data_2020.iat[x,25]
     bref_war_import_2020 = data_2020.iat[x,30]
     bref_war_def_import_2020 = data_2020.iat[x,31]
     bref_war_off_import_2020 = data_2020.iat[x,32]
     plus_ops_import_2020 = data_2020.iat[x,46]
     # per pa
     bref_batting_runs_per_pa_import_2020 = bref_batting_runs_import_2020 / pa_check_for_rookies_import_2020
     bref_bsr_runs_per_pa_import_2020 = bref_bsr_runs_import_2020 / pa_check_for_rookies_import_2020
     bref_gdp_runs_per_pa_import_2020 = bref_gdp_runs_import_2020 / pa_check_for_rookies_import_2020
     bref_runs_above_avg_per_pa_import_2020 = bref_runs_above_avg_import_2020 / pa_check_for_rookies_import_2020
     bref_runs_above_avg_def_per_pa_import_2020 = bref_runs_above_avg_def_import_2020 / pa_check_for_rookies_import_2020
     bref_runs_above_avg_off_per_pa_import_2020 = bref_runs_above_avg_off_import_2020 / pa_check_for_rookies_import_2020
     bref_war_per_pa_import_2020 = bref_war_import_2020 / pa_check_for_rookies_import_2020
     bref_war_def_per_pa_import_2020 = bref_war_def_import_2020 / pa_check_for_rookies_import_2020
     bref_war_off_per_pa_import_2020 = bref_war_off_import_2020 / pa_check_for_rookies_import_2020
     # find the batter and load in the stats
     if batter.objects.filter(key_mlbam = mlb_id_import_2020).exists():
      #print("updating veteran " + lastname_import_2021 + " " + firstname_import_2021)
      iterate_batter= batter.objects.get(key_mlbam = mlb_id_import_2020)
       # update all the stats
      iterate_batter.bref_batting_runs2020 = bref_batting_runs_import_2020
      iterate_batter.bref_bsr_runs2020 = bref_bsr_runs_import_2020
      iterate_batter.bref_gdp_runs2020 = bref_gdp_runs_import_2020
      iterate_batter.bref_runs_above_avg2020 = bref_runs_above_avg_import_2020
      iterate_batter.bref_runs_above_avg_def2020 = bref_runs_above_avg_def_import_2020
      iterate_batter.bref_runs_above_avg_off2020 = bref_runs_above_avg_off_import_2020
      iterate_batter.bref_war2020 = bref_war_import_2020
      iterate_batter.bref_war_def2020 = bref_war_def_import_2020
      iterate_batter.bref_war_off2020 = bref_war_off_import_2020
      iterate_batter.plus_ops2020 = plus_ops_import_2020
      iterate_batter.bref_batting_runs_per_pa2020 = bref_batting_runs_per_pa_import_2020
      iterate_batter.bref_bsr_runs_per_pa2020 = bref_bsr_runs_per_pa_import_2020
      iterate_batter.bref_gdp_runs_per_pa2020 = bref_gdp_runs_per_pa_import_2020
      iterate_batter.bref_runs_above_avg_per_pa2020 = bref_runs_above_avg_per_pa_import_2020
      iterate_batter.bref_runs_above_avg_def_per_pa2020 = bref_runs_above_avg_def_per_pa_import_2020
      iterate_batter.bref_runs_above_avg_off_per_pa2020 = bref_runs_above_avg_off_per_pa_import_2020
      iterate_batter.bref_war_per_pa2020 = bref_war_per_pa_import_2020
      iterate_batter.bref_war_def_per_pa2020 = bref_war_def_per_pa_import_2020
      iterate_batter.bref_war_off_per_pa2020 = bref_war_off_per_pa_import_2020
      iterate_batter.loaded_bref_2020 = True
      iterate_batter.save()
    



    #baseball savant
    # expected 2022
    data_2022_expected = statcast_batter_expected_stats(2022, 20)
    number_of_players_2022 = data_2022_expected.shape[0]
    for x in range(number_of_players_2022):
      key_mlbam_check_2022 = data_2022_expected.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2022)
        bip2022_import = float(data_2022_expected.iat[x,5])
        xavg2022_import = data_2022_expected.iat[x,7]
        xavgdiff2022_import = data_2022_expected.iat[x,8]
        xslg2022_import = data_2022_expected.iat[x,10]
        xslgdiff2022_import = data_2022_expected.iat[x,11]
        xwoba2022_import = data_2022_expected.iat[x,13]
        xwobadiff2022_import = data_2022_expected.iat[x,14]
        update_batter.bip2022 = bip2022_import
        update_batter.xavg2022 = xavg2022_import
        update_batter.xavgdiff2022 = xavgdiff2022_import
        update_batter.xslg2022 = xslg2022_import
        update_batter.xslgdiff2022 = xslgdiff2022_import
        update_batter.xwoba2022 = xwoba2022_import
        update_batter.xwobadiff2022 = xwobadiff2022_import
        update_batter.loaded_bs_x_2022 = True
        update_batter.save()
        
    #barrel 2022
    data_2022_barrel = statcast_batter_exitvelo_barrels(2022, 20)
    number_of_players_2022 = data_2022_barrel.shape[0]
    for x in range(number_of_players_2022):
      key_mlbam_check_2022 = data_2022_barrel.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2022)
        anglesweetspotpercent2022_import = data_2022_barrel.iat[x,5] / 100
        max_hit_speed2022_import = float(data_2022_barrel.iat[x,6])
        avg_hit_speed2022_import = float(data_2022_barrel.iat[x,7])
        max_distance2022_import = float(data_2022_barrel.iat[x,10])
        avg_distance2022_import = float(data_2022_barrel.iat[x,11])
        ev95percent2022_import = float(data_2022_barrel.iat[x,14]) / 100
        brl_percent2022_import = float(data_2022_barrel.iat[x,16]) / 100
        brl_pa2022_import = float(data_2022_barrel.iat[x,17])
        update_batter.anglesweetspotpercent2022 = anglesweetspotpercent2022_import
        update_batter.max_hit_speed2022 = max_hit_speed2022_import
        update_batter.avg_hit_speed2022 = avg_hit_speed2022_import
        update_batter.max_distance2022 = max_distance2022_import
        update_batter.avg_distance2022 = avg_distance2022_import
        update_batter.ev95percent2022 = ev95percent2022_import
        update_batter.brl_percent2022 = brl_percent2022_import
        update_batter.brl_pa2022 = brl_pa2022_import
        update_batter.loaded_bs_barrel_2022 = True
        update_batter.save()



    # expected 2021
    data_2021_expected = statcast_batter_expected_stats(2021, 20)
    number_of_players_2021 = data_2021_expected.shape[0]
    for x in range(number_of_players_2021):
      key_mlbam_check_2021 = data_2021_expected.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2021).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2021)
        bip2021_import = float(data_2021_expected.iat[x,5])
        xavg2021_import = float(data_2021_expected.iat[x,7])
        xavgdiff2021_import = float(data_2021_expected.iat[x,8])
        xslg2021_import = float(data_2021_expected.iat[x,10])
        xslgdiff2021_import = data_2021_expected.iat[x,11]
        xwoba2021_import = data_2021_expected.iat[x,13]
        xwobadiff2021_import = data_2021_expected.iat[x,14]
        update_batter.bip2021 = bip2021_import
        update_batter.xavg2021 = xavg2021_import
        update_batter.xavgdiff2021 = xavgdiff2021_import
        update_batter.xslg2021 = xslg2021_import
        update_batter.xslgdiff2021 = xslgdiff2021_import
        update_batter.xwoba2021 = xwoba2021_import
        update_batter.xwobadiff2021 = xwobadiff2021_import
        update_batter.loaded_bs_x_2021 = True
        update_batter.save()
        
    #barrel 2021
    data_2021_barrel = statcast_batter_exitvelo_barrels(2021, 20)
    number_of_players_2021 = data_2021_barrel.shape[0]
    for x in range(number_of_players_2021):
      key_mlbam_check_2021 = data_2021_barrel.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2021).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2021)
        anglesweetspotpercent2021_import = data_2021_barrel.iat[x,5] / 100
        max_hit_speed2021_import = float(data_2021_barrel.iat[x,6])
        avg_hit_speed2021_import = float(data_2021_barrel.iat[x,7])
        max_distance2021_import = float(data_2021_barrel.iat[x,10])
        avg_distance2021_import = float(data_2021_barrel.iat[x,11])
        ev95percent2021_import = data_2021_barrel.iat[x,14] / 100
        brl_percent2021_import = data_2021_barrel.iat[x,16] / 100
        brl_pa2021_import = float(data_2021_barrel.iat[x,17])
        update_batter.anglesweetspotpercent2021 = anglesweetspotpercent2021_import
        update_batter.max_hit_speed2021 = max_hit_speed2021_import
        update_batter.avg_hit_speed2021 = avg_hit_speed2021_import
        update_batter.max_distance2021 = max_distance2021_import
        update_batter.avg_distance2021 = avg_distance2021_import
        update_batter.ev95percent2021 = ev95percent2021_import
        update_batter.brl_percent2021 = brl_percent2021_import
        update_batter.brl_pa2021 = brl_pa2021_import
        update_batter.loaded_bs_barrel_2021 = True
        update_batter.save()



    # expected 2020
    data_2020_expected = statcast_batter_expected_stats(2020, 20)
    number_of_players_2020 = data_2020_expected.shape[0]
    for x in range(number_of_players_2020):
      key_mlbam_check_2020 = data_2020_expected.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2020).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2020)
        bip2020_import = float(data_2020_expected.iat[x,5])
        xavg2020_import = data_2020_expected.iat[x,7]
        xavgdiff2020_import = data_2020_expected.iat[x,8]
        xslg2020_import = data_2020_expected.iat[x,10]
        xslgdiff2020_import = data_2020_expected.iat[x,11]
        xwoba2020_import = data_2020_expected.iat[x,13]
        xwobadiff2020_import = data_2020_expected.iat[x,14]
        update_batter.bip2020 = bip2020_import
        update_batter.xavg2020 = xavg2020_import
        update_batter.xavgdiff2020 = xavgdiff2020_import
        update_batter.xslg2020 = xslg2020_import
        update_batter.xslgdiff2020 = xslgdiff2020_import
        update_batter.xwoba2020 = xwoba2020_import
        update_batter.xwobadiff2020 = xwobadiff2020_import
        update_batter.loaded_bs_x_2020 = True
        update_batter.save()
        
    #barrel 2020
    data_2020_barrel = statcast_batter_exitvelo_barrels(2020, 20)
    number_of_players_2020 = data_2020_barrel.shape[0]
    for x in range(number_of_players_2020):
      key_mlbam_check_2020 = data_2020_barrel.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2020).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2020)
        anglesweetspotpercent2020_import = data_2020_barrel.iat[x,5] / 100
        max_hit_speed2020_import = float(data_2020_barrel.iat[x,6])
        avg_hit_speed2020_import = float(data_2020_barrel.iat[x,7])
        max_distance2020_import = float(data_2020_barrel.iat[x,10])
        avg_distance2020_import = float(data_2020_barrel.iat[x,11])
        ev95percent2020_import = data_2020_barrel.iat[x,14] / 100
        brl_percent2020_import = data_2020_barrel.iat[x,16]  / 100
        brl_pa2020_import = float(data_2020_barrel.iat[x,17])
        update_batter.anglesweetspotpercent2020 = anglesweetspotpercent2020_import
        update_batter.max_hit_speed2020 = max_hit_speed2020_import
        update_batter.avg_hit_speed2020 = avg_hit_speed2020_import
        update_batter.max_distance2020 = max_distance2020_import
        update_batter.avg_distance2020 = avg_distance2020_import
        update_batter.ev95percent2020 = ev95percent2020_import
        update_batter.brl_percent2020 = brl_percent2020_import
        update_batter.brl_pa2020 = brl_pa2020_import
        update_batter.loaded_bs_barrel_2020 = True
        update_batter.save()

    #baseball savant fielding 2022
    data_2022_fielding = statcast_outs_above_average(2022, pos = "all", min_att = 20)
    number_of_players_2022 = data_2022_fielding.shape[0]
    for x in range(number_of_players_2022):
      key_mlbam_check_2022 = data_2022_fielding.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2022)
        outs_above_avg2022_import = float(data_2022_fielding.iat[x,7])
        fielding_runs_prevented2022_import = float(data_2022_fielding.iat[x,6])
        update_batter.outs_above_avg2022 = outs_above_avg2022_import
        update_batter.fielding_runs_prevented2022 = fielding_runs_prevented2022_import
        update_batter.loaded_bs_fielding_2022 = True
        update_batter.save()

    #baseball savant fielding 2021
    data_2021_fielding = statcast_outs_above_average(2021, pos = "all", min_att = 20)
    number_of_players_2021 = data_2021_fielding.shape[0]
    for x in range(number_of_players_2021):
      key_mlbam_check_2021 = data_2021_fielding.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2021).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2021)
        outs_above_avg2021_import = float(data_2021_fielding.iat[x,7])
        fielding_runs_prevented2021_import = float(data_2021_fielding.iat[x,6])
        update_batter.outs_above_avg2021 = outs_above_avg2021_import
        update_batter.fielding_runs_prevented2021 = fielding_runs_prevented2021_import
        update_batter.loaded_bs_fielding_2021 = True
        update_batter.save()

    #baseball savant fielding 2020
    data_2020_fielding = statcast_outs_above_average(2020, pos = "all", min_att = 20)
    number_of_players_2020 = data_2020_fielding.shape[0]
    for x in range(number_of_players_2020):
      key_mlbam_check_2020 = data_2020_fielding.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2020).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2020)
        outs_above_avg2020_import = float(data_2020_fielding.iat[x,7])
        fielding_runs_prevented2020_import = float(data_2020_fielding.iat[x,6])
        update_batter.outs_above_avg2020 = outs_above_avg2020_import
        update_batter.fielding_runs_prevented2020 = fielding_runs_prevented2020_import
        update_batter.loaded_bs_fielding_2020 = True
        update_batter.save()
 

    #baseball savant running 2022
    data_2022_running = statcast_sprint_speed(2022, 20)
    number_of_players_2022 = data_2022_running.shape[0]
    for x in range(number_of_players_2022):
      key_mlbam_check_2022 = data_2022_running.iat[x,2]
      if batter.objects.filter(key_mlbam = key_mlbam_check_2022).exists():
        update_batter = batter.objects.get(key_mlbam = key_mlbam_check_2022)
        home_to_first2022_import = data_2022_running.iat[x,8]
        sprint_speed2022_import = float(data_2022_running.iat[x,9])
        if np.isnan(home_to_first2022_import):
          update_batter.loaded_bs_running_2022 = False
        else:
          update_batter.home_to_first2022 = float(home_to_first2022_import)
          update_batter.sprint_speed2022 = sprint_speed2022_import
          update_batter.loaded_bs_running_2022 = True
          update_batter.save()