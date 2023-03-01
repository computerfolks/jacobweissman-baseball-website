import decimal
from django.core.management.base import BaseCommand
from app_bb.models import batter
from django.db.models.aggregates import StdDev, Avg

#copy and paste from 2022 except for last if statement with baserunning and bottom by hometofirst and sprintspeed

class Command(BaseCommand):
 def handle(self, *args, **options):
   if batter.objects.filter(lastname = "dummy").exists():
     batter.objects.filter(lastname = "dummy").delete()
   pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("pa2021"))
   pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("pa2021"))
   plus_avg2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_avg2021"))
   plus_avg2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_avg2021"))
   avg2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("avg2021"))
   avg2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("avg2021"))
   obp2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("obp2021"))
   obp2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("obp2021"))
   plus_obp2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_obp2021"))
   plus_obp2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_obp2021"))
   slg2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("slg2021"))
   slg2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("slg2021"))
   plus_slg2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_slg2021"))
   plus_slg2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_slg2021"))
   ops2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("ops2021"))
   ops2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("ops2021"))
   bb_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bb_per_pa2021"))
   bb_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("bb_per_pa2021"))
   plus_bb_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_bb_per_pa2021"))
   plus_bb_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_bb_per_pa2021"))
   plus_k_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_k_per_pa2021"))
   plus_k_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_k_per_pa2021"))
   k_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("k_per_pa2021"))
   k_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("k_per_pa2021"))
   r_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("r_per_pa2021"))
   r_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("r_per_pa2021"))
   rbi_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("rbi_per_pa2021"))
   rbi_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("rbi_per_pa2021"))
   gdp_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("gdp_per_pa2021"))
   gdp_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("gdp_per_pa2021"))
   xSB_added2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xSB_added2021"))
   xSB_added2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("xSB_added2021"))
   xSB_added_percent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xSB_added_percent2021"))
   xSB_added_percent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("xSB_added_percent2021"))
   wRAA2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("wRAA2021"))
   wRAA2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("wRAA2021"))
   wOBA2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("wOBA2021"))
   wOBA2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("wOBA2021"))
   wRC2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("wRC2021"))
   wRC2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("wRC2021"))
   plus_wRC2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_wRC2021"))
   plus_wRC2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_wRC2021"))
   iso2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("iso2021"))
   iso2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("iso2021"))
   plus_iso2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_iso2021"))
   plus_iso2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_iso2021"))
   babip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("babip2021"))
   babip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("babip2021"))
   plus_babip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_babip2021"))
   plus_babip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_babip2021"))
   ld_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("ld_per_bip2021"))
   ld_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("ld_per_bip2021"))
   gb_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("gb_per_bip2021"))
   gb_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("gb_per_bip2021"))
   fb_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fb_per_bip2021"))
   fb_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fb_per_bip2021"))
   iffb_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("iffb_per_bip2021"))
   iffb_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("iffb_per_bip2021"))
   hr_per_fb2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(loaded_hr_per_fb2021 = True).aggregate(StdDev("hr_per_fb2021"))
   hr_per_fb2021mean = batter.objects.all().filter(loaded_2021 = True).filter(loaded_hr_per_fb2021 = True).aggregate(Avg("hr_per_fb2021"))
   bsr2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bsr2021"))
   # print("baserunning total", bsr2021stddev) 1.47900609072223
   bsr2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("bsr2021"))
   # print("baserunning mean", bsr2021mean) 0
   clutch2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("clutch2021"))
   clutch2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("clutch2021"))
   fwar2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fwar2021"))
   fwar2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fwar2021"))
   hardpercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hardpercent2021"))
   hardpercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("hardpercent2021"))
   plus_hardpercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_hardpercent2021"))
   plus_hardpercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_hardpercent2021"))
   hardhitpercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hardhitpercent2021"))
   hardhitpercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("hardhitpercent2021"))
   fwar_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fwar_per_pa2021"))
   fwar_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fwar_per_pa2021"))
   bsr_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bsr_per_pa2021"))
   # print("baserunning per pa", bsr_per_pa2021stddev) 0.00833214477662146
   bsr_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("bsr_per_pa2021"))
   outsidezoneswingpercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("outsidezoneswingpercent2021"))
   outsidezoneswingpercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("outsidezoneswingpercent2021"))
   firstpitchstrikepercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("firstpitchstrikepercent2021"))
   firstpitchstrikepercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("firstpitchstrikepercent2021"))
   swingcontactpercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("swingcontactpercent2021"))
   swingcontactpercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("swingcontactpercent2021"))
   swingingstrikespercent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("swingingstrikespercent2021"))
   swingingstrikespercent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("swingingstrikespercent2021"))
   foff2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("foff2021"))
   foff2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("foff2021"))
   fdef2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(StdDev("fdef2021"))
   # print("defense total", fdef2021stddev) 3.92625378652656
   fdef2021mean = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(Avg("fdef2021"))
   # print("defense mean", fdef2021mean) -0.485714285714286
   ffld2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(StdDev("ffld2021"))
   # print("fielding total", ffld2021stddev) 2.93118745254359
   ffld2021mean = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(Avg("ffld2021"))
   # print("fielding mean", ffld2021mean) 0.0409937888198759
   foff_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("foff_per_pa2021"))
   foff_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("foff_per_pa2021"))
   fdef_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(StdDev("fdef_per_pa2021"))
   # print("defense per pa", fdef_per_pa2021stddev) 0.0245836618867729
   fdef_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(Avg("fdef_per_pa2021"))
   fbat2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fbat2021"))
   # print("batting total", fbat2021stddev) 7.63961508130041
   fbat2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fbat2021"))
   # print("batting mean", fbat2021mean) 0.225819672131148
   ffld_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(StdDev("ffld_per_pa2021"))
   # print("fielding per pa", ffld_per_pa2021stddev) 0.0208832062380861
   ffld_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).filter(fldloaded_2021 = True).aggregate(Avg("ffld_per_pa2021"))
   # barrel_percent2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("barrel_percent2021"))
   # barrel_percent2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("barrel_percent2021"))
   fbat_per_pa2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fbat_per_pa2021"))
   # print("batting per pa", fbat_per_pa2021stddev) 0.0438921952567499
   fbat_per_pa2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fbat_per_pa2021"))
   # maxEV2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("maxEV2021"))
   # maxEV2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("maxEV2021"))
   plus_ld_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_ld_per_bip2021"))
   plus_ld_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_ld_per_bip2021"))
   plus_gb_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_gb_per_bip2021"))
   plus_gb_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_gb_per_bip2021"))
   plus_fb_per_bip2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_fb_per_bip2021"))
   plus_fb_per_bip2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_fb_per_bip2021"))
   spd2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("spd2021"))
   spd2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("spd2021"))
   plus_hr_per_fb2021stddev = batter.objects.all().filter(loaded_2021 = True).filter(loaded_hr_per_fb2021 = True).aggregate(StdDev("plus_hr_per_fb2021"))
   plus_hr_per_fb2021mean = batter.objects.all().filter(loaded_2021 = True).filter(loaded_hr_per_fb2021 = True).aggregate(Avg("plus_hr_per_fb2021"))
   # xBA2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xBA2021"))
   # xBA2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("xBA2021"))
   # fgxSLG2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fgxSLG2021"))
   # fgxSLG2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fgxSLG2021"))
   # fgxWOBA2021stddev = batter.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fgxWOBA2021"))
   # fgxWOBA2021mean = batter.objects.all().filter(loaded_2021 = True).aggregate(Avg("fgxWOBA2021"))
   bref_bsr_runs2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_bsr_runs2021"))
   bref_bsr_runs2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_bsr_runs2021"))
   bref_batting_runs2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_batting_runs2021"))
   bref_batting_runs2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_batting_runs2021"))
   bref_runs_above_avg2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg2021"))
   bref_runs_above_avg2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg2021"))
   bref_gdp_runs2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_gdp_runs2021"))
   bref_gdp_runs2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_gdp_runs2021"))
   bref_runs_above_avg_def2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg_def2021"))
   bref_runs_above_avg_def2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg_def2021"))
   bref_war2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war2021"))
   bref_war2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war2021"))
   bref_runs_above_avg_off2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg_off2021"))
   bref_runs_above_avg_off2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg_off2021"))
   bref_war_def2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war_def2021"))
   bref_war_def2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war_def2021"))
   bref_war_off2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war_off2021"))
   bref_war_off2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war_off2021"))
   plus_ops2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("plus_ops2021"))
   plus_ops2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("plus_ops2021"))
   bref_batting_runs_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_batting_runs_per_pa2021"))
   bref_batting_runs_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_batting_runs_per_pa2021"))
   bref_bsr_runs_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_bsr_runs_per_pa2021"))
   bref_bsr_runs_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_bsr_runs_per_pa2021"))
   bref_gdp_runs_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_gdp_runs_per_pa2021"))
   bref_gdp_runs_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_gdp_runs_per_pa2021"))
   bref_runs_above_avg_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg_per_pa2021"))
   bref_runs_above_avg_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg_per_pa2021"))
   bref_runs_above_avg_def_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg_def_per_pa2021"))
   bref_runs_above_avg_def_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg_def_per_pa2021"))
   bref_war_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war_per_pa2021"))
   bref_war_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war_per_pa2021"))
   bref_runs_above_avg_off_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_runs_above_avg_off_per_pa2021"))
   bref_runs_above_avg_off_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_runs_above_avg_off_per_pa2021"))
   bref_war_off_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war_off_per_pa2021"))
   bref_war_off_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war_off_per_pa2021"))
   bref_war_def_per_pa2021stddev = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(StdDev("bref_war_def_per_pa2021"))
   bref_war_def_per_pa2021mean = batter.objects.all().filter(loaded_bref_2021 = True).aggregate(Avg("bref_war_def_per_pa2021"))
   #baseball savant x
   xavg2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xavg2021"))
   xavg2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xavg2021"))
   bip2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("bip2021"))
   bip2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("bip2021"))
   xslg2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xslg2021"))
   xslg2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xslg2021"))
   xavgdiff2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xavgdiff2021"))
   xavgdiff2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xavgdiff2021"))
   xslgdiff2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xslgdiff2021"))
   xslgdiff2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xslgdiff2021"))
   xwobadiff2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xwobadiff2021"))
   xwobadiff2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xwobadiff2021"))
   xwoba2021stddev = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xwoba2021"))
   xwoba2021mean = batter.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xwoba2021"))
   #baseball savant barrel
   anglesweetspotpercent2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("anglesweetspotpercent2021"))
   anglesweetspotpercent2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("anglesweetspotpercent2021"))
   max_hit_speed2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("max_hit_speed2021"))
   max_hit_speed2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("max_hit_speed2021"))
   avg_hit_speed2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("avg_hit_speed2021"))
   avg_hit_speed2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("avg_hit_speed2021"))
   max_distance2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("max_distance2021"))
   max_distance2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("max_distance2021"))
   avg_distance2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("avg_distance2021"))
   avg_distance2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("avg_distance2021"))
   ev95percent2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("ev95percent2021"))
   ev95percent2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("ev95percent2021"))
   brl_percent2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("brl_percent2021"))
   brl_percent2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("brl_percent2021"))
   brl_pa2021stddev = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("brl_pa2021"))
   brl_pa2021mean = batter.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("brl_pa2021"))
  #  outs_above_avg2021stddev = batter.objects.all().filter(loaded_bs_fielding_2021 = True).aggregate(StdDev("outs_above_avg2021"))
  #  outs_above_avg2021mean = batter.objects.all().filter(loaded_bs_fielding_2021 = True).aggregate(Avg("outs_above_avg2021"))
  #  fielding_runs_prevented2021stddev = batter.objects.all().filter(loaded_bs_fielding_2021 = True).aggregate(StdDev("fielding_runs_prevented2021"))
  #  fielding_runs_prevented2021mean = batter.objects.all().filter(loaded_bs_fielding_2021 = True).aggregate(Avg("fielding_runs_prevented2021"))
 
   for zbatter in batter.objects.all().filter(loaded_2021 = True):
     zbatter.zpa2021 = (zbatter.pa2021 - pa2021mean["pa2021__avg"]) / pa2021stddev["pa2021__stddev"]
     zbatter.zplus_avg2021 = (zbatter.plus_avg2021 - plus_avg2021mean["plus_avg2021__avg"]) / plus_avg2021stddev["plus_avg2021__stddev"]
     zbatter.zavg2021 = (zbatter.avg2021 - avg2021mean["avg2021__avg"]) / avg2021stddev["avg2021__stddev"]
     zbatter.zobp2021 = (zbatter.obp2021 - obp2021mean["obp2021__avg"]) / obp2021stddev["obp2021__stddev"]
     zbatter.zplus_obp2021 = (zbatter.plus_obp2021 - plus_obp2021mean["plus_obp2021__avg"]) / plus_obp2021stddev["plus_obp2021__stddev"]
     zbatter.zslg2021 = (zbatter.slg2021 - slg2021mean["slg2021__avg"]) / slg2021stddev["slg2021__stddev"]
     zbatter.zplus_slg2021 = (zbatter.plus_slg2021 - plus_slg2021mean["plus_slg2021__avg"]) / plus_slg2021stddev["plus_slg2021__stddev"]
     zbatter.zops2021 = (zbatter.ops2021 - ops2021mean["ops2021__avg"]) / ops2021stddev["ops2021__stddev"]
     zbatter.zbb_per_pa2021 = (zbatter.bb_per_pa2021 - bb_per_pa2021mean["bb_per_pa2021__avg"]) / bb_per_pa2021stddev["bb_per_pa2021__stddev"]
     zbatter.zplus_bb_per_pa2021 = (zbatter.plus_bb_per_pa2021 - plus_bb_per_pa2021mean["plus_bb_per_pa2021__avg"]) / plus_bb_per_pa2021stddev["plus_bb_per_pa2021__stddev"]
     #must invert z-score
     zbatter.zplus_k_per_pa2021 = -(zbatter.plus_k_per_pa2021 - plus_k_per_pa2021mean["plus_k_per_pa2021__avg"]) / plus_k_per_pa2021stddev["plus_k_per_pa2021__stddev"]
     #must invert z-score
     zbatter.zk_per_pa2021 = -(zbatter.k_per_pa2021 - k_per_pa2021mean["k_per_pa2021__avg"]) / k_per_pa2021stddev["k_per_pa2021__stddev"]
     zbatter.zr_per_pa2021 = (zbatter.r_per_pa2021 - r_per_pa2021mean["r_per_pa2021__avg"]) / r_per_pa2021stddev["r_per_pa2021__stddev"]
     zbatter.zrbi_per_pa2021 = (zbatter.rbi_per_pa2021 - rbi_per_pa2021mean["rbi_per_pa2021__avg"]) / rbi_per_pa2021stddev["rbi_per_pa2021__stddev"]
     #must invert z-score
     zbatter.zgdp_per_pa2021 = -(zbatter.gdp_per_pa2021 - gdp_per_pa2021mean["gdp_per_pa2021__avg"]) / gdp_per_pa2021stddev["gdp_per_pa2021__stddev"]
     zbatter.zxSB_added2021 = (zbatter.xSB_added2021 - xSB_added2021mean["xSB_added2021__avg"]) / xSB_added2021stddev["xSB_added2021__stddev"]
     zbatter.zxSB_added_percent2021 = (zbatter.xSB_added_percent2021 - xSB_added_percent2021mean["xSB_added_percent2021__avg"]) / xSB_added_percent2021stddev["xSB_added_percent2021__stddev"]
     zbatter.zwRAA2021 = (zbatter.wRAA2021 - wRAA2021mean["wRAA2021__avg"]) / wRAA2021stddev["wRAA2021__stddev"]
     zbatter.zwOBA2021 = (zbatter.wOBA2021 - wOBA2021mean["wOBA2021__avg"]) / wOBA2021stddev["wOBA2021__stddev"]
     zbatter.zwRC2021 = (zbatter.wRC2021 - wRC2021mean["wRC2021__avg"]) / wRC2021stddev["wRC2021__stddev"]
     zbatter.zplus_wRC2021 = (zbatter.plus_wRC2021 - plus_wRC2021mean["plus_wRC2021__avg"]) / plus_wRC2021stddev["plus_wRC2021__stddev"]
     zbatter.ziso2021 = (zbatter.iso2021 - iso2021mean["iso2021__avg"]) / iso2021stddev["iso2021__stddev"]
     zbatter.zplus_iso2021 = (zbatter.plus_iso2021 - plus_iso2021mean["plus_iso2021__avg"]) / plus_iso2021stddev["plus_iso2021__stddev"]
     zbatter.zbabip2021 = (zbatter.babip2021 - babip2021mean["babip2021__avg"]) / babip2021stddev["babip2021__stddev"]
     zbatter.zplus_babip2021 = (zbatter.plus_babip2021 - plus_babip2021mean["plus_babip2021__avg"]) / plus_babip2021stddev["plus_babip2021__stddev"]
     zbatter.zld_per_bip2021 = (zbatter.ld_per_bip2021 - ld_per_bip2021mean["ld_per_bip2021__avg"]) / ld_per_bip2021stddev["ld_per_bip2021__stddev"]
     #must invert z-score
     zbatter.zgb_per_bip2021 = -(zbatter.gb_per_bip2021 - gb_per_bip2021mean["gb_per_bip2021__avg"]) / gb_per_bip2021stddev["gb_per_bip2021__stddev"]
     zbatter.zfb_per_bip2021 = (zbatter.fb_per_bip2021 - fb_per_bip2021mean["fb_per_bip2021__avg"]) / fb_per_bip2021stddev["fb_per_bip2021__stddev"]
     #must invert z-score
     zbatter.ziffb_per_bip2021 = -(zbatter.iffb_per_bip2021 - iffb_per_bip2021mean["iffb_per_bip2021__avg"]) / iffb_per_bip2021stddev["iffb_per_bip2021__stddev"]
     zbatter.zbsr2021 = (zbatter.bsr2021 - bsr2021mean["bsr2021__avg"]) / bsr2021stddev["bsr2021__stddev"]
     zbatter.zclutch2021 = (zbatter.clutch2021 - clutch2021mean["clutch2021__avg"]) / clutch2021stddev["clutch2021__stddev"]
     zbatter.zfwar2021 = (zbatter.fwar2021 - fwar2021mean["fwar2021__avg"]) / fwar2021stddev["fwar2021__stddev"]
     zbatter.zhardpercent2021 = (zbatter.hardpercent2021 - hardpercent2021mean["hardpercent2021__avg"]) / hardpercent2021stddev["hardpercent2021__stddev"]
     zbatter.zplus_hardpercent2021 = (zbatter.plus_hardpercent2021 - plus_hardpercent2021mean["plus_hardpercent2021__avg"]) / plus_hardpercent2021stddev["plus_hardpercent2021__stddev"]
     zbatter.zhardhitpercent2021 = (zbatter.hardhitpercent2021 - hardhitpercent2021mean["hardhitpercent2021__avg"]) / hardhitpercent2021stddev["hardhitpercent2021__stddev"]
     zbatter.zfwar_per_pa2021 = (zbatter.fwar_per_pa2021 - fwar_per_pa2021mean["fwar_per_pa2021__avg"]) / fwar_per_pa2021stddev["fwar_per_pa2021__stddev"]
     zbatter.zbsr_per_pa2021 = (zbatter.bsr_per_pa2021 - bsr_per_pa2021mean["bsr_per_pa2021__avg"]) / bsr_per_pa2021stddev["bsr_per_pa2021__stddev"]
     #must invert z-score
     zbatter.zoutsidezoneswingpercent2021 = -(zbatter.outsidezoneswingpercent2021 - outsidezoneswingpercent2021mean["outsidezoneswingpercent2021__avg"]) / outsidezoneswingpercent2021stddev["outsidezoneswingpercent2021__stddev"]
     #must invert z-score
     zbatter.zfirstpitchstrikepercent2021 = -(zbatter.firstpitchstrikepercent2021 - firstpitchstrikepercent2021mean["firstpitchstrikepercent2021__avg"]) / firstpitchstrikepercent2021stddev["firstpitchstrikepercent2021__stddev"]
     zbatter.zswingcontactpercent2021 = (zbatter.swingcontactpercent2021 - swingcontactpercent2021mean["swingcontactpercent2021__avg"]) / swingcontactpercent2021stddev["swingcontactpercent2021__stddev"]
     #must invert z-score
     zbatter.zswingingstrikespercent2021 = -(zbatter.swingingstrikespercent2021 - swingingstrikespercent2021mean["swingingstrikespercent2021__avg"]) / swingingstrikespercent2021stddev["swingingstrikespercent2021__stddev"]
     zbatter.zfoff2021 = (zbatter.foff2021 - foff2021mean["foff2021__avg"]) / foff2021stddev["foff2021__stddev"]
     zbatter.zfoff_per_pa2021 = (zbatter.foff_per_pa2021 - foff_per_pa2021mean["foff_per_pa2021__avg"]) / foff_per_pa2021stddev["foff_per_pa2021__stddev"]
     zbatter.zfbat2021 = (zbatter.fbat2021 - fbat2021mean["fbat2021__avg"]) / fbat2021stddev["fbat2021__stddev"]
     if zbatter.fldloaded_2021 == True:
       zbatter.zfdef2021 = (zbatter.fdef2021 - fdef2021mean["fdef2021__avg"]) / fdef2021stddev["fdef2021__stddev"]
       zbatter.zffld2021 = (zbatter.ffld2021 - ffld2021mean["ffld2021__avg"]) / ffld2021stddev["ffld2021__stddev"]
       zbatter.zfdef_per_pa2021 = (zbatter.fdef_per_pa2021 - fdef_per_pa2021mean["fdef_per_pa2021__avg"]) / fdef_per_pa2021stddev["fdef_per_pa2021__stddev"]
       zbatter.zffld_per_pa2021 = (zbatter.ffld_per_pa2021 - ffld_per_pa2021mean["ffld_per_pa2021__avg"]) / ffld_per_pa2021stddev["ffld_per_pa2021__stddev"]
     else:
       zbatter.zfdef2021 = 0
       zbatter.zffld2021 = 0
       zbatter.zfdef_per_pa2021 = 0
       zbatter.zffld_per_pa2021 = 0
     #zbatter.zbarrel_percent2021 = (zbatter.barrel_percent2021 - barrel_percent2021mean["barrel_percent2021__avg"]) / barrel_percent2021stddev["barrel_percent2021__stddev"]
     zbatter.zfbat_per_pa2021 = (zbatter.fbat_per_pa2021 - fbat_per_pa2021mean["fbat_per_pa2021__avg"]) / fbat_per_pa2021stddev["fbat_per_pa2021__stddev"]
     #zbatter.zmaxEV2021 = (zbatter.maxEV2021 - maxEV2021mean["maxEV2021__avg"]) / maxEV2021stddev["maxEV2021__stddev"]
     #TEMP zbatter.zplus_ld_per_bip2021 = (zbatter.plus_ld_per_bip2021 - plus_ld_per_bip2021mean["plus_ld_per_bip2021__avg"]) / plus_ld_per_bip2021stddev["plus_ld_per_bip2021__stddev"]
    
     #must invert z-score
     zbatter.zplus_gb_per_bip2021 = -(zbatter.plus_gb_per_bip2021 - plus_gb_per_bip2021mean["plus_gb_per_bip2021__avg"]) / plus_gb_per_bip2021stddev["plus_gb_per_bip2021__stddev"]
     zbatter.zplus_fb_per_bip2021 = (zbatter.plus_fb_per_bip2021 - plus_fb_per_bip2021mean["plus_fb_per_bip2021__avg"]) / plus_fb_per_bip2021stddev["plus_fb_per_bip2021__stddev"]
     zbatter.zspd2021 = (zbatter.spd2021 - spd2021mean["spd2021__avg"]) / spd2021stddev["spd2021__stddev"]
     if zbatter.loaded_hr_per_fb2021 == True:
       zbatter.zplus_hr_per_fb2021 = (zbatter.plus_hr_per_fb2021 - plus_hr_per_fb2021mean["plus_hr_per_fb2021__avg"]) / plus_hr_per_fb2021stddev["plus_hr_per_fb2021__stddev"]
       zbatter.zhr_per_fb2021 = (zbatter.hr_per_fb2021 - hr_per_fb2021mean["hr_per_fb2021__avg"]) / hr_per_fb2021stddev["hr_per_fb2021__stddev"]
     else:
       zbatter.zplus_hr_per_fb2021 = 0
       zbatter.zhr_per_fb2021 = 0
     # zbatter.zxBA2021 = (zbatter.xBA2021 - xBA2021mean["xBA2021__avg"]) / xBA2021stddev["xBA2021__stddev"]
     # zbatter.zfgxSLG2021 = (zbatter.fgxSLG2021 - fgxSLG2021mean["fgxSLG2021__avg"]) / fgxSLG2021stddev["fgxSLG2021__stddev"]
     # zbatter.zfgxWOBA2021 = (zbatter.fgxWOBA2021 - fgxWOBA2021mean["fgxWOBA2021__avg"]) / fgxWOBA2021stddev["fgxWOBA2021__stddev"]
     if zbatter.loaded_bref_2021 == True:
       zbatter.zbref_bsr_runs2021 = (zbatter.bref_bsr_runs2021 - bref_bsr_runs2021mean["bref_bsr_runs2021__avg"]) / bref_bsr_runs2021stddev["bref_bsr_runs2021__stddev"]
       zbatter.zbref_batting_runs2021 = (zbatter.bref_batting_runs2021 - bref_batting_runs2021mean["bref_batting_runs2021__avg"]) / bref_batting_runs2021stddev["bref_batting_runs2021__stddev"]
       zbatter.zbref_runs_above_avg2021 = (zbatter.bref_runs_above_avg2021 - bref_runs_above_avg2021mean["bref_runs_above_avg2021__avg"]) / bref_runs_above_avg2021stddev["bref_runs_above_avg2021__stddev"]
       zbatter.zbref_gdp_runs2021 = (zbatter.bref_gdp_runs2021 - bref_gdp_runs2021mean["bref_gdp_runs2021__avg"]) / bref_gdp_runs2021stddev["bref_gdp_runs2021__stddev"]
       zbatter.zbref_runs_above_avg_def2021 = (zbatter.bref_runs_above_avg_def2021 - bref_runs_above_avg_def2021mean["bref_runs_above_avg_def2021__avg"]) / bref_runs_above_avg_def2021stddev["bref_runs_above_avg_def2021__stddev"]
       zbatter.zbref_war2021 = (zbatter.bref_war2021 - bref_war2021mean["bref_war2021__avg"]) / bref_war2021stddev["bref_war2021__stddev"]
       zbatter.zbref_runs_above_avg_off2021 = (zbatter.bref_runs_above_avg_off2021 - bref_runs_above_avg_off2021mean["bref_runs_above_avg_off2021__avg"]) / bref_runs_above_avg_off2021stddev["bref_runs_above_avg_off2021__stddev"]
       zbatter.zbref_war_def2021 = (zbatter.bref_war_def2021 - bref_war_def2021mean["bref_war_def2021__avg"]) / bref_war_def2021stddev["bref_war_def2021__stddev"]
       zbatter.zbref_war_off2021 = (zbatter.bref_war_off2021 - bref_war_off2021mean["bref_war_off2021__avg"]) / bref_war_off2021stddev["bref_war_off2021__stddev"]
       zbatter.zplus_ops2021 = (zbatter.plus_ops2021 - plus_ops2021mean["plus_ops2021__avg"]) / plus_ops2021stddev["plus_ops2021__stddev"]
       zbatter.zbref_batting_runs_per_pa2021 = (zbatter.bref_batting_runs_per_pa2021 - bref_batting_runs_per_pa2021mean["bref_batting_runs_per_pa2021__avg"]) / bref_batting_runs_per_pa2021stddev["bref_batting_runs_per_pa2021__stddev"]
       zbatter.zbref_bsr_runs_per_pa2021 = (zbatter.bref_bsr_runs_per_pa2021 - bref_bsr_runs_per_pa2021mean["bref_bsr_runs_per_pa2021__avg"]) / bref_bsr_runs_per_pa2021stddev["bref_bsr_runs_per_pa2021__stddev"]
       zbatter.zbref_gdp_runs_per_pa2021 = (zbatter.bref_gdp_runs_per_pa2021 - bref_gdp_runs_per_pa2021mean["bref_gdp_runs_per_pa2021__avg"]) / bref_gdp_runs_per_pa2021stddev["bref_gdp_runs_per_pa2021__stddev"]
       zbatter.zbref_runs_above_avg_per_pa2021 = (zbatter.bref_runs_above_avg_per_pa2021 - bref_runs_above_avg_per_pa2021mean["bref_runs_above_avg_per_pa2021__avg"]) / bref_runs_above_avg_per_pa2021stddev["bref_runs_above_avg_per_pa2021__stddev"]
       zbatter.zbref_runs_above_avg_def_per_pa2021 = (zbatter.bref_runs_above_avg_def_per_pa2021 - bref_runs_above_avg_def_per_pa2021mean["bref_runs_above_avg_def_per_pa2021__avg"]) / bref_runs_above_avg_def_per_pa2021stddev["bref_runs_above_avg_def_per_pa2021__stddev"]
       zbatter.zbref_war_per_pa2021 = (zbatter.bref_war_per_pa2021 - bref_war_per_pa2021mean["bref_war_per_pa2021__avg"]) / bref_war_per_pa2021stddev["bref_war_per_pa2021__stddev"]
       zbatter.zbref_runs_above_avg_off_per_pa2021 = (zbatter.bref_runs_above_avg_off_per_pa2021 - bref_runs_above_avg_off_per_pa2021mean["bref_runs_above_avg_off_per_pa2021__avg"]) / bref_runs_above_avg_off_per_pa2021stddev["bref_runs_above_avg_off_per_pa2021__stddev"]
       zbatter.zbref_war_off_per_pa2021 = (zbatter.bref_war_off_per_pa2021 - bref_war_off_per_pa2021mean["bref_war_off_per_pa2021__avg"]) / bref_war_off_per_pa2021stddev["bref_war_off_per_pa2021__stddev"]
       zbatter.zbref_war_def_per_pa2021 = (zbatter.bref_war_def_per_pa2021 - bref_war_def_per_pa2021mean["bref_war_def_per_pa2021__avg"]) / bref_war_def_per_pa2021stddev["bref_war_def_per_pa2021__stddev"]
     if zbatter.loaded_bs_x_2021 == True:
       zbatter.zxavg2021 = (zbatter.xavg2021 - xavg2021mean["xavg2021__avg"]) / xavg2021stddev["xavg2021__stddev"]
       zbatter.zbip2021 = (zbatter.bip2021 - bip2021mean["bip2021__avg"]) / bip2021stddev["bip2021__stddev"]
       zbatter.zxslg2021 = (zbatter.xslg2021 - xslg2021mean["xslg2021__avg"]) / xslg2021stddev["xslg2021__stddev"]
       zbatter.zxavgdiff2021 = (zbatter.xavgdiff2021 - xavgdiff2021mean["xavgdiff2021__avg"]) / xavgdiff2021stddev["xavgdiff2021__stddev"]
       zbatter.zxslgdiff2021 = (zbatter.xslgdiff2021 - xslgdiff2021mean["xslgdiff2021__avg"]) / xslgdiff2021stddev["xslgdiff2021__stddev"]
       zbatter.zxwoba2021 = (zbatter.xwoba2021 - xwoba2021mean["xwoba2021__avg"]) / xwoba2021stddev["xwoba2021__stddev"]
       zbatter.zxwobadiff2021 = (zbatter.xwobadiff2021 - xwobadiff2021mean["xwobadiff2021__avg"]) / xwobadiff2021stddev["xwobadiff2021__stddev"]
     if zbatter.loaded_bs_barrel_2021 == True:
       zbatter.zanglesweetspotpercent2021 = (zbatter.anglesweetspotpercent2021 - anglesweetspotpercent2021mean["anglesweetspotpercent2021__avg"]) / anglesweetspotpercent2021stddev["anglesweetspotpercent2021__stddev"]
       zbatter.zmax_hit_speed2021 = (zbatter.max_hit_speed2021 - max_hit_speed2021mean["max_hit_speed2021__avg"]) / max_hit_speed2021stddev["max_hit_speed2021__stddev"]
       zbatter.zavg_hit_speed2021 = (zbatter.avg_hit_speed2021 - avg_hit_speed2021mean["avg_hit_speed2021__avg"]) / avg_hit_speed2021stddev["avg_hit_speed2021__stddev"]
       zbatter.zmax_distance2021 = (zbatter.max_distance2021 - max_distance2021mean["max_distance2021__avg"]) / max_distance2021stddev["max_distance2021__stddev"]
       zbatter.zavg_distance2021 = (zbatter.avg_distance2021 - avg_distance2021mean["avg_distance2021__avg"]) / avg_distance2021stddev["avg_distance2021__stddev"]
       zbatter.zev95percent2021 = (zbatter.ev95percent2021 - ev95percent2021mean["ev95percent2021__avg"]) / ev95percent2021stddev["ev95percent2021__stddev"]
       zbatter.zbrl_percent2021 = (zbatter.brl_percent2021 - brl_percent2021mean["brl_percent2021__avg"]) / brl_percent2021stddev["brl_percent2021__stddev"]
       zbatter.zbrl_pa2021 = (zbatter.brl_pa2021 - brl_pa2021mean["brl_pa2021__avg"]) / brl_pa2021stddev["brl_pa2021__stddev"]
    #  if zbatter.loaded_bs_fielding_2021 == True:
    #    zbatter.zouts_above_avg2021 = (zbatter.outs_above_avg2021 - outs_above_avg2021mean["outs_above_avg2021__avg"]) / outs_above_avg2021stddev["outs_above_avg2021__stddev"]
    #    zbatter.zfielding_runs_prevented2021 = (zbatter.fielding_runs_prevented2021 - fielding_runs_prevented2021mean["fielding_runs_prevented2021__avg"]) / fielding_runs_prevented2021stddev["fielding_runs_prevented2021__stddev"]
     zbatter.save()

