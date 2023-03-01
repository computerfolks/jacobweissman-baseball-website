import decimal
from django.core.management.base import BaseCommand
from app_bb.models import batter
from django.db.models.aggregates import StdDev, Avg

class Command(BaseCommand):
 def handle(self, *args, **options):
   if batter.objects.filter(lastname = "dummy").exists():
     batter.objects.filter(lastname = "dummy").delete()
   pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("pa2020"))
   pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("pa2020"))
   plus_avg2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_avg2020"))
   plus_avg2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_avg2020"))
   avg2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("avg2020"))
   avg2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("avg2020"))
   obp2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("obp2020"))
   obp2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("obp2020"))
   plus_obp2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_obp2020"))
   plus_obp2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_obp2020"))
   slg2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("slg2020"))
   slg2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("slg2020"))
   plus_slg2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_slg2020"))
   plus_slg2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_slg2020"))
   ops2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("ops2020"))
   ops2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("ops2020"))
   bb_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bb_per_pa2020"))
   bb_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("bb_per_pa2020"))
   plus_bb_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_bb_per_pa2020"))
   plus_bb_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_bb_per_pa2020"))
   plus_k_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_k_per_pa2020"))
   plus_k_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_k_per_pa2020"))
   k_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("k_per_pa2020"))
   k_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("k_per_pa2020"))
   r_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("r_per_pa2020"))
   r_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("r_per_pa2020"))
   rbi_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("rbi_per_pa2020"))
   rbi_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("rbi_per_pa2020"))
   gdp_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("gdp_per_pa2020"))
   gdp_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("gdp_per_pa2020"))
   xSB_added2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xSB_added2020"))
   xSB_added2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("xSB_added2020"))
   xSB_added_percent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xSB_added_percent2020"))
   xSB_added_percent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("xSB_added_percent2020"))
   wRAA2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("wRAA2020"))
   wRAA2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("wRAA2020"))
   wOBA2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("wOBA2020"))
   wOBA2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("wOBA2020"))
   wRC2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("wRC2020"))
   wRC2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("wRC2020"))
   plus_wRC2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_wRC2020"))
   plus_wRC2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_wRC2020"))
   iso2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("iso2020"))
   iso2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("iso2020"))
   plus_iso2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_iso2020"))
   plus_iso2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_iso2020"))
   babip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("babip2020"))
   babip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("babip2020"))
   plus_babip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_babip2020"))
   plus_babip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_babip2020"))
   ld_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("ld_per_bip2020"))
   ld_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("ld_per_bip2020"))
   gb_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("gb_per_bip2020"))
   gb_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("gb_per_bip2020"))
   fb_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fb_per_bip2020"))
   fb_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fb_per_bip2020"))
   iffb_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("iffb_per_bip2020"))
   iffb_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("iffb_per_bip2020"))
   hr_per_fb2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(loaded_hr_per_fb2020 = True).aggregate(StdDev("hr_per_fb2020"))
   hr_per_fb2020mean = batter.objects.all().filter(loaded_2020 = True).filter(loaded_hr_per_fb2020 = True).aggregate(Avg("hr_per_fb2020"))
   bsr2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bsr2020"))
   # print("baserunning total", bsr2020stddev) 1.47900609072223
   bsr2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("bsr2020"))
   # print("baserunning mean", bsr2020mean) 0
   clutch2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("clutch2020"))
   clutch2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("clutch2020"))
   fwar2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fwar2020"))
   fwar2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fwar2020"))
   hardpercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hardpercent2020"))
   hardpercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("hardpercent2020"))
   plus_hardpercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_hardpercent2020"))
   plus_hardpercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_hardpercent2020"))
   hardhitpercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hardhitpercent2020"))
   hardhitpercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("hardhitpercent2020"))
   fwar_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fwar_per_pa2020"))
   fwar_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fwar_per_pa2020"))
   bsr_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bsr_per_pa2020"))
   # print("baserunning per pa", bsr_per_pa2020stddev) 0.00833214477662146
   bsr_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("bsr_per_pa2020"))
   outsidezoneswingpercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("outsidezoneswingpercent2020"))
   outsidezoneswingpercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("outsidezoneswingpercent2020"))
   firstpitchstrikepercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("firstpitchstrikepercent2020"))
   firstpitchstrikepercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("firstpitchstrikepercent2020"))
   swingcontactpercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("swingcontactpercent2020"))
   swingcontactpercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("swingcontactpercent2020"))
   swingingstrikespercent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("swingingstrikespercent2020"))
   swingingstrikespercent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("swingingstrikespercent2020"))
   foff2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("foff2020"))
   foff2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("foff2020"))
   fdef2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(StdDev("fdef2020"))
   # print("defense total", fdef2020stddev) 3.92625378652656
   fdef2020mean = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(Avg("fdef2020"))
   # print("defense mean", fdef2020mean) -0.485714285714286
   ffld2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(StdDev("ffld2020"))
   # print("fielding total", ffld2020stddev) 2.93118745254359
   ffld2020mean = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(Avg("ffld2020"))
   # print("fielding mean", ffld2020mean) 0.0409937888198759
   foff_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("foff_per_pa2020"))
   foff_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("foff_per_pa2020"))
   fdef_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(StdDev("fdef_per_pa2020"))
   # print("defense per pa", fdef_per_pa2020stddev) 0.0245836618867729
   fdef_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(Avg("fdef_per_pa2020"))
   fbat2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fbat2020"))
   # print("batting total", fbat2020stddev) 7.63961508130041
   fbat2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fbat2020"))
   # print("batting mean", fbat2020mean) 0.225819672131148
   ffld_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(StdDev("ffld_per_pa2020"))
   # print("fielding per pa", ffld_per_pa2020stddev) 0.0208832062380861
   ffld_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).filter(fldloaded_2020 = True).aggregate(Avg("ffld_per_pa2020"))
   # barrel_percent2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("barrel_percent2020"))
   # barrel_percent2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("barrel_percent2020"))
   fbat_per_pa2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fbat_per_pa2020"))
   # print("batting per pa", fbat_per_pa2020stddev) 0.0438921952567499
   fbat_per_pa2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fbat_per_pa2020"))
   # maxEV2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("maxEV2020"))
   # maxEV2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("maxEV2020"))
   plus_ld_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_ld_per_bip2020"))
   plus_ld_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_ld_per_bip2020"))
   plus_gb_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_gb_per_bip2020"))
   plus_gb_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_gb_per_bip2020"))
   plus_fb_per_bip2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_fb_per_bip2020"))
   plus_fb_per_bip2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_fb_per_bip2020"))
   spd2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("spd2020"))
   spd2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("spd2020"))
   plus_hr_per_fb2020stddev = batter.objects.all().filter(loaded_2020 = True).filter(loaded_hr_per_fb2020 = True).aggregate(StdDev("plus_hr_per_fb2020"))
   plus_hr_per_fb2020mean = batter.objects.all().filter(loaded_2020 = True).filter(loaded_hr_per_fb2020 = True).aggregate(Avg("plus_hr_per_fb2020"))
   # xBA2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xBA2020"))
   # xBA2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("xBA2020"))
   # fgxSLG2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fgxSLG2020"))
   # fgxSLG2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fgxSLG2020"))
   # fgxWOBA2020stddev = batter.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fgxWOBA2020"))
   # fgxWOBA2020mean = batter.objects.all().filter(loaded_2020 = True).aggregate(Avg("fgxWOBA2020"))
   bref_bsr_runs2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_bsr_runs2020"))
   bref_bsr_runs2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_bsr_runs2020"))
   bref_batting_runs2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_batting_runs2020"))
   bref_batting_runs2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_batting_runs2020"))
   bref_runs_above_avg2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg2020"))
   bref_runs_above_avg2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg2020"))
   bref_gdp_runs2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_gdp_runs2020"))
   bref_gdp_runs2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_gdp_runs2020"))
   bref_runs_above_avg_def2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg_def2020"))
   bref_runs_above_avg_def2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg_def2020"))
   bref_war2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war2020"))
   bref_war2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war2020"))
   bref_runs_above_avg_off2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg_off2020"))
   bref_runs_above_avg_off2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg_off2020"))
   bref_war_def2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war_def2020"))
   bref_war_def2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war_def2020"))
   bref_war_off2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war_off2020"))
   bref_war_off2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war_off2020"))
   plus_ops2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("plus_ops2020"))
   plus_ops2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("plus_ops2020"))
   bref_batting_runs_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_batting_runs_per_pa2020"))
   bref_batting_runs_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_batting_runs_per_pa2020"))
   bref_bsr_runs_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_bsr_runs_per_pa2020"))
   bref_bsr_runs_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_bsr_runs_per_pa2020"))
   bref_gdp_runs_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_gdp_runs_per_pa2020"))
   bref_gdp_runs_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_gdp_runs_per_pa2020"))
   bref_runs_above_avg_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg_per_pa2020"))
   bref_runs_above_avg_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg_per_pa2020"))
   bref_runs_above_avg_def_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg_def_per_pa2020"))
   bref_runs_above_avg_def_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg_def_per_pa2020"))
   bref_war_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war_per_pa2020"))
   bref_war_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war_per_pa2020"))
   bref_runs_above_avg_off_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_runs_above_avg_off_per_pa2020"))
   bref_runs_above_avg_off_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_runs_above_avg_off_per_pa2020"))
   bref_war_off_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war_off_per_pa2020"))
   bref_war_off_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war_off_per_pa2020"))
   bref_war_def_per_pa2020stddev = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(StdDev("bref_war_def_per_pa2020"))
   bref_war_def_per_pa2020mean = batter.objects.all().filter(loaded_bref_2020 = True).aggregate(Avg("bref_war_def_per_pa2020"))
   #baseball savant x
   xavg2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xavg2020"))
   xavg2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xavg2020"))
   bip2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("bip2020"))
   bip2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("bip2020"))
   xslg2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xslg2020"))
   xslg2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xslg2020"))
   xavgdiff2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xavgdiff2020"))
   xavgdiff2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xavgdiff2020"))
   xslgdiff2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xslgdiff2020"))
   xslgdiff2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xslgdiff2020"))
   xwobadiff2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xwobadiff2020"))
   xwobadiff2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xwobadiff2020"))
   xwoba2020stddev = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xwoba2020"))
   xwoba2020mean = batter.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xwoba2020"))
   #baseball savant barrel
   anglesweetspotpercent2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("anglesweetspotpercent2020"))
   anglesweetspotpercent2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("anglesweetspotpercent2020"))
   max_hit_speed2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("max_hit_speed2020"))
   max_hit_speed2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("max_hit_speed2020"))
   avg_hit_speed2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("avg_hit_speed2020"))
   avg_hit_speed2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("avg_hit_speed2020"))
   max_distance2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("max_distance2020"))
   max_distance2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("max_distance2020"))
   avg_distance2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("avg_distance2020"))
   avg_distance2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("avg_distance2020"))
   ev95percent2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("ev95percent2020"))
   ev95percent2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("ev95percent2020"))
   brl_percent2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("brl_percent2020"))
   brl_percent2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("brl_percent2020"))
   brl_pa2020stddev = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("brl_pa2020"))
   brl_pa2020mean = batter.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("brl_pa2020"))
  #  outs_above_avg2020stddev = batter.objects.all().filter(loaded_bs_fielding_2020 = True).aggregate(StdDev("outs_above_avg2020"))
  #  outs_above_avg2020mean = batter.objects.all().filter(loaded_bs_fielding_2020 = True).aggregate(Avg("outs_above_avg2020"))
  #  fielding_runs_prevented2020stddev = batter.objects.all().filter(loaded_bs_fielding_2020 = True).aggregate(StdDev("fielding_runs_prevented2020"))
  #  fielding_runs_prevented2020mean = batter.objects.all().filter(loaded_bs_fielding_2020 = True).aggregate(Avg("fielding_runs_prevented2020"))
 
   for zbatter in batter.objects.all().filter(loaded_2020 = True):
     zbatter.zpa2020 = (zbatter.pa2020 - pa2020mean["pa2020__avg"]) / pa2020stddev["pa2020__stddev"]
     zbatter.zplus_avg2020 = (zbatter.plus_avg2020 - plus_avg2020mean["plus_avg2020__avg"]) / plus_avg2020stddev["plus_avg2020__stddev"]
     zbatter.zavg2020 = (zbatter.avg2020 - avg2020mean["avg2020__avg"]) / avg2020stddev["avg2020__stddev"]
     zbatter.zobp2020 = (zbatter.obp2020 - obp2020mean["obp2020__avg"]) / obp2020stddev["obp2020__stddev"]
     zbatter.zplus_obp2020 = (zbatter.plus_obp2020 - plus_obp2020mean["plus_obp2020__avg"]) / plus_obp2020stddev["plus_obp2020__stddev"]
     zbatter.zslg2020 = (zbatter.slg2020 - slg2020mean["slg2020__avg"]) / slg2020stddev["slg2020__stddev"]
     zbatter.zplus_slg2020 = (zbatter.plus_slg2020 - plus_slg2020mean["plus_slg2020__avg"]) / plus_slg2020stddev["plus_slg2020__stddev"]
     zbatter.zops2020 = (zbatter.ops2020 - ops2020mean["ops2020__avg"]) / ops2020stddev["ops2020__stddev"]
     zbatter.zbb_per_pa2020 = (zbatter.bb_per_pa2020 - bb_per_pa2020mean["bb_per_pa2020__avg"]) / bb_per_pa2020stddev["bb_per_pa2020__stddev"]
     zbatter.zplus_bb_per_pa2020 = (zbatter.plus_bb_per_pa2020 - plus_bb_per_pa2020mean["plus_bb_per_pa2020__avg"]) / plus_bb_per_pa2020stddev["plus_bb_per_pa2020__stddev"]
     #must invert z-score
     zbatter.zplus_k_per_pa2020 = -(zbatter.plus_k_per_pa2020 - plus_k_per_pa2020mean["plus_k_per_pa2020__avg"]) / plus_k_per_pa2020stddev["plus_k_per_pa2020__stddev"]
     #must invert z-score
     zbatter.zk_per_pa2020 = -(zbatter.k_per_pa2020 - k_per_pa2020mean["k_per_pa2020__avg"]) / k_per_pa2020stddev["k_per_pa2020__stddev"]
     zbatter.zr_per_pa2020 = (zbatter.r_per_pa2020 - r_per_pa2020mean["r_per_pa2020__avg"]) / r_per_pa2020stddev["r_per_pa2020__stddev"]
     zbatter.zrbi_per_pa2020 = (zbatter.rbi_per_pa2020 - rbi_per_pa2020mean["rbi_per_pa2020__avg"]) / rbi_per_pa2020stddev["rbi_per_pa2020__stddev"]
     #must invert z-score
     zbatter.zgdp_per_pa2020 = -(zbatter.gdp_per_pa2020 - gdp_per_pa2020mean["gdp_per_pa2020__avg"]) / gdp_per_pa2020stddev["gdp_per_pa2020__stddev"]
     zbatter.zxSB_added2020 = (zbatter.xSB_added2020 - xSB_added2020mean["xSB_added2020__avg"]) / xSB_added2020stddev["xSB_added2020__stddev"]
     zbatter.zxSB_added_percent2020 = (zbatter.xSB_added_percent2020 - xSB_added_percent2020mean["xSB_added_percent2020__avg"]) / xSB_added_percent2020stddev["xSB_added_percent2020__stddev"]
     zbatter.zwRAA2020 = (zbatter.wRAA2020 - wRAA2020mean["wRAA2020__avg"]) / wRAA2020stddev["wRAA2020__stddev"]
     zbatter.zwOBA2020 = (zbatter.wOBA2020 - wOBA2020mean["wOBA2020__avg"]) / wOBA2020stddev["wOBA2020__stddev"]
     zbatter.zwRC2020 = (zbatter.wRC2020 - wRC2020mean["wRC2020__avg"]) / wRC2020stddev["wRC2020__stddev"]
     zbatter.zplus_wRC2020 = (zbatter.plus_wRC2020 - plus_wRC2020mean["plus_wRC2020__avg"]) / plus_wRC2020stddev["plus_wRC2020__stddev"]
     zbatter.ziso2020 = (zbatter.iso2020 - iso2020mean["iso2020__avg"]) / iso2020stddev["iso2020__stddev"]
     zbatter.zplus_iso2020 = (zbatter.plus_iso2020 - plus_iso2020mean["plus_iso2020__avg"]) / plus_iso2020stddev["plus_iso2020__stddev"]
     zbatter.zbabip2020 = (zbatter.babip2020 - babip2020mean["babip2020__avg"]) / babip2020stddev["babip2020__stddev"]
     zbatter.zplus_babip2020 = (zbatter.plus_babip2020 - plus_babip2020mean["plus_babip2020__avg"]) / plus_babip2020stddev["plus_babip2020__stddev"]
     zbatter.zld_per_bip2020 = (zbatter.ld_per_bip2020 - ld_per_bip2020mean["ld_per_bip2020__avg"]) / ld_per_bip2020stddev["ld_per_bip2020__stddev"]
     #must invert z-score
     zbatter.zgb_per_bip2020 = -(zbatter.gb_per_bip2020 - gb_per_bip2020mean["gb_per_bip2020__avg"]) / gb_per_bip2020stddev["gb_per_bip2020__stddev"]
     zbatter.zfb_per_bip2020 = (zbatter.fb_per_bip2020 - fb_per_bip2020mean["fb_per_bip2020__avg"]) / fb_per_bip2020stddev["fb_per_bip2020__stddev"]
     #must invert z-score
     zbatter.ziffb_per_bip2020 = -(zbatter.iffb_per_bip2020 - iffb_per_bip2020mean["iffb_per_bip2020__avg"]) / iffb_per_bip2020stddev["iffb_per_bip2020__stddev"]
     zbatter.zbsr2020 = (zbatter.bsr2020 - bsr2020mean["bsr2020__avg"]) / bsr2020stddev["bsr2020__stddev"]
     zbatter.zclutch2020 = (zbatter.clutch2020 - clutch2020mean["clutch2020__avg"]) / clutch2020stddev["clutch2020__stddev"]
     zbatter.zfwar2020 = (zbatter.fwar2020 - fwar2020mean["fwar2020__avg"]) / fwar2020stddev["fwar2020__stddev"]
     zbatter.zhardpercent2020 = (zbatter.hardpercent2020 - hardpercent2020mean["hardpercent2020__avg"]) / hardpercent2020stddev["hardpercent2020__stddev"]
     zbatter.zplus_hardpercent2020 = (zbatter.plus_hardpercent2020 - plus_hardpercent2020mean["plus_hardpercent2020__avg"]) / plus_hardpercent2020stddev["plus_hardpercent2020__stddev"]
     zbatter.zhardhitpercent2020 = (zbatter.hardhitpercent2020 - hardhitpercent2020mean["hardhitpercent2020__avg"]) / hardhitpercent2020stddev["hardhitpercent2020__stddev"]
     zbatter.zfwar_per_pa2020 = (zbatter.fwar_per_pa2020 - fwar_per_pa2020mean["fwar_per_pa2020__avg"]) / fwar_per_pa2020stddev["fwar_per_pa2020__stddev"]
     zbatter.zbsr_per_pa2020 = (zbatter.bsr_per_pa2020 - bsr_per_pa2020mean["bsr_per_pa2020__avg"]) / bsr_per_pa2020stddev["bsr_per_pa2020__stddev"]
     #must invert z-score
     zbatter.zoutsidezoneswingpercent2020 = -(zbatter.outsidezoneswingpercent2020 - outsidezoneswingpercent2020mean["outsidezoneswingpercent2020__avg"]) / outsidezoneswingpercent2020stddev["outsidezoneswingpercent2020__stddev"]
     #must invert z-score
     zbatter.zfirstpitchstrikepercent2020 = -(zbatter.firstpitchstrikepercent2020 - firstpitchstrikepercent2020mean["firstpitchstrikepercent2020__avg"]) / firstpitchstrikepercent2020stddev["firstpitchstrikepercent2020__stddev"]
     zbatter.zswingcontactpercent2020 = (zbatter.swingcontactpercent2020 - swingcontactpercent2020mean["swingcontactpercent2020__avg"]) / swingcontactpercent2020stddev["swingcontactpercent2020__stddev"]
     #must invert z-score
     zbatter.zswingingstrikespercent2020 = -(zbatter.swingingstrikespercent2020 - swingingstrikespercent2020mean["swingingstrikespercent2020__avg"]) / swingingstrikespercent2020stddev["swingingstrikespercent2020__stddev"]
     zbatter.zfoff2020 = (zbatter.foff2020 - foff2020mean["foff2020__avg"]) / foff2020stddev["foff2020__stddev"]
     zbatter.zfoff_per_pa2020 = (zbatter.foff_per_pa2020 - foff_per_pa2020mean["foff_per_pa2020__avg"]) / foff_per_pa2020stddev["foff_per_pa2020__stddev"]
     zbatter.zfbat2020 = (zbatter.fbat2020 - fbat2020mean["fbat2020__avg"]) / fbat2020stddev["fbat2020__stddev"]
     if zbatter.fldloaded_2020 == True:
       zbatter.zfdef2020 = (zbatter.fdef2020 - fdef2020mean["fdef2020__avg"]) / fdef2020stddev["fdef2020__stddev"]
       zbatter.zffld2020 = (zbatter.ffld2020 - ffld2020mean["ffld2020__avg"]) / ffld2020stddev["ffld2020__stddev"]
       zbatter.zfdef_per_pa2020 = (zbatter.fdef_per_pa2020 - fdef_per_pa2020mean["fdef_per_pa2020__avg"]) / fdef_per_pa2020stddev["fdef_per_pa2020__stddev"]
       zbatter.zffld_per_pa2020 = (zbatter.ffld_per_pa2020 - ffld_per_pa2020mean["ffld_per_pa2020__avg"]) / ffld_per_pa2020stddev["ffld_per_pa2020__stddev"]
     else:
       zbatter.zfdef2020 = 0
       zbatter.zffld2020 = 0
       zbatter.zfdef_per_pa2020 = 0
       zbatter.zffld_per_pa2020 = 0
     #zbatter.zbarrel_percent2020 = (zbatter.barrel_percent2020 - barrel_percent2020mean["barrel_percent2020__avg"]) / barrel_percent2020stddev["barrel_percent2020__stddev"]
     zbatter.zfbat_per_pa2020 = (zbatter.fbat_per_pa2020 - fbat_per_pa2020mean["fbat_per_pa2020__avg"]) / fbat_per_pa2020stddev["fbat_per_pa2020__stddev"]
     #zbatter.zmaxEV2020 = (zbatter.maxEV2020 - maxEV2020mean["maxEV2020__avg"]) / maxEV2020stddev["maxEV2020__stddev"]
     #TEMP zbatter.zplus_ld_per_bip2020 = (zbatter.plus_ld_per_bip2020 - plus_ld_per_bip2020mean["plus_ld_per_bip2020__avg"]) / plus_ld_per_bip2020stddev["plus_ld_per_bip2020__stddev"]
    
     #must invert z-score
     zbatter.zplus_gb_per_bip2020 = -(zbatter.plus_gb_per_bip2020 - plus_gb_per_bip2020mean["plus_gb_per_bip2020__avg"]) / plus_gb_per_bip2020stddev["plus_gb_per_bip2020__stddev"]
     zbatter.zplus_fb_per_bip2020 = (zbatter.plus_fb_per_bip2020 - plus_fb_per_bip2020mean["plus_fb_per_bip2020__avg"]) / plus_fb_per_bip2020stddev["plus_fb_per_bip2020__stddev"]
     zbatter.zspd2020 = (zbatter.spd2020 - spd2020mean["spd2020__avg"]) / spd2020stddev["spd2020__stddev"]
     if zbatter.loaded_hr_per_fb2020 == True:
       zbatter.zplus_hr_per_fb2020 = (zbatter.plus_hr_per_fb2020 - plus_hr_per_fb2020mean["plus_hr_per_fb2020__avg"]) / plus_hr_per_fb2020stddev["plus_hr_per_fb2020__stddev"]
       zbatter.zhr_per_fb2020 = (zbatter.hr_per_fb2020 - hr_per_fb2020mean["hr_per_fb2020__avg"]) / hr_per_fb2020stddev["hr_per_fb2020__stddev"]
     else:
       zbatter.zplus_hr_per_fb2020 = 0
       zbatter.zhr_per_fb2020 = 0
     # zbatter.zxBA2020 = (zbatter.xBA2020 - xBA2020mean["xBA2020__avg"]) / xBA2020stddev["xBA2020__stddev"]
     # zbatter.zfgxSLG2020 = (zbatter.fgxSLG2020 - fgxSLG2020mean["fgxSLG2020__avg"]) / fgxSLG2020stddev["fgxSLG2020__stddev"]
     # zbatter.zfgxWOBA2020 = (zbatter.fgxWOBA2020 - fgxWOBA2020mean["fgxWOBA2020__avg"]) / fgxWOBA2020stddev["fgxWOBA2020__stddev"]
     if zbatter.loaded_bref_2020 == True:
       zbatter.zbref_bsr_runs2020 = (zbatter.bref_bsr_runs2020 - bref_bsr_runs2020mean["bref_bsr_runs2020__avg"]) / bref_bsr_runs2020stddev["bref_bsr_runs2020__stddev"]
       zbatter.zbref_batting_runs2020 = (zbatter.bref_batting_runs2020 - bref_batting_runs2020mean["bref_batting_runs2020__avg"]) / bref_batting_runs2020stddev["bref_batting_runs2020__stddev"]
       zbatter.zbref_runs_above_avg2020 = (zbatter.bref_runs_above_avg2020 - bref_runs_above_avg2020mean["bref_runs_above_avg2020__avg"]) / bref_runs_above_avg2020stddev["bref_runs_above_avg2020__stddev"]
       zbatter.zbref_gdp_runs2020 = (zbatter.bref_gdp_runs2020 - bref_gdp_runs2020mean["bref_gdp_runs2020__avg"]) / bref_gdp_runs2020stddev["bref_gdp_runs2020__stddev"]
       zbatter.zbref_runs_above_avg_def2020 = (zbatter.bref_runs_above_avg_def2020 - bref_runs_above_avg_def2020mean["bref_runs_above_avg_def2020__avg"]) / bref_runs_above_avg_def2020stddev["bref_runs_above_avg_def2020__stddev"]
       zbatter.zbref_war2020 = (zbatter.bref_war2020 - bref_war2020mean["bref_war2020__avg"]) / bref_war2020stddev["bref_war2020__stddev"]
       zbatter.zbref_runs_above_avg_off2020 = (zbatter.bref_runs_above_avg_off2020 - bref_runs_above_avg_off2020mean["bref_runs_above_avg_off2020__avg"]) / bref_runs_above_avg_off2020stddev["bref_runs_above_avg_off2020__stddev"]
       zbatter.zbref_war_def2020 = (zbatter.bref_war_def2020 - bref_war_def2020mean["bref_war_def2020__avg"]) / bref_war_def2020stddev["bref_war_def2020__stddev"]
       zbatter.zbref_war_off2020 = (zbatter.bref_war_off2020 - bref_war_off2020mean["bref_war_off2020__avg"]) / bref_war_off2020stddev["bref_war_off2020__stddev"]
       zbatter.zplus_ops2020 = (zbatter.plus_ops2020 - plus_ops2020mean["plus_ops2020__avg"]) / plus_ops2020stddev["plus_ops2020__stddev"]
       zbatter.zbref_batting_runs_per_pa2020 = (zbatter.bref_batting_runs_per_pa2020 - bref_batting_runs_per_pa2020mean["bref_batting_runs_per_pa2020__avg"]) / bref_batting_runs_per_pa2020stddev["bref_batting_runs_per_pa2020__stddev"]
       zbatter.zbref_bsr_runs_per_pa2020 = (zbatter.bref_bsr_runs_per_pa2020 - bref_bsr_runs_per_pa2020mean["bref_bsr_runs_per_pa2020__avg"]) / bref_bsr_runs_per_pa2020stddev["bref_bsr_runs_per_pa2020__stddev"]
       zbatter.zbref_gdp_runs_per_pa2020 = (zbatter.bref_gdp_runs_per_pa2020 - bref_gdp_runs_per_pa2020mean["bref_gdp_runs_per_pa2020__avg"]) / bref_gdp_runs_per_pa2020stddev["bref_gdp_runs_per_pa2020__stddev"]
       zbatter.zbref_runs_above_avg_per_pa2020 = (zbatter.bref_runs_above_avg_per_pa2020 - bref_runs_above_avg_per_pa2020mean["bref_runs_above_avg_per_pa2020__avg"]) / bref_runs_above_avg_per_pa2020stddev["bref_runs_above_avg_per_pa2020__stddev"]
       zbatter.zbref_runs_above_avg_def_per_pa2020 = (zbatter.bref_runs_above_avg_def_per_pa2020 - bref_runs_above_avg_def_per_pa2020mean["bref_runs_above_avg_def_per_pa2020__avg"]) / bref_runs_above_avg_def_per_pa2020stddev["bref_runs_above_avg_def_per_pa2020__stddev"]
       zbatter.zbref_war_per_pa2020 = (zbatter.bref_war_per_pa2020 - bref_war_per_pa2020mean["bref_war_per_pa2020__avg"]) / bref_war_per_pa2020stddev["bref_war_per_pa2020__stddev"]
       zbatter.zbref_runs_above_avg_off_per_pa2020 = (zbatter.bref_runs_above_avg_off_per_pa2020 - bref_runs_above_avg_off_per_pa2020mean["bref_runs_above_avg_off_per_pa2020__avg"]) / bref_runs_above_avg_off_per_pa2020stddev["bref_runs_above_avg_off_per_pa2020__stddev"]
       zbatter.zbref_war_off_per_pa2020 = (zbatter.bref_war_off_per_pa2020 - bref_war_off_per_pa2020mean["bref_war_off_per_pa2020__avg"]) / bref_war_off_per_pa2020stddev["bref_war_off_per_pa2020__stddev"]
       zbatter.zbref_war_def_per_pa2020 = (zbatter.bref_war_def_per_pa2020 - bref_war_def_per_pa2020mean["bref_war_def_per_pa2020__avg"]) / bref_war_def_per_pa2020stddev["bref_war_def_per_pa2020__stddev"]
     if zbatter.loaded_bs_x_2020 == True:
       zbatter.zxavg2020 = (zbatter.xavg2020 - xavg2020mean["xavg2020__avg"]) / xavg2020stddev["xavg2020__stddev"]
       zbatter.zbip2020 = (zbatter.bip2020 - bip2020mean["bip2020__avg"]) / bip2020stddev["bip2020__stddev"]
       zbatter.zxslg2020 = (zbatter.xslg2020 - xslg2020mean["xslg2020__avg"]) / xslg2020stddev["xslg2020__stddev"]
       zbatter.zxavgdiff2020 = (zbatter.xavgdiff2020 - xavgdiff2020mean["xavgdiff2020__avg"]) / xavgdiff2020stddev["xavgdiff2020__stddev"]
       zbatter.zxslgdiff2020 = (zbatter.xslgdiff2020 - xslgdiff2020mean["xslgdiff2020__avg"]) / xslgdiff2020stddev["xslgdiff2020__stddev"]
       zbatter.zxwoba2020 = (zbatter.xwoba2020 - xwoba2020mean["xwoba2020__avg"]) / xwoba2020stddev["xwoba2020__stddev"]
       zbatter.zxwobadiff2020 = (zbatter.xwobadiff2020 - xwobadiff2020mean["xwobadiff2020__avg"]) / xwobadiff2020stddev["xwobadiff2020__stddev"]
     if zbatter.loaded_bs_barrel_2020 == True:
       zbatter.zanglesweetspotpercent2020 = (zbatter.anglesweetspotpercent2020 - anglesweetspotpercent2020mean["anglesweetspotpercent2020__avg"]) / anglesweetspotpercent2020stddev["anglesweetspotpercent2020__stddev"]
       zbatter.zmax_hit_speed2020 = (zbatter.max_hit_speed2020 - max_hit_speed2020mean["max_hit_speed2020__avg"]) / max_hit_speed2020stddev["max_hit_speed2020__stddev"]
       zbatter.zavg_hit_speed2020 = (zbatter.avg_hit_speed2020 - avg_hit_speed2020mean["avg_hit_speed2020__avg"]) / avg_hit_speed2020stddev["avg_hit_speed2020__stddev"]
       zbatter.zmax_distance2020 = (zbatter.max_distance2020 - max_distance2020mean["max_distance2020__avg"]) / max_distance2020stddev["max_distance2020__stddev"]
       zbatter.zavg_distance2020 = (zbatter.avg_distance2020 - avg_distance2020mean["avg_distance2020__avg"]) / avg_distance2020stddev["avg_distance2020__stddev"]
       zbatter.zev95percent2020 = (zbatter.ev95percent2020 - ev95percent2020mean["ev95percent2020__avg"]) / ev95percent2020stddev["ev95percent2020__stddev"]
       zbatter.zbrl_percent2020 = (zbatter.brl_percent2020 - brl_percent2020mean["brl_percent2020__avg"]) / brl_percent2020stddev["brl_percent2020__stddev"]
       zbatter.zbrl_pa2020 = (zbatter.brl_pa2020 - brl_pa2020mean["brl_pa2020__avg"]) / brl_pa2020stddev["brl_pa2020__stddev"]
    #  if zbatter.loaded_bs_fielding_2020 == True:
    #    zbatter.zouts_above_avg2020 = (zbatter.outs_above_avg2020 - outs_above_avg2020mean["outs_above_avg2020__avg"]) / outs_above_avg2020stddev["outs_above_avg2020__stddev"]
    #    zbatter.zfielding_runs_prevented2020 = (zbatter.fielding_runs_prevented2020 - fielding_runs_prevented2020mean["fielding_runs_prevented2020__avg"]) / fielding_runs_prevented2020stddev["fielding_runs_prevented2020__stddev"]
     zbatter.save()

