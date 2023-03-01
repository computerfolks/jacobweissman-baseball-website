# also gonna need a function which gives a z-score for every category, only 2022 should be updated every day. in this, create dummy batter, which should be approximately 1.5 standard deviations below the league average for each batting statistic

# this code updates all the 2022 batters. it will run every day
# runtime 3:20
import decimal
from django.core.management.base import BaseCommand
from app_bb.models import batter
from pybaseball import *
import numpy as np
import matplotlib.pylab as plt
from pybaseball.statcast_batter import statcast_batter_expected_stats
from pybaseball.statcast_batter import statcast_batter_exitvelo_barrels
from pybaseball.statcast_fielding import statcast_outs_above_average
from pybaseball.statcast_running import statcast_sprint_speed

class Command(BaseCommand):
  def handle(self, *args, **options):
    if batter.objects.filter(lastname = "dummy").exists():
      batter.objects.filter(lastname = "dummy").delete()
    # UPDATE FANGRAPHS
    data_2022 = batting_stats(2022, qual = 30)
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
      if batter.objects.filter(fangraphs_id = fangraphs_id_import).exists():
        update_batter = batter.objects.get(fangraphs_id = fangraphs_id_import)
        #update batter
        update_batter.loaded_2022 = True
        update_batter.pa2022 = pa2022_import
        update_batter.avg2022 = avg2022_import
        update_batter.plus_avg2022 = plus_avg2022_import
        update_batter.obp2022 = obp2022_import
        update_batter.plus_obp2022 = plus_obp2022_import
        update_batter.slg2022 = slg2022_import
        update_batter.plus_slg2022 = plus_slg2022_import
        update_batter.ops2022 = ops2022_import
        update_batter.bb_per_pa2022 = bb_per_pa2022_import
        update_batter.plus_bb_per_pa2022 = plus_bb_per_pa2022_import
        update_batter.k_per_pa2022 = k_per_pa2022_import
        update_batter.plus_k_per_pa2022 = plus_k_per_pa2022_import
        update_batter.r_per_pa2022 = r_per_pa2022_import
        update_batter.rbi_per_pa2022 = rbi_per_pa2022_import
        update_batter.gdp_per_pa2022 = gdp_per_pa2022_import
        update_batter.xSB_added2022 = xSB_added2022_import
        update_batter.xSB_added_percent2022 = xSB_added_percent2022_import
        update_batter.wRAA2022 = wRAA2022_import
        update_batter.wOBA2022 = wOBA2022_import
        update_batter.wRC2022 = wRC2022_import
        update_batter.plus_wRC2022 = plus_wRC2022_import
        update_batter.iso2022 = iso2022_import
        update_batter.plus_iso2022 = plus_iso2022_import
        update_batter.babip2022 = babip2022_import
        update_batter.plus_babip2022 = plus_babip2022_import
        update_batter.ld_per_bip2022 = ld_per_bip2022_import
        # update_batter.plus_ld_per_bip2022 = plus_ld_per_bip2022_import, #note: seems to be messed up
        update_batter.gb_per_bip2022 = gb_per_bip2022_import
        update_batter.plus_gb_per_bip2022 = plus_gb_per_bip2022_import
        update_batter.fb_per_bip2022 = fb_per_bip2022_import
        update_batter.plus_fb_per_bip2022 = plus_fb_per_bip2022_import
        update_batter.iffb_per_bip2022 = iffb_per_bip2022_import
        update_batter.hr_per_fb2022 = hr_per_fb2022_import
        update_batter.plus_hr_per_fb2022 = plus_hr_per_fb2022_import
        update_batter.spd2022 = spd2022_import
        update_batter.bsr2022 = bsr2022_import
        update_batter.clutch2022 = clutch2022_import
        update_batter.fwar2022 = fwar2022_import
        update_batter.hardpercent2022 = hardpercent2022_import
        update_batter.plus_hardpercent2022 = plus_hardpercent2022_import
        #update_batter.barrel_percent2022 = barrel_percent2022_import
        #update_batter.maxEV2021= maxEV2022_import
        update_batter.hardhitpercent2022 = hardhitpercent2022_import
        #update_batter.xBA2022 = xBA2022_import
        #update_batter.fgxSLG2022 = fgxSLG2022_import
        #update_batter.fgxWOBA2022 = fgxWOBA2022_import
        update_batter.fwar_per_pa2022 = fwar_per_pa2022_import
        update_batter.bsr_per_pa2022 = bsr_per_pa2022_import
        update_batter.outsidezoneswingpercent2022 = outsidezoneswingpercent2022_import
        update_batter.firstpitchstrikepercent2022 = firstpitchstrikepercent2022_import
        update_batter.swingcontactpercent2022 = swingcontactpercent2022_import
        update_batter.swingingstrikespercent2022 = swingingstrikespercent2022_import
        update_batter.foff2022 = foff2022_import
        update_batter.fdef2022 = fdef2022_import
        update_batter.foff_per_pa2022 = foff_per_pa2022_import
        update_batter.fdef_per_pa2022 = fdef_per_pa2022_import
        update_batter.ffld2022 = ffld2022_import
        update_batter.fbat2022 = fbat2022_import
        update_batter.ffld_per_pa2022 = ffld_per_pa2022_import
        update_batter.fbat_per_pa2022 = fbat_per_pa2022_import
        update_batter.fldloaded_2022 = fldloaded_2022_import
        update_batter.loaded_hr_per_fb2022 = loaded_hr_per_fb2022_import
        update_batter.save()

      #we do not need to handle the case of a batter already in the database having taken AB's in 2020/2021, because their fangraphs ID would still have been loaded and the if statement would run
      #if the batter did not previously exist AT ALL because they did not have AB's, we must create the batter now
      else:
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

        


    # UPDATE BREF
    data = bwar_bat(2022)
    data_2022 = data[(data.year_ID == 2022) & (data.PA >= 30)]
    number_of_players_2022 = data_2022.shape[0]
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

    #update baseball savant
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
          