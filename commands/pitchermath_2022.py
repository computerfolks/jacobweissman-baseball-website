import decimal
from django.core.management.base import BaseCommand
from app_bb.models import pitcher
from django.db.models.aggregates import StdDev, Avg

# for other math scripts, you will need to filter for some of the stats. if you want to handle pitcher-batters, you can always increase sample size requirement or even just sample of the standard dev / mean calculations by with exclude less than 50 innings, for example
#takes <20 seconds to run
# when this is totally ready to go, just copy and paste + replace 2022 to form the 2021 and 2020 scripts, do the same in models.py
# write in code which checks if dummy exists before running and deletes if it exists

#see battermath for explanation of inverting the z-score

class Command(BaseCommand):
  def handle(self, *args, **options):
    if pitcher.objects.filter(lastname = "dummy").exists():
      pitcher.objects.filter(lastname = "dummy").delete()
    winningpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("winningpercent2022"))
    winningpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("winningpercent2022"))
    war2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("war2022"))
    war2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("war2022"))
    era2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("era2022"))
    era2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("era2022"))
    shutouts2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("shutouts2022"))
    shutouts2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("shutouts2022"))
    saves2022stddev = pitcher.objects.all().filter(loaded_2022 = True).exclude(saves2022 = 0).aggregate(StdDev("saves2022"))
    saves2022mean = pitcher.objects.all().filter(loaded_2022 = True).exclude(saves2022 = 0).aggregate(Avg("saves2022"))
    savepercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).exclude(saves2022 = 0).aggregate(StdDev("savepercent2022"))
    savepercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).exclude(saves2022 = 0).aggregate(Avg("savepercent2022"))
    innings2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("innings2022"))
    innings2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("innings2022"))
    battersfaced2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("battersfaced2022"))
    battersfaced2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("battersfaced2022"))
    hits2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hits2022"))
    hits2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("hits2022"))
    runs2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("runs2022"))
    runs2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("runs2022"))
    # runsaverage2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("runsaverage2022"))
    # runsaverage2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("runsaverage2022"))
    homeruns2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("homeruns2022"))
    homeruns2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("homeruns2022"))
    bbhbp2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bbhbp2022"))
    bbhbp2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("bbhbp2022"))
    k2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("k2022"))
    k2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("k2022"))
    thrownforkpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("thrownforkpercent2022"))
    thrownforkpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("thrownforkpercent2022"))
    kpernine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("kpernine2022"))
    kpernine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("kpernine2022"))
    bbpernine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bbpernine2022"))
    bbpernine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("bbpernine2022"))
    hitpernine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hitpernine2022"))
    hitpernine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("hitpernine2022"))
    hrpernine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hrpernine2022"))
    hrpernine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("hrpernine2022"))
    kperbb2022stddev = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_2022 = True).aggregate(StdDev("kperbb2022"))
    kperbb2022mean = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_2022 = True).aggregate(Avg("kperbb2022"))
    avg2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("avg2022"))
    avg2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("avg2022"))
    whip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("whip2022"))
    whip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("whip2022"))
    babip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("babip2022"))
    babip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("babip2022"))
    lobpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("lobpercent2022"))
    lobpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("lobpercent2022"))
    hrperfb2022stddev = pitcher.objects.all().filter(loaded_hrperfb2022 = True).filter(loaded_2022 = True).aggregate(StdDev("hrperfb2022"))
    hrperfb2022mean = pitcher.objects.all().filter(loaded_hrperfb2022 = True).filter(loaded_2022 = True).aggregate(Avg("hrperfb2022"))
    fip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fip2022"))
    fip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("fip2022"))
    gbperfb2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("gbperfb2022"))
    gbperfb2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("gbperfb2022"))
    gbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("gbpercent2022"))
    gbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("gbpercent2022"))
    iffbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("iffbpercent2022"))
    iffbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("iffbpercent2022"))
    ldpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("ldpercent2022"))
    ldpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("ldpercent2022"))
    fbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fbpercent2022"))
    fbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("fbpercent2022"))
    rar2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("rar2022"))
    rar2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("rar2022"))
    tera2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("tera2022"))
    tera2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("tera2022"))
    xfip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xfip2022"))
    xfip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("xfip2022"))
    wpa2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("wpa2022"))
    wpa2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("wpa2022"))
    retwentyfour2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("retwentyfour2022"))
    retwentyfour2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("retwentyfour2022"))
    clutch2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("clutch2022"))
    clutch2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("clutch2022"))
    outsidezoneswingpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("outsidezoneswingpercent2022"))
    outsidezoneswingpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("outsidezoneswingpercent2022"))
    firstpitchstrikepercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("firstpitchstrikepercent2022"))
    firstpitchstrikepercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("firstpitchstrikepercent2022"))
    swingingstrikespercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("swingingstrikespercent2022"))
    swingingstrikespercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("swingingstrikespercent2022"))
    shutdowns2022stddev = pitcher.objects.all().filter(loaded_2022 = True).exclude(shutdowns2022 = 0).aggregate(StdDev("shutdowns2022"))
    shutdowns2022mean = pitcher.objects.all().filter(loaded_2022 = True).exclude(shutdowns2022 = 0).aggregate(Avg("shutdowns2022"))
    meltdowns2022stddev = pitcher.objects.all().filter(loaded_2022 = True).exclude(meltdowns2022 = 0).aggregate(StdDev("meltdowns2022"))
    meltdowns2022mean = pitcher.objects.all().filter(loaded_2022 = True).exclude(meltdowns2022 = 0).aggregate(Avg("meltdowns2022"))
    eraminus2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("eraminus2022"))
    eraminus2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("eraminus2022"))
    fipminus2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("fipminus2022"))
    fipminus2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("fipminus2022"))
    xfipminus2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xfipminus2022"))
    xfipminus2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("xfipminus2022"))
    bbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("bbpercent2022"))
    bbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("bbpercent2022"))
    cswpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("cswpercent2022"))
    cswpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("cswpercent2022"))
    softpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("softpercent2022"))
    softpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("softpercent2022"))
    mediumpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("mediumpercent2022"))
    mediumpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("mediumpercent2022"))
    softplusmediumpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("softplusmediumpercent2022"))
    softplusmediumpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("softplusmediumpercent2022"))
    runsaverage2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("runsaverage2022"))
    runsaverage2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("runsaverage2022"))
    softplusmediumpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("softplusmediumpercent2022"))
    softplusmediumpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("softplusmediumpercent2022"))
    kwera2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("kwera2022"))
    kwera2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("kwera2022"))
    kpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("kpercent2022"))
    kpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("kpercent2022"))
    weakpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("weakpercent2022"))
    weakpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("weakpercent2022"))
    siera2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("siera2022"))
    siera2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("siera2022"))
    plus_k_per_nine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_k_per_nine2022"))
    plus_k_per_nine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_k_per_nine2022"))
    plus_bb_per_nine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_bb_per_nine2022"))
    plus_bb_per_nine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_bb_per_nine2022"))
    plus_k_per_bb2022stddev = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_2022 = True).aggregate(StdDev("plus_k_per_bb2022"))
    plus_k_per_bb2022mean = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_2022 = True).aggregate(Avg("plus_k_per_bb2022"))
    plus_h_per_nine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_h_per_nine2022"))
    plus_h_per_nine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_h_per_nine2022"))
    plus_hr_per_nine2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_hr_per_nine2022"))
    plus_hr_per_nine2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_hr_per_nine2022"))
    plus_avg2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_avg2022"))
    plus_avg2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_avg2022"))
    plus_whip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_whip2022"))
    plus_whip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_whip2022"))
    plus_babip2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_babip2022"))
    plus_babip2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_babip2022"))
    plus_lobpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_lobpercent2022"))
    plus_lobpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_lobpercent2022"))
    plus_kpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_kpercent2022"))
    plus_kpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_kpercent2022"))
    plus_bbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_bbpercent2022"))
    plus_bbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_bbpercent2022"))
    plus_ldpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_ldpercent2022"))
    plus_ldpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_ldpercent2022"))
    plus_gbpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_gbpercent2022"))
    plus_gbpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_gbpercent2022"))
    plus_hrperfb2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_hrperfb2022"))
    plus_hrperfb2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_hrperfb2022"))
    plus_softpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_softpercent2022"))
    plus_softpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_softpercent2022"))
    plus_mediumpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("plus_mediumpercent2022"))
    plus_mediumpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("plus_mediumpercent2022"))
    barrel_percent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("barrel_percent2022"))
    barrel_percent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("barrel_percent2022"))
    hardhitpercent2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("hardhitpercent2022"))
    hardhitpercent2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("hardhitpercent2022"))
    averageev2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("averageev2022"))
    averageev2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("averageev2022"))
    averagela2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("averagela2022"))
    averagela2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("averagela2022"))
    xera2022stddev = pitcher.objects.all().filter(loaded_2022 = True).aggregate(StdDev("xera2022"))
    xera2022mean = pitcher.objects.all().filter(loaded_2022 = True).aggregate(Avg("xera2022"))

    #baseball savant barrel 2022
    bbevents2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("bbevents2022"))
    bbevents2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("bbevents2022"))
    #avghitangle2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("avghitangle2022"))
    #avghitangle2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("avghitangle2022"))
    anglesweetspotpercent2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("anglesweetspotpercent2022"))
    anglesweetspotpercent2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("anglesweetspotpercent2022"))
    #anglehitspeed2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("anglehitspeed2022"))
    #anglehitspeed2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("anglehitspeed2022"))
    #bsgbpercent2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("bsgbpercent2022"))
    #bsgbpercent2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("bsgbpercent2022"))
    avgdistance2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("avgdistance2022"))
    avgdistance2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("avgdistance2022"))
    ev95plus2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("ev95plus2022"))
    ev95plus2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("ev95plus2022"))
    #brlpercent2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("brlpercent2022"))
    #brlpercent2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("brlpercent2022"))
    ev95pluspercent2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("ev95pluspercent2022"))
    ev95pluspercent2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("ev95pluspercent2022"))
    brlperpa2022stddev = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(StdDev("brlperpa2022"))
    brlperpa2022mean = pitcher.objects.all().filter(loaded_bs_barrel_2022 = True).aggregate(Avg("brlperpa2022"))

    #baseball savant expected 2022
    bip2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("bip2022"))
    bip2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("bip2022"))
    xavg2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xavg2022"))
    xavg2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xavg2022"))
    xavgdiff2022stddev = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_bs_x_2022 = True).aggregate(StdDev("xavgdiff2022"))
    xavgdiff2022mean = pitcher.objects.all().filter(loaded_k_per_bb2022 = True).filter(loaded_bs_x_2022 = True).aggregate(Avg("xavgdiff2022"))
    slg2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("slg2022"))
    slg2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("slg2022"))
    xslg2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xslg2022"))
    xslg2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xslg2022"))
    xslgdiff2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xslgdiff2022"))
    xslgdiff2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xslgdiff2022"))
    woba2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("woba2022"))
    woba2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("woba2022"))
    xwoba2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xwoba2022"))
    xwoba2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xwoba2022"))
    xwobadiff2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xwobadiff2022"))
    xwobadiff2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xwobadiff2022"))
    #2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("bsera2022"))
    #bsera2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("bsera2022"))
    #bsxera2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("bsxera2022"))
    #bsxera2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("bsxera2022"))
    xeradiff2022stddev = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(StdDev("xeradiff2022"))
    xeradiff2022mean = pitcher.objects.all().filter(loaded_bs_x_2022 = True).aggregate(Avg("xeradiff2022"))
 


    for zpitcher in pitcher.objects.all().filter(loaded_2022 = True):
      zpitcher.zwinningpercent2022 = (zpitcher.winningpercent2022 - winningpercent2022mean["winningpercent2022__avg"]) / winningpercent2022stddev["winningpercent2022__stddev"]
      zpitcher.zwar2022 = (zpitcher.war2022 - war2022mean["war2022__avg"]) / war2022stddev["war2022__stddev"]
      #must invert z-score
      zpitcher.zera2022 = -(zpitcher.era2022 - era2022mean["era2022__avg"]) / era2022stddev["era2022__stddev"]
      zpitcher.zshutouts2022 = (zpitcher.shutouts2022 - shutouts2022mean["shutouts2022__avg"]) / shutouts2022stddev["shutouts2022__stddev"]
      if zpitcher.saves2022 > 1:
        zpitcher.zsaves2022 = (zpitcher.saves2022 - saves2022mean["saves2022__avg"]) / saves2022stddev["saves2022__stddev"]
        zpitcher.zsavepercent2022 = (zpitcher.savepercent2022 - savepercent2022mean["savepercent2022__avg"]) / savepercent2022stddev["savepercent2022__stddev"]
      else:
        zpitcher.zsaves2022 = 0
        zpitcher.zsavepercent2022 = 0
      zpitcher.zinnings2022 = (zpitcher.innings2022 - innings2022mean["innings2022__avg"]) / innings2022stddev["innings2022__stddev"]
      zpitcher.zbattersfaced2022 = (zpitcher.battersfaced2022 - battersfaced2022mean["battersfaced2022__avg"]) / battersfaced2022stddev["battersfaced2022__stddev"]
      zpitcher.zhits2022 = (zpitcher.hits2022 - hits2022mean["hits2022__avg"]) / hits2022stddev["hits2022__stddev"]
      zpitcher.zruns2022 = (zpitcher.runs2022 - runs2022mean["runs2022__avg"]) / runs2022stddev["runs2022__stddev"]
      # #must invert z-score
      # zpitcher.zrunsaverage2022 = -(zpitcher.runsaverage2022 - runsaverage2022mean["runsaverage2022__avg"]) / runsaverage2022stddev["runsaverage2022__stddev"]
      zpitcher.zhomeruns2022 = (zpitcher.homeruns2022 - homeruns2022mean["homeruns2022__avg"]) / homeruns2022stddev["homeruns2022__stddev"]
      zpitcher.zbbhbp2022 = (zpitcher.bbhbp2022 - bbhbp2022mean["bbhbp2022__avg"]) / bbhbp2022stddev["bbhbp2022__stddev"]
      zpitcher.zk2022 = (zpitcher.k2022 - k2022mean["k2022__avg"]) / k2022stddev["k2022__stddev"]
      zpitcher.zthrownforkpercent2022 = (zpitcher.thrownforkpercent2022 - thrownforkpercent2022mean["thrownforkpercent2022__avg"]) / thrownforkpercent2022stddev["thrownforkpercent2022__stddev"]
      zpitcher.zkpernine2022 = (zpitcher.kpernine2022 - kpernine2022mean["kpernine2022__avg"]) / kpernine2022stddev["kpernine2022__stddev"]
      #must invert z-score
      zpitcher.zbbpernine2022 = -(zpitcher.bbpernine2022 - bbpernine2022mean["bbpernine2022__avg"]) / bbpernine2022stddev["bbpernine2022__stddev"]
      #must invert z-score
      zpitcher.zhitpernine2022 = -(zpitcher.hitpernine2022 - hitpernine2022mean["hitpernine2022__avg"]) / hitpernine2022stddev["hitpernine2022__stddev"]
      #must invert z-score
      zpitcher.zhrpernine2022 = -(zpitcher.hrpernine2022 - hrpernine2022mean["hrpernine2022__avg"]) / hrpernine2022stddev["hrpernine2022__stddev"]
      zpitcher.zkperbb2022 = (zpitcher.kperbb2022 - kperbb2022mean["kperbb2022__avg"]) / kperbb2022stddev["kperbb2022__stddev"]
      #must invert z-score
      zpitcher.zavg2022 = -(zpitcher.avg2022 - avg2022mean["avg2022__avg"]) / avg2022stddev["avg2022__stddev"]
      #must invert z-score
      zpitcher.zwhip2022 = -(zpitcher.whip2022 - whip2022mean["whip2022__avg"]) / whip2022stddev["whip2022__stddev"]
      #must invert z-score
      zpitcher.zbabip2022 = -(zpitcher.babip2022 - babip2022mean["babip2022__avg"]) / babip2022stddev["babip2022__stddev"]
      #must invert z-score
      zpitcher.zhrperfb2022 = -(zpitcher.hrperfb2022 - hrperfb2022mean["hrperfb2022__avg"]) / hrperfb2022stddev["hrperfb2022__stddev"]
      #must invert z-score
      zpitcher.zfip2022 = -(zpitcher.fip2022 - fip2022mean["fip2022__avg"]) / fip2022stddev["fip2022__stddev"]
      zpitcher.zgbperfb2022 = (zpitcher.gbperfb2022 - gbperfb2022mean["gbperfb2022__avg"]) / gbperfb2022stddev["gbperfb2022__stddev"]
      zpitcher.zgbpercent2022 = (zpitcher.gbpercent2022 - gbpercent2022mean["gbpercent2022__avg"]) / gbpercent2022stddev["gbpercent2022__stddev"]
      zpitcher.ziffbpercent2022 = (zpitcher.iffbpercent2022 - iffbpercent2022mean["iffbpercent2022__avg"]) / iffbpercent2022stddev["iffbpercent2022__stddev"]
      #must invert z-score
      zpitcher.zldpercent2022 = -(zpitcher.ldpercent2022 - ldpercent2022mean["ldpercent2022__avg"]) / ldpercent2022stddev["ldpercent2022__stddev"]
      #must invert z-score
      zpitcher.zfbpercent2022 = -(zpitcher.fbpercent2022 - fbpercent2022mean["fbpercent2022__avg"]) / fbpercent2022stddev["fbpercent2022__stddev"]
      zpitcher.zrar2022 = (zpitcher.rar2022 - rar2022mean["rar2022__avg"]) / rar2022stddev["rar2022__stddev"]
      #must invert z-score
      zpitcher.ztera2022 = -(zpitcher.tera2022 - tera2022mean["tera2022__avg"]) / tera2022stddev["tera2022__stddev"]
      #must invert z-score
      zpitcher.zxfip2022 = -(zpitcher.xfip2022 - xfip2022mean["xfip2022__avg"]) / xfip2022stddev["xfip2022__stddev"]
      zpitcher.zwpa2022 = (zpitcher.wpa2022 - wpa2022mean["wpa2022__avg"]) / wpa2022stddev["wpa2022__stddev"]
      zpitcher.zretwentyfour2022 = (zpitcher.retwentyfour2022 - retwentyfour2022mean["retwentyfour2022__avg"]) / retwentyfour2022stddev["retwentyfour2022__stddev"]
      zpitcher.zclutch2022 = (zpitcher.clutch2022 - clutch2022mean["clutch2022__avg"]) / clutch2022stddev["clutch2022__stddev"]
      zpitcher.zoutsidezoneswingpercent2022 = (zpitcher.outsidezoneswingpercent2022 - outsidezoneswingpercent2022mean["outsidezoneswingpercent2022__avg"]) / outsidezoneswingpercent2022stddev["outsidezoneswingpercent2022__stddev"]
      zpitcher.zfirstpitchstrikepercent2022 = (zpitcher.firstpitchstrikepercent2022 - firstpitchstrikepercent2022mean["firstpitchstrikepercent2022__avg"]) / firstpitchstrikepercent2022stddev["firstpitchstrikepercent2022__stddev"]
      zpitcher.zswingingstrikespercent2022 = (zpitcher.swingingstrikespercent2022 - swingingstrikespercent2022mean["swingingstrikespercent2022__avg"]) / swingingstrikespercent2022stddev["swingingstrikespercent2022__stddev"]
      if zpitcher.shutdowns2022 > 0:
        zpitcher.zshutdowns2022 = (zpitcher.shutdowns2022 - shutdowns2022mean["shutdowns2022__avg"]) / shutdowns2022stddev["shutdowns2022__stddev"]
      else:
        zpitcher.zshutdowns2022 = 0
      if zpitcher.meltdowns2022 > 0:
        zpitcher.zmeltdowns2022 = (zpitcher.meltdowns2022 - meltdowns2022mean["meltdowns2022__avg"]) / meltdowns2022stddev["meltdowns2022__stddev"]
      else:
        zpitcher.zmeltdowns2022 = 0
      zpitcher.zeraminus2022 = (zpitcher.eraminus2022 - eraminus2022mean["eraminus2022__avg"]) / eraminus2022stddev["eraminus2022__stddev"]
      zpitcher.zfipminus2022 = (zpitcher.fipminus2022 - fipminus2022mean["fipminus2022__avg"]) / fipminus2022stddev["fipminus2022__stddev"]
      zpitcher.zxfipminus2022 = (zpitcher.xfipminus2022 - xfipminus2022mean["xfipminus2022__avg"]) / xfipminus2022stddev["xfipminus2022__stddev"]
      #must invert z-score
      zpitcher.zbbpercent2022 = -(zpitcher.bbpercent2022 - bbpercent2022mean["bbpercent2022__avg"]) / bbpercent2022stddev["bbpercent2022__stddev"]
      zpitcher.zcswpercent2022 = (zpitcher.cswpercent2022 - cswpercent2022mean["cswpercent2022__avg"]) / cswpercent2022stddev["cswpercent2022__stddev"]
      zpitcher.zsoftpercent2022 = (zpitcher.softpercent2022 - softpercent2022mean["softpercent2022__avg"]) / softpercent2022stddev["softpercent2022__stddev"]
      zpitcher.zmediumpercent2022 = (zpitcher.mediumpercent2022 - mediumpercent2022mean["mediumpercent2022__avg"]) / mediumpercent2022stddev["mediumpercent2022__stddev"]
      zpitcher.zsoftplusmediumpercent2022 = (zpitcher.softplusmediumpercent2022 - softplusmediumpercent2022mean["softplusmediumpercent2022__avg"]) / softplusmediumpercent2022stddev["softplusmediumpercent2022__stddev"]
      #must invert z-score
      zpitcher.zrunsaverage2022 = -(zpitcher.runsaverage2022 - runsaverage2022mean["runsaverage2022__avg"]) / runsaverage2022stddev["runsaverage2022__stddev"]
      zpitcher.zsoftplusmediumpercent2022 = (zpitcher.softplusmediumpercent2022 - softplusmediumpercent2022mean["softplusmediumpercent2022__avg"]) / softplusmediumpercent2022stddev["softplusmediumpercent2022__stddev"]
      #must invert z-score
      zpitcher.zkwera2022 = -(zpitcher.kwera2022 - kwera2022mean["kwera2022__avg"]) / kwera2022stddev["kwera2022__stddev"]
      zpitcher.zkpercent2022 = (zpitcher.kpercent2022 - kpercent2022mean["kpercent2022__avg"]) / kpercent2022stddev["kpercent2022__stddev"]
      zpitcher.zweakpercent2022 = (zpitcher.weakpercent2022 - weakpercent2022mean["weakpercent2022__avg"]) / weakpercent2022stddev["weakpercent2022__stddev"]
      #must invert z-score
      zpitcher.zsiera2022 = -(zpitcher.siera2022 - siera2022mean["siera2022__avg"]) / siera2022stddev["siera2022__stddev"]
      zpitcher.zplus_k_per_nine2022 = (zpitcher.plus_k_per_nine2022 - plus_k_per_nine2022mean["plus_k_per_nine2022__avg"]) / plus_k_per_nine2022stddev["plus_k_per_nine2022__stddev"]
      #must invert z-score
      zpitcher.zplus_bb_per_nine2022 = -(zpitcher.plus_bb_per_nine2022 - plus_bb_per_nine2022mean["plus_bb_per_nine2022__avg"]) / plus_bb_per_nine2022stddev["plus_bb_per_nine2022__stddev"]
      zpitcher.zplus_k_per_bb2022 = (zpitcher.plus_k_per_bb2022 - plus_k_per_bb2022mean["plus_k_per_bb2022__avg"]) / plus_k_per_bb2022stddev["plus_k_per_bb2022__stddev"]
      #must invert z-score
      zpitcher.zplus_h_per_nine2022 = -(zpitcher.plus_h_per_nine2022 - plus_h_per_nine2022mean["plus_h_per_nine2022__avg"]) / plus_h_per_nine2022stddev["plus_h_per_nine2022__stddev"]
      #must invert z-score
      zpitcher.zplus_hr_per_nine2022 = -(zpitcher.plus_hr_per_nine2022 - plus_hr_per_nine2022mean["plus_hr_per_nine2022__avg"]) / plus_hr_per_nine2022stddev["plus_hr_per_nine2022__stddev"]
      #must invert z-score
      zpitcher.zplus_avg2022 = -(zpitcher.plus_avg2022 - plus_avg2022mean["plus_avg2022__avg"]) / plus_avg2022stddev["plus_avg2022__stddev"]
      #must invert z-score
      zpitcher.zplus_whip2022 = -(zpitcher.plus_whip2022 - plus_whip2022mean["plus_whip2022__avg"]) / plus_whip2022stddev["plus_whip2022__stddev"]
      #must invert z-score
      zpitcher.zplus_babip2022 = -(zpitcher.plus_babip2022 - plus_babip2022mean["plus_babip2022__avg"]) / plus_babip2022stddev["plus_babip2022__stddev"]
      zpitcher.zplus_lobpercent2022 = (zpitcher.plus_lobpercent2022 - plus_lobpercent2022mean["plus_lobpercent2022__avg"]) / plus_lobpercent2022stddev["plus_lobpercent2022__stddev"]
      zpitcher.zplus_kpercent2022 = (zpitcher.plus_kpercent2022 - plus_kpercent2022mean["plus_kpercent2022__avg"]) / plus_kpercent2022stddev["plus_kpercent2022__stddev"]
      #must invert z-score
      zpitcher.zplus_bbpercent2022 = -(zpitcher.plus_bbpercent2022 - plus_bbpercent2022mean["plus_bbpercent2022__avg"]) / plus_bbpercent2022stddev["plus_bbpercent2022__stddev"]
      #must invert z-score
      zpitcher.zplus_ldpercent2022 = -(zpitcher.plus_ldpercent2022 - plus_ldpercent2022mean["plus_ldpercent2022__avg"]) / plus_ldpercent2022stddev["plus_ldpercent2022__stddev"]
      zpitcher.zplus_gbpercent2022 = (zpitcher.plus_gbpercent2022 - plus_gbpercent2022mean["plus_gbpercent2022__avg"]) / plus_gbpercent2022stddev["plus_gbpercent2022__stddev"]
      #must invert z-score
      zpitcher.zplus_hrperfb2022 = -(zpitcher.plus_hrperfb2022 - plus_hrperfb2022mean["plus_hrperfb2022__avg"]) / plus_hrperfb2022stddev["plus_hrperfb2022__stddev"]
      zpitcher.zplus_softpercent2022 = (zpitcher.plus_softpercent2022 - plus_softpercent2022mean["plus_softpercent2022__avg"]) / plus_softpercent2022stddev["plus_softpercent2022__stddev"]
      zpitcher.zplus_mediumpercent2022 = (zpitcher.plus_mediumpercent2022 - plus_mediumpercent2022mean["plus_mediumpercent2022__avg"]) / plus_mediumpercent2022stddev["plus_mediumpercent2022__stddev"]
      #must invert z-score
      zpitcher.zbarrel_percent2022 = -(zpitcher.barrel_percent2022 - barrel_percent2022mean["barrel_percent2022__avg"]) / barrel_percent2022stddev["barrel_percent2022__stddev"]
      #must invert z-score
      zpitcher.zhardhitpercent2022 = -(zpitcher.hardhitpercent2022 - hardhitpercent2022mean["hardhitpercent2022__avg"]) / hardhitpercent2022stddev["hardhitpercent2022__stddev"]
      #must invert z-score
      zpitcher.zaverageev2022 = -(zpitcher.averageev2022 - averageev2022mean["averageev2022__avg"]) / averageev2022stddev["averageev2022__stddev"]
      zpitcher.zaveragela2022 = (zpitcher.averagela2022 - averagela2022mean["averagela2022__avg"]) / averagela2022stddev["averagela2022__stddev"]
      #must invert z-score
      zpitcher.zxera2022 = -(zpitcher.xera2022 - xera2022mean["xera2022__avg"]) / xera2022stddev["xera2022__stddev"]
      if zpitcher.loaded_bs_barrel_2022 == True:
        zpitcher.zbbevents2022 = (zpitcher.bbevents2022 - bbevents2022mean["bbevents2022__avg"]) / bbevents2022stddev["bbevents2022__stddev"]
        #zpitcher.zavghitangle2022 = (zpitcher.avghitangle2022 - avghitangle2022mean["avghitangle2022__avg"]) / avghitangle2022stddev["avghitangle2022__stddev"]
        #must invert z-score
        zpitcher.zanglesweetspotpercent2022 = -(zpitcher.anglesweetspotpercent2022 - anglesweetspotpercent2022mean["anglesweetspotpercent2022__avg"]) / anglesweetspotpercent2022stddev["anglesweetspotpercent2022__stddev"]
        #zpitcher.zanglehitspeed2022 = (zpitcher.anglehitspeed2022 - anglehitspeed2022mean["anglehitspeed2022__avg"]) / anglehitspeed2022stddev["anglehitspeed2022__stddev"]
        #zpitcher.zbsgbpercent2022 = (zpitcher.bsgbpercent2022 - bsgbpercent2022mean["bsgbpercent2022__avg"]) / bsgbpercent2022stddev["bsgbpercent2022__stddev"]
        #must invert z-score
        zpitcher.zavgdistance2022 = -(zpitcher.avgdistance2022 - avgdistance2022mean["avgdistance2022__avg"]) / avgdistance2022stddev["avgdistance2022__stddev"]
        zpitcher.zev95plus2022 = (zpitcher.ev95plus2022 - ev95plus2022mean["ev95plus2022__avg"]) / ev95plus2022stddev["ev95plus2022__stddev"]
        #zpitcher.zbrlpercent2022 = (zpitcher.brlpercent2022 - brlpercent2022mean["brlpercent2022__avg"]) / brlpercent2022stddev["brlpercent2022__stddev"]
        #must invert z-score
        zpitcher.zev95pluspercent2022 = -(zpitcher.ev95pluspercent2022 - ev95pluspercent2022mean["ev95pluspercent2022__avg"]) / ev95pluspercent2022stddev["ev95pluspercent2022__stddev"]
        #must invert z-score
        zpitcher.zbrlperpa2022 = -(zpitcher.brlperpa2022 - brlperpa2022mean["brlperpa2022__avg"]) / brlperpa2022stddev["brlperpa2022__stddev"]
      if zpitcher.loaded_bs_x_2022 == True:
        zpitcher.zbip2022 = (zpitcher.bip2022 - bip2022mean["bip2022__avg"]) / bip2022stddev["bip2022__stddev"]
        #must invert z-score
        zpitcher.zxavg2022 = -(zpitcher.xavg2022 - xavg2022mean["xavg2022__avg"]) / xavg2022stddev["xavg2022__stddev"]
        zpitcher.zxavgdiff2022 = (zpitcher.xavgdiff2022 - xavgdiff2022mean["xavgdiff2022__avg"]) / xavgdiff2022stddev["xavgdiff2022__stddev"]
        #must invert z-score
        zpitcher.zslg2022 = -(zpitcher.slg2022 - slg2022mean["slg2022__avg"]) / slg2022stddev["slg2022__stddev"]
        #must invert z-score
        zpitcher.zxslg2022 = -(zpitcher.xslg2022 - xslg2022mean["xslg2022__avg"]) / xslg2022stddev["xslg2022__stddev"]
        zpitcher.zxslgdiff2022 = (zpitcher.xslgdiff2022 - xslgdiff2022mean["xslgdiff2022__avg"]) / xslgdiff2022stddev["xslgdiff2022__stddev"]
        #must invert z-score
        zpitcher.zwoba2022 = -(zpitcher.woba2022 - woba2022mean["woba2022__avg"]) / woba2022stddev["woba2022__stddev"]
        #must invert z-score
        zpitcher.zxwoba2022 = -(zpitcher.xwoba2022 - xwoba2022mean["xwoba2022__avg"]) / xwoba2022stddev["xwoba2022__stddev"]
        zpitcher.zxwobadiff2022 = (zpitcher.xwobadiff2022 - xwobadiff2022mean["xwobadiff2022__avg"]) / xwobadiff2022stddev["xwobadiff2022__stddev"]
        #zpitcher.zbsera2022 = (zpitcher.bsera2022 - bsera2022mean["bsera2022__avg"]) / bsera2022stddev["bsera2022__stddev"]
        #zpitcher.zbsxera2022 = (zpitcher.bsxera2022 - bsxera2022mean["bsxera2022__avg"]) / bsxera2022stddev["bsxera2022__stddev"]
        zpitcher.zxeradiff2022 = (zpitcher.xeradiff2022 - xeradiff2022mean["xeradiff2022__avg"]) / xeradiff2022stddev["xeradiff2022__stddev"]
      zpitcher.save()
