import decimal
from django.core.management.base import BaseCommand
from app_bb.models import batter
from django.db.models.aggregates import StdDev, Avg


# when this is totally ready to go, just copy and paste + replace 2022 to form the 2021 and 2020 scripts, do the same in models.py
# how do I handle not being loaded? keep it at zero, and just custom write in the big math userweight function to check?
# write in code which checks if dummy exists before running and deletes if it exists

#in all cases, for simplicity, negative z should be bad and positive should be good
#some stats (like batter strikeouts) the inverse is true, so for those stats, I will make note and invert the z value right away
#this way the dummy batter creation doesn't change at all


class Command(BaseCommand):
  def handle(self, *args, **options):
    if batter.objects.filter(lastname = "dummy").exists():
      batter.objects.filter(lastname = "dummy").delete()
    pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("pa2022"))
    pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("pa2022"))
    plus_avg2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_avg2022"))
    plus_avg2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_avg2022"))
    avg2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("avg2022"))
    avg2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("avg2022"))
    obp2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("obp2022"))
    obp2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("obp2022"))
    plus_obp2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_obp2022"))
    plus_obp2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_obp2022"))
    slg2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("slg2022"))
    slg2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("slg2022"))
    plus_slg2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_slg2022"))
    plus_slg2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_slg2022"))
    ops2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("ops2022"))
    ops2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("ops2022"))
    bb_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bb_per_pa2022"))
    bb_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("bb_per_pa2022"))
    plus_bb_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_bb_per_pa2022"))
    plus_bb_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_bb_per_pa2022"))
    plus_k_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_k_per_pa2022"))
    plus_k_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_k_per_pa2022"))
    k_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("k_per_pa2022"))
    k_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("k_per_pa2022"))
    r_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("r_per_pa2022"))
    r_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("r_per_pa2022"))
    rbi_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("rbi_per_pa2022"))
    rbi_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("rbi_per_pa2022"))
    gdp_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("gdp_per_pa2022"))
    gdp_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("gdp_per_pa2022"))
    xSB_added2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xSB_added2022"))
    xSB_added2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("xSB_added2022"))
    xSB_added_percent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xSB_added_percent2022"))
    xSB_added_percent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("xSB_added_percent2022"))
    wRAA2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("wRAA2022"))
    wRAA2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("wRAA2022"))
    wOBA2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("wOBA2022"))
    wOBA2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("wOBA2022"))
    wRC2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("wRC2022"))
    wRC2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("wRC2022"))
    plus_wRC2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_wRC2022"))
    plus_wRC2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_wRC2022"))
    iso2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("iso2022"))
    iso2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("iso2022"))
    plus_iso2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_iso2022"))
    plus_iso2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_iso2022"))
    babip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("babip2022"))
    babip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("babip2022"))
    plus_babip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_babip2022"))
    plus_babip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_babip2022"))
    ld_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("ld_per_bip2022"))
    ld_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("ld_per_bip2022"))
    gb_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("gb_per_bip2022"))
    gb_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("gb_per_bip2022"))
    fb_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fb_per_bip2022"))
    fb_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fb_per_bip2022"))
    iffb_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("iffb_per_bip2022"))
    iffb_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("iffb_per_bip2022"))
    hr_per_fb2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(loaded_hr_per_fb2022 = True).aggregate(StdDev("hr_per_fb2022"))
    hr_per_fb2022mean = batter.objects.all().filter(loaded_2022 = True).filter(loaded_hr_per_fb2022 = True).aggregate(Avg("hr_per_fb2022"))
    bsr2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bsr2022"))
    # print("baserunning total", bsr2022stddev) 1.47900609072223
    bsr2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("bsr2022"))
    # print("baserunning mean", bsr2022mean) 0
    clutch2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("clutch2022"))
    clutch2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("clutch2022"))
    fwar2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fwar2022"))
    fwar2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fwar2022"))
    hardpercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hardpercent2022"))
    hardpercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("hardpercent2022"))
    plus_hardpercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_hardpercent2022"))
    plus_hardpercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_hardpercent2022"))
    hardhitpercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hardhitpercent2022"))
    hardhitpercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("hardhitpercent2022"))
    fwar_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fwar_per_pa2022"))
    fwar_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fwar_per_pa2022"))
    bsr_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bsr_per_pa2022"))
    # print("baserunning per pa", bsr_per_pa2022stddev) 0.00833214477662146
    bsr_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("bsr_per_pa2022"))
    outsidezoneswingpercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("outsidezoneswingpercent2022"))
    outsidezoneswingpercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("outsidezoneswingpercent2022"))
    firstpitchstrikepercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("firstpitchstrikepercent2022"))
    firstpitchstrikepercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("firstpitchstrikepercent2022"))
    swingcontactpercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("swingcontactpercent2022"))
    swingcontactpercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("swingcontactpercent2022"))
    swingingstrikespercent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("swingingstrikespercent2022"))
    swingingstrikespercent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("swingingstrikespercent2022"))
    foff2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("foff2022"))
    foff2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("foff2022"))
    fdef2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(StdDev("fdef2022"))
    # print("defense total", fdef2022stddev) 3.92625378652656
    fdef2022mean = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(Avg("fdef2022"))
    # print("defense mean", fdef2022mean) -0.485714285714286
    ffld2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(StdDev("ffld2022"))
    # print("fielding total", ffld2022stddev) 2.93118745254359
    ffld2022mean = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(Avg("ffld2022"))
    # print("fielding mean", ffld2022mean) 0.0409937888198759
    foff_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("foff_per_pa2022"))
    foff_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("foff_per_pa2022"))
    fdef_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(StdDev("fdef_per_pa2022"))
    # print("defense per pa", fdef_per_pa2022stddev) 0.0245836618867729
    fdef_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(Avg("fdef_per_pa2022"))
    fbat2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fbat2022"))
    # print("batting total", fbat2022stddev) 7.63961508130041
    fbat2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fbat2022"))
    # print("batting mean", fbat2022mean) 0.225819672131148
    ffld_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(StdDev("ffld_per_pa2022"))
    # print("fielding per pa", ffld_per_pa2022stddev) 0.0208832062380861
    ffld_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).filter(fldloaded_2022 = True).aggregate(Avg("ffld_per_pa2022"))
    # barrel_percent2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("barrel_percent2022"))
    # barrel_percent2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("barrel_percent2022"))
    fbat_per_pa2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fbat_per_pa2022"))
    # print("batting per pa", fbat_per_pa2022stddev) 0.0438921952567499
    fbat_per_pa2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fbat_per_pa2022"))
    # maxEV2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("maxEV2022"))
    # maxEV2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("maxEV2022"))
    plus_ld_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_ld_per_bip2022"))
    plus_ld_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_ld_per_bip2022"))
    plus_gb_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_gb_per_bip2022"))
    plus_gb_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_gb_per_bip2022"))
    plus_fb_per_bip2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_fb_per_bip2022"))
    plus_fb_per_bip2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_fb_per_bip2022"))
    spd2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("spd2022"))
    spd2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("spd2022"))
    plus_hr_per_fb2022stddev = batter.objects.all().filter(loaded_2022 = True).filter(loaded_hr_per_fb2022 = True).aggregate(StdDev("plus_hr_per_fb2022"))
    plus_hr_per_fb2022mean = batter.objects.all().filter(loaded_2022 = True).filter(loaded_hr_per_fb2022 = True).aggregate(Avg("plus_hr_per_fb2022"))
    # xBA2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xBA2022"))
    # xBA2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("xBA2022"))
    # fgxSLG2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fgxSLG2022"))
    # fgxSLG2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fgxSLG2022"))
    # fgxWOBA2022stddev = batter.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fgxWOBA2022"))
    # fgxWOBA2022mean = batter.objects.all().filter(loaded_2022 = True).aggregate(Avg("fgxWOBA2022"))
    bref_bsr_runs2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_bsr_runs2022"))
    bref_bsr_runs2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_bsr_runs2022"))
    bref_batting_runs2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_batting_runs2022"))
    bref_batting_runs2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_batting_runs2022"))
    bref_runs_above_avg2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg2022"))
    bref_runs_above_avg2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg2022"))
    bref_gdp_runs2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_gdp_runs2022"))
    bref_gdp_runs2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_gdp_runs2022"))
    bref_runs_above_avg_def2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg_def2022"))
    bref_runs_above_avg_def2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg_def2022"))
    bref_war2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war2022"))
    bref_war2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war2022"))
    bref_runs_above_avg_off2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg_off2022"))
    bref_runs_above_avg_off2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg_off2022"))
    bref_war_def2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war_def2022"))
    bref_war_def2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war_def2022"))
    bref_war_off2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war_off2022"))
    bref_war_off2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war_off2022"))
    plus_ops2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("plus_ops2022"))
    plus_ops2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("plus_ops2022"))
    bref_batting_runs_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_batting_runs_per_pa2022"))
    bref_batting_runs_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_batting_runs_per_pa2022"))
    bref_bsr_runs_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_bsr_runs_per_pa2022"))
    bref_bsr_runs_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_bsr_runs_per_pa2022"))
    bref_gdp_runs_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_gdp_runs_per_pa2022"))
    bref_gdp_runs_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_gdp_runs_per_pa2022"))
    bref_runs_above_avg_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg_per_pa2022"))
    bref_runs_above_avg_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg_per_pa2022"))
    bref_runs_above_avg_def_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg_def_per_pa2022"))
    bref_runs_above_avg_def_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg_def_per_pa2022"))
    bref_war_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war_per_pa2022"))
    bref_war_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war_per_pa2022"))
    bref_runs_above_avg_off_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_runs_above_avg_off_per_pa2022"))
    bref_runs_above_avg_off_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_runs_above_avg_off_per_pa2022"))
    bref_war_off_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war_off_per_pa2022"))
    bref_war_off_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war_off_per_pa2022"))
    bref_war_def_per_pa2022stddev = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(StdDev("bref_war_def_per_pa2022"))
    bref_war_def_per_pa2022mean = batter.objects.all().filter(loaded_bref_2022 = True).aggregate(Avg("bref_war_def_per_pa2022"))
    #baseball savant x
    xavg2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xavg2022"))
    xavg2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xavg2022"))
    bip2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("bip2022"))
    bip2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("bip2022"))
    xslg2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xslg2022"))
    xslg2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xslg2022"))
    xavgdiff2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xavgdiff2022"))
    xavgdiff2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xavgdiff2022"))
    xslgdiff2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xslgdiff2022"))
    xslgdiff2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xslgdiff2022"))
    xwobadiff2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xwobadiff2022"))
    xwobadiff2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xwobadiff2022"))
    xwoba2022stddev = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xwoba2022"))
    xwoba2022mean = batter.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xwoba2022"))
    #baseball savant barrel
    anglesweetspotpercent2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("anglesweetspotpercent2022"))
    anglesweetspotpercent2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("anglesweetspotpercent2022"))
    max_hit_speed2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("max_hit_speed2022"))
    max_hit_speed2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("max_hit_speed2022"))
    avg_hit_speed2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("avg_hit_speed2022"))
    avg_hit_speed2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("avg_hit_speed2022"))
    max_distance2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("max_distance2022"))
    max_distance2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("max_distance2022"))
    avg_distance2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("avg_distance2022"))
    avg_distance2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("avg_distance2022"))
    ev95percent2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("ev95percent2022"))
    ev95percent2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("ev95percent2022"))
    brl_percent2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("brl_percent2022"))
    brl_percent2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("brl_percent2022"))
    brl_pa2022stddev = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("brl_pa2022"))
    brl_pa2022mean = batter.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("brl_pa2022"))
    outs_above_avg2022stddev = batter.objects.all().filter(loaded_bs_fielding_2022 = True).aggregate(StdDev("outs_above_avg2022"))
    outs_above_avg2022mean = batter.objects.all().filter(loaded_bs_fielding_2022 = True).aggregate(Avg("outs_above_avg2022"))
    fielding_runs_prevented2022stddev = batter.objects.all().filter(loaded_bs_fielding_2022 = True).aggregate(StdDev("fielding_runs_prevented2022"))
    fielding_runs_prevented2022mean = batter.objects.all().filter(loaded_bs_fielding_2022 = True).aggregate(Avg("fielding_runs_prevented2022"))
    home_to_first2022stddev = batter.objects.all().filter(loaded_bs_running_2022 = True).aggregate(StdDev("home_to_first2022"))
    home_to_first2022mean = batter.objects.all().filter(loaded_bs_running_2022 = True).aggregate(Avg("home_to_first2022"))
    sprint_speed2022stddev = batter.objects.all().filter(loaded_bs_running_2022 = True).aggregate(StdDev("sprint_speed2022"))
    sprint_speed2022mean = batter.objects.all().filter(loaded_bs_running_2022 = True).aggregate(Avg("sprint_speed2022"))

    for zbatter in batter.objects.all().filter(loaded_2022 = True):
      zbatter.zpa2022 = (zbatter.pa2022 - pa2022mean["pa2022__avg"]) / pa2022stddev["pa2022__stddev"]
      zbatter.zplus_avg2022 = (zbatter.plus_avg2022 - plus_avg2022mean["plus_avg2022__avg"]) / plus_avg2022stddev["plus_avg2022__stddev"]
      zbatter.zavg2022 = (zbatter.avg2022 - avg2022mean["avg2022__avg"]) / avg2022stddev["avg2022__stddev"]
      zbatter.zobp2022 = (zbatter.obp2022 - obp2022mean["obp2022__avg"]) / obp2022stddev["obp2022__stddev"]
      zbatter.zplus_obp2022 = (zbatter.plus_obp2022 - plus_obp2022mean["plus_obp2022__avg"]) / plus_obp2022stddev["plus_obp2022__stddev"]
      zbatter.zslg2022 = (zbatter.slg2022 - slg2022mean["slg2022__avg"]) / slg2022stddev["slg2022__stddev"]
      zbatter.zplus_slg2022 = (zbatter.plus_slg2022 - plus_slg2022mean["plus_slg2022__avg"]) / plus_slg2022stddev["plus_slg2022__stddev"]
      zbatter.zops2022 = (zbatter.ops2022 - ops2022mean["ops2022__avg"]) / ops2022stddev["ops2022__stddev"]
      zbatter.zbb_per_pa2022 = (zbatter.bb_per_pa2022 - bb_per_pa2022mean["bb_per_pa2022__avg"]) / bb_per_pa2022stddev["bb_per_pa2022__stddev"]
      zbatter.zplus_bb_per_pa2022 = (zbatter.plus_bb_per_pa2022 - plus_bb_per_pa2022mean["plus_bb_per_pa2022__avg"]) / plus_bb_per_pa2022stddev["plus_bb_per_pa2022__stddev"]
      #must invert z-score
      zbatter.zplus_k_per_pa2022 = -(zbatter.plus_k_per_pa2022 - plus_k_per_pa2022mean["plus_k_per_pa2022__avg"]) / plus_k_per_pa2022stddev["plus_k_per_pa2022__stddev"]
      #must invert z-score
      zbatter.zk_per_pa2022 = -(zbatter.k_per_pa2022 - k_per_pa2022mean["k_per_pa2022__avg"]) / k_per_pa2022stddev["k_per_pa2022__stddev"]
      zbatter.zr_per_pa2022 = (zbatter.r_per_pa2022 - r_per_pa2022mean["r_per_pa2022__avg"]) / r_per_pa2022stddev["r_per_pa2022__stddev"]
      zbatter.zrbi_per_pa2022 = (zbatter.rbi_per_pa2022 - rbi_per_pa2022mean["rbi_per_pa2022__avg"]) / rbi_per_pa2022stddev["rbi_per_pa2022__stddev"]
      #must invert z-score
      zbatter.zgdp_per_pa2022 = -(zbatter.gdp_per_pa2022 - gdp_per_pa2022mean["gdp_per_pa2022__avg"]) / gdp_per_pa2022stddev["gdp_per_pa2022__stddev"]
      zbatter.zxSB_added2022 = (zbatter.xSB_added2022 - xSB_added2022mean["xSB_added2022__avg"]) / xSB_added2022stddev["xSB_added2022__stddev"]
      zbatter.zxSB_added_percent2022 = (zbatter.xSB_added_percent2022 - xSB_added_percent2022mean["xSB_added_percent2022__avg"]) / xSB_added_percent2022stddev["xSB_added_percent2022__stddev"]
      zbatter.zwRAA2022 = (zbatter.wRAA2022 - wRAA2022mean["wRAA2022__avg"]) / wRAA2022stddev["wRAA2022__stddev"]
      zbatter.zwOBA2022 = (zbatter.wOBA2022 - wOBA2022mean["wOBA2022__avg"]) / wOBA2022stddev["wOBA2022__stddev"]
      zbatter.zwRC2022 = (zbatter.wRC2022 - wRC2022mean["wRC2022__avg"]) / wRC2022stddev["wRC2022__stddev"]
      zbatter.zplus_wRC2022 = (zbatter.plus_wRC2022 - plus_wRC2022mean["plus_wRC2022__avg"]) / plus_wRC2022stddev["plus_wRC2022__stddev"]
      zbatter.ziso2022 = (zbatter.iso2022 - iso2022mean["iso2022__avg"]) / iso2022stddev["iso2022__stddev"]
      zbatter.zplus_iso2022 = (zbatter.plus_iso2022 - plus_iso2022mean["plus_iso2022__avg"]) / plus_iso2022stddev["plus_iso2022__stddev"]
      zbatter.zbabip2022 = (zbatter.babip2022 - babip2022mean["babip2022__avg"]) / babip2022stddev["babip2022__stddev"]
      zbatter.zplus_babip2022 = (zbatter.plus_babip2022 - plus_babip2022mean["plus_babip2022__avg"]) / plus_babip2022stddev["plus_babip2022__stddev"]
      zbatter.zld_per_bip2022 = (zbatter.ld_per_bip2022 - ld_per_bip2022mean["ld_per_bip2022__avg"]) / ld_per_bip2022stddev["ld_per_bip2022__stddev"]
      #must invert z-score
      zbatter.zgb_per_bip2022 = -(zbatter.gb_per_bip2022 - gb_per_bip2022mean["gb_per_bip2022__avg"]) / gb_per_bip2022stddev["gb_per_bip2022__stddev"]
      zbatter.zfb_per_bip2022 = (zbatter.fb_per_bip2022 - fb_per_bip2022mean["fb_per_bip2022__avg"]) / fb_per_bip2022stddev["fb_per_bip2022__stddev"]
      #must invert z-score
      zbatter.ziffb_per_bip2022 = -(zbatter.iffb_per_bip2022 - iffb_per_bip2022mean["iffb_per_bip2022__avg"]) / iffb_per_bip2022stddev["iffb_per_bip2022__stddev"]
      zbatter.zbsr2022 = (zbatter.bsr2022 - bsr2022mean["bsr2022__avg"]) / bsr2022stddev["bsr2022__stddev"]
      zbatter.zclutch2022 = (zbatter.clutch2022 - clutch2022mean["clutch2022__avg"]) / clutch2022stddev["clutch2022__stddev"]
      zbatter.zfwar2022 = (zbatter.fwar2022 - fwar2022mean["fwar2022__avg"]) / fwar2022stddev["fwar2022__stddev"]
      zbatter.zhardpercent2022 = (zbatter.hardpercent2022 - hardpercent2022mean["hardpercent2022__avg"]) / hardpercent2022stddev["hardpercent2022__stddev"]
      zbatter.zplus_hardpercent2022 = (zbatter.plus_hardpercent2022 - plus_hardpercent2022mean["plus_hardpercent2022__avg"]) / plus_hardpercent2022stddev["plus_hardpercent2022__stddev"]
      zbatter.zhardhitpercent2022 = (zbatter.hardhitpercent2022 - hardhitpercent2022mean["hardhitpercent2022__avg"]) / hardhitpercent2022stddev["hardhitpercent2022__stddev"]
      zbatter.zfwar_per_pa2022 = (zbatter.fwar_per_pa2022 - fwar_per_pa2022mean["fwar_per_pa2022__avg"]) / fwar_per_pa2022stddev["fwar_per_pa2022__stddev"]
      zbatter.zbsr_per_pa2022 = (zbatter.bsr_per_pa2022 - bsr_per_pa2022mean["bsr_per_pa2022__avg"]) / bsr_per_pa2022stddev["bsr_per_pa2022__stddev"]
      #must invert z-score
      zbatter.zoutsidezoneswingpercent2022 = -(zbatter.outsidezoneswingpercent2022 - outsidezoneswingpercent2022mean["outsidezoneswingpercent2022__avg"]) / outsidezoneswingpercent2022stddev["outsidezoneswingpercent2022__stddev"]
      #must invert z-score
      zbatter.zfirstpitchstrikepercent2022 = -(zbatter.firstpitchstrikepercent2022 - firstpitchstrikepercent2022mean["firstpitchstrikepercent2022__avg"]) / firstpitchstrikepercent2022stddev["firstpitchstrikepercent2022__stddev"]
      zbatter.zswingcontactpercent2022 = (zbatter.swingcontactpercent2022 - swingcontactpercent2022mean["swingcontactpercent2022__avg"]) / swingcontactpercent2022stddev["swingcontactpercent2022__stddev"]
      #must invert z-score
      zbatter.zswingingstrikespercent2022 = -(zbatter.swingingstrikespercent2022 - swingingstrikespercent2022mean["swingingstrikespercent2022__avg"]) / swingingstrikespercent2022stddev["swingingstrikespercent2022__stddev"]
      zbatter.zfoff2022 = (zbatter.foff2022 - foff2022mean["foff2022__avg"]) / foff2022stddev["foff2022__stddev"]
      zbatter.zfoff_per_pa2022 = (zbatter.foff_per_pa2022 - foff_per_pa2022mean["foff_per_pa2022__avg"]) / foff_per_pa2022stddev["foff_per_pa2022__stddev"]
      zbatter.zfbat2022 = (zbatter.fbat2022 - fbat2022mean["fbat2022__avg"]) / fbat2022stddev["fbat2022__stddev"]
      if zbatter.fldloaded_2022 == True:
        zbatter.zfdef2022 = (zbatter.fdef2022 - fdef2022mean["fdef2022__avg"]) / fdef2022stddev["fdef2022__stddev"]
        zbatter.zffld2022 = (zbatter.ffld2022 - ffld2022mean["ffld2022__avg"]) / ffld2022stddev["ffld2022__stddev"]
        zbatter.zfdef_per_pa2022 = (zbatter.fdef_per_pa2022 - fdef_per_pa2022mean["fdef_per_pa2022__avg"]) / fdef_per_pa2022stddev["fdef_per_pa2022__stddev"]
        zbatter.zffld_per_pa2022 = (zbatter.ffld_per_pa2022 - ffld_per_pa2022mean["ffld_per_pa2022__avg"]) / ffld_per_pa2022stddev["ffld_per_pa2022__stddev"]
      else:
        zbatter.zfdef2022 = 0
        zbatter.zffld2022 = 0
        zbatter.zfdef_per_pa2022 = 0
        zbatter.zffld_per_pa2022 = 0
      #zbatter.zbarrel_percent2022 = (zbatter.barrel_percent2022 - barrel_percent2022mean["barrel_percent2022__avg"]) / barrel_percent2022stddev["barrel_percent2022__stddev"]
      zbatter.zfbat_per_pa2022 = (zbatter.fbat_per_pa2022 - fbat_per_pa2022mean["fbat_per_pa2022__avg"]) / fbat_per_pa2022stddev["fbat_per_pa2022__stddev"]
      #zbatter.zmaxEV2022 = (zbatter.maxEV2022 - maxEV2022mean["maxEV2022__avg"]) / maxEV2022stddev["maxEV2022__stddev"]
      #TEMP zbatter.zplus_ld_per_bip2022 = (zbatter.plus_ld_per_bip2022 - plus_ld_per_bip2022mean["plus_ld_per_bip2022__avg"]) / plus_ld_per_bip2022stddev["plus_ld_per_bip2022__stddev"]
      
      #must invert z-score
      zbatter.zplus_gb_per_bip2022 = -(zbatter.plus_gb_per_bip2022 - plus_gb_per_bip2022mean["plus_gb_per_bip2022__avg"]) / plus_gb_per_bip2022stddev["plus_gb_per_bip2022__stddev"]
      zbatter.zplus_fb_per_bip2022 = (zbatter.plus_fb_per_bip2022 - plus_fb_per_bip2022mean["plus_fb_per_bip2022__avg"]) / plus_fb_per_bip2022stddev["plus_fb_per_bip2022__stddev"]
      zbatter.zspd2022 = (zbatter.spd2022 - spd2022mean["spd2022__avg"]) / spd2022stddev["spd2022__stddev"]
      if zbatter.loaded_hr_per_fb2022 == True:
        zbatter.zplus_hr_per_fb2022 = (zbatter.plus_hr_per_fb2022 - plus_hr_per_fb2022mean["plus_hr_per_fb2022__avg"]) / plus_hr_per_fb2022stddev["plus_hr_per_fb2022__stddev"]
        zbatter.zhr_per_fb2022 = (zbatter.hr_per_fb2022 - hr_per_fb2022mean["hr_per_fb2022__avg"]) / hr_per_fb2022stddev["hr_per_fb2022__stddev"]
      else:
        zbatter.zplus_hr_per_fb2022 = 0
        zbatter.zhr_per_fb2022 = 0
      # zbatter.zxBA2022 = (zbatter.xBA2022 - xBA2022mean["xBA2022__avg"]) / xBA2022stddev["xBA2022__stddev"]
      # zbatter.zfgxSLG2022 = (zbatter.fgxSLG2022 - fgxSLG2022mean["fgxSLG2022__avg"]) / fgxSLG2022stddev["fgxSLG2022__stddev"]
      # zbatter.zfgxWOBA2022 = (zbatter.fgxWOBA2022 - fgxWOBA2022mean["fgxWOBA2022__avg"]) / fgxWOBA2022stddev["fgxWOBA2022__stddev"]
      if zbatter.loaded_bref_2022 == True:
        zbatter.zbref_bsr_runs2022 = (zbatter.bref_bsr_runs2022 - bref_bsr_runs2022mean["bref_bsr_runs2022__avg"]) / bref_bsr_runs2022stddev["bref_bsr_runs2022__stddev"]
        zbatter.zbref_batting_runs2022 = (zbatter.bref_batting_runs2022 - bref_batting_runs2022mean["bref_batting_runs2022__avg"]) / bref_batting_runs2022stddev["bref_batting_runs2022__stddev"]
        zbatter.zbref_runs_above_avg2022 = (zbatter.bref_runs_above_avg2022 - bref_runs_above_avg2022mean["bref_runs_above_avg2022__avg"]) / bref_runs_above_avg2022stddev["bref_runs_above_avg2022__stddev"]
        zbatter.zbref_gdp_runs2022 = (zbatter.bref_gdp_runs2022 - bref_gdp_runs2022mean["bref_gdp_runs2022__avg"]) / bref_gdp_runs2022stddev["bref_gdp_runs2022__stddev"]
        zbatter.zbref_runs_above_avg_def2022 = (zbatter.bref_runs_above_avg_def2022 - bref_runs_above_avg_def2022mean["bref_runs_above_avg_def2022__avg"]) / bref_runs_above_avg_def2022stddev["bref_runs_above_avg_def2022__stddev"]
        zbatter.zbref_war2022 = (zbatter.bref_war2022 - bref_war2022mean["bref_war2022__avg"]) / bref_war2022stddev["bref_war2022__stddev"]
        zbatter.zbref_runs_above_avg_off2022 = (zbatter.bref_runs_above_avg_off2022 - bref_runs_above_avg_off2022mean["bref_runs_above_avg_off2022__avg"]) / bref_runs_above_avg_off2022stddev["bref_runs_above_avg_off2022__stddev"]
        zbatter.zbref_war_def2022 = (zbatter.bref_war_def2022 - bref_war_def2022mean["bref_war_def2022__avg"]) / bref_war_def2022stddev["bref_war_def2022__stddev"]
        zbatter.zbref_war_off2022 = (zbatter.bref_war_off2022 - bref_war_off2022mean["bref_war_off2022__avg"]) / bref_war_off2022stddev["bref_war_off2022__stddev"]
        zbatter.zplus_ops2022 = (zbatter.plus_ops2022 - plus_ops2022mean["plus_ops2022__avg"]) / plus_ops2022stddev["plus_ops2022__stddev"]
        zbatter.zbref_batting_runs_per_pa2022 = (zbatter.bref_batting_runs_per_pa2022 - bref_batting_runs_per_pa2022mean["bref_batting_runs_per_pa2022__avg"]) / bref_batting_runs_per_pa2022stddev["bref_batting_runs_per_pa2022__stddev"]
        zbatter.zbref_bsr_runs_per_pa2022 = (zbatter.bref_bsr_runs_per_pa2022 - bref_bsr_runs_per_pa2022mean["bref_bsr_runs_per_pa2022__avg"]) / bref_bsr_runs_per_pa2022stddev["bref_bsr_runs_per_pa2022__stddev"]
        zbatter.zbref_gdp_runs_per_pa2022 = (zbatter.bref_gdp_runs_per_pa2022 - bref_gdp_runs_per_pa2022mean["bref_gdp_runs_per_pa2022__avg"]) / bref_gdp_runs_per_pa2022stddev["bref_gdp_runs_per_pa2022__stddev"]
        zbatter.zbref_runs_above_avg_per_pa2022 = (zbatter.bref_runs_above_avg_per_pa2022 - bref_runs_above_avg_per_pa2022mean["bref_runs_above_avg_per_pa2022__avg"]) / bref_runs_above_avg_per_pa2022stddev["bref_runs_above_avg_per_pa2022__stddev"]
        zbatter.zbref_runs_above_avg_def_per_pa2022 = (zbatter.bref_runs_above_avg_def_per_pa2022 - bref_runs_above_avg_def_per_pa2022mean["bref_runs_above_avg_def_per_pa2022__avg"]) / bref_runs_above_avg_def_per_pa2022stddev["bref_runs_above_avg_def_per_pa2022__stddev"]
        zbatter.zbref_war_per_pa2022 = (zbatter.bref_war_per_pa2022 - bref_war_per_pa2022mean["bref_war_per_pa2022__avg"]) / bref_war_per_pa2022stddev["bref_war_per_pa2022__stddev"]
        zbatter.zbref_runs_above_avg_off_per_pa2022 = (zbatter.bref_runs_above_avg_off_per_pa2022 - bref_runs_above_avg_off_per_pa2022mean["bref_runs_above_avg_off_per_pa2022__avg"]) / bref_runs_above_avg_off_per_pa2022stddev["bref_runs_above_avg_off_per_pa2022__stddev"]
        zbatter.zbref_war_off_per_pa2022 = (zbatter.bref_war_off_per_pa2022 - bref_war_off_per_pa2022mean["bref_war_off_per_pa2022__avg"]) / bref_war_off_per_pa2022stddev["bref_war_off_per_pa2022__stddev"]
        zbatter.zbref_war_def_per_pa2022 = (zbatter.bref_war_def_per_pa2022 - bref_war_def_per_pa2022mean["bref_war_def_per_pa2022__avg"]) / bref_war_def_per_pa2022stddev["bref_war_def_per_pa2022__stddev"]
      if zbatter.loaded_bs_x_2022 == True:
        zbatter.zxavg2022 = (zbatter.xavg2022 - xavg2022mean["xavg2022__avg"]) / xavg2022stddev["xavg2022__stddev"]
        zbatter.zbip2022 = (zbatter.bip2022 - bip2022mean["bip2022__avg"]) / bip2022stddev["bip2022__stddev"]
        zbatter.zxslg2022 = (zbatter.xslg2022 - xslg2022mean["xslg2022__avg"]) / xslg2022stddev["xslg2022__stddev"]
        zbatter.zxavgdiff2022 = (zbatter.xavgdiff2022 - xavgdiff2022mean["xavgdiff2022__avg"]) / xavgdiff2022stddev["xavgdiff2022__stddev"]
        zbatter.zxslgdiff2022 = (zbatter.xslgdiff2022 - xslgdiff2022mean["xslgdiff2022__avg"]) / xslgdiff2022stddev["xslgdiff2022__stddev"]
        zbatter.zxwoba2022 = (zbatter.xwoba2022 - xwoba2022mean["xwoba2022__avg"]) / xwoba2022stddev["xwoba2022__stddev"]
        zbatter.zxwobadiff2022 = (zbatter.xwobadiff2022 - xwobadiff2022mean["xwobadiff2022__avg"]) / xwobadiff2022stddev["xwobadiff2022__stddev"]
      if zbatter.loaded_bs_barrel_2022 == True:
        zbatter.zanglesweetspotpercent2022 = (zbatter.anglesweetspotpercent2022 - anglesweetspotpercent2022mean["anglesweetspotpercent2022__avg"]) / anglesweetspotpercent2022stddev["anglesweetspotpercent2022__stddev"]
        zbatter.zmax_hit_speed2022 = (zbatter.max_hit_speed2022 - max_hit_speed2022mean["max_hit_speed2022__avg"]) / max_hit_speed2022stddev["max_hit_speed2022__stddev"]
        zbatter.zavg_hit_speed2022 = (zbatter.avg_hit_speed2022 - avg_hit_speed2022mean["avg_hit_speed2022__avg"]) / avg_hit_speed2022stddev["avg_hit_speed2022__stddev"]
        zbatter.zmax_distance2022 = (zbatter.max_distance2022 - max_distance2022mean["max_distance2022__avg"]) / max_distance2022stddev["max_distance2022__stddev"]
        zbatter.zavg_distance2022 = (zbatter.avg_distance2022 - avg_distance2022mean["avg_distance2022__avg"]) / avg_distance2022stddev["avg_distance2022__stddev"]
        zbatter.zev95percent2022 = (zbatter.ev95percent2022 - ev95percent2022mean["ev95percent2022__avg"]) / ev95percent2022stddev["ev95percent2022__stddev"]
        zbatter.zbrl_percent2022 = (zbatter.brl_percent2022 - brl_percent2022mean["brl_percent2022__avg"]) / brl_percent2022stddev["brl_percent2022__stddev"]
        zbatter.zbrl_pa2022 = (zbatter.brl_pa2022 - brl_pa2022mean["brl_pa2022__avg"]) / brl_pa2022stddev["brl_pa2022__stddev"]
      if zbatter.loaded_bs_fielding_2022 == True:
        zbatter.zouts_above_avg2022 = (zbatter.outs_above_avg2022 - outs_above_avg2022mean["outs_above_avg2022__avg"]) / outs_above_avg2022stddev["outs_above_avg2022__stddev"]
        zbatter.zfielding_runs_prevented2022 = (zbatter.fielding_runs_prevented2022 - fielding_runs_prevented2022mean["fielding_runs_prevented2022__avg"]) / fielding_runs_prevented2022stddev["fielding_runs_prevented2022__stddev"]
      if zbatter.loaded_bs_running_2022 == True:
        #must invert z-score
        zbatter.zhome_to_first2022 = -(zbatter.home_to_first2022 - home_to_first2022mean["home_to_first2022__avg"]) / home_to_first2022stddev["home_to_first2022__stddev"]
        zbatter.zsprint_speed2022 = (zbatter.sprint_speed2022 - sprint_speed2022mean["sprint_speed2022__avg"]) / sprint_speed2022stddev["sprint_speed2022__stddev"]
      zbatter.save()
