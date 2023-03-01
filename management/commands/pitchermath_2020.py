import decimal
from django.core.management.base import BaseCommand
from app_bb.models import pitcher
from django.db.models.aggregates import StdDev, Avg

class Command(BaseCommand):
 def handle(self, *args, **options):
   if pitcher.objects.filter(lastname = "dummy").exists():
     pitcher.objects.filter(lastname = "dummy").delete()
   winningpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("winningpercent2020"))
   winningpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("winningpercent2020"))
   war2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("war2020"))
   war2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("war2020"))
   era2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("era2020"))
   era2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("era2020"))
   shutouts2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("shutouts2020"))
   shutouts2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("shutouts2020"))
   saves2020stddev = pitcher.objects.all().filter(loaded_2020 = True).exclude(saves2020 = 0).aggregate(StdDev("saves2020"))
   saves2020mean = pitcher.objects.all().filter(loaded_2020 = True).exclude(saves2020 = 0).aggregate(Avg("saves2020"))
   savepercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).exclude(saves2020 = 0).aggregate(StdDev("savepercent2020"))
   savepercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).exclude(saves2020 = 0).aggregate(Avg("savepercent2020"))
   innings2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("innings2020"))
   innings2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("innings2020"))
   battersfaced2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("battersfaced2020"))
   battersfaced2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("battersfaced2020"))
   hits2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hits2020"))
   hits2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("hits2020"))
   runs2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("runs2020"))
   runs2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("runs2020"))
   # runsaverage2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("runsaverage2020"))
   # runsaverage2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("runsaverage2020"))
   homeruns2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("homeruns2020"))
   homeruns2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("homeruns2020"))
   bbhbp2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bbhbp2020"))
   bbhbp2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("bbhbp2020"))
   k2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("k2020"))
   k2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("k2020"))
   thrownforkpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("thrownforkpercent2020"))
   thrownforkpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("thrownforkpercent2020"))
   kpernine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("kpernine2020"))
   kpernine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("kpernine2020"))
   bbpernine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bbpernine2020"))
   bbpernine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("bbpernine2020"))
   hitpernine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hitpernine2020"))
   hitpernine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("hitpernine2020"))
   hrpernine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hrpernine2020"))
   hrpernine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("hrpernine2020"))
   kperbb2020stddev = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_2020 = True).aggregate(StdDev("kperbb2020"))
   kperbb2020mean = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_2020 = True).aggregate(Avg("kperbb2020"))
   avg2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("avg2020"))
   avg2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("avg2020"))
   whip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("whip2020"))
   whip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("whip2020"))
   babip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("babip2020"))
   babip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("babip2020"))
   lobpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("lobpercent2020"))
   lobpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("lobpercent2020"))
   hrperfb2020stddev = pitcher.objects.all().filter(loaded_hrperfb2020 = True).filter(loaded_2020 = True).aggregate(StdDev("hrperfb2020"))
   hrperfb2020mean = pitcher.objects.all().filter(loaded_hrperfb2020 = True).filter(loaded_2020 = True).aggregate(Avg("hrperfb2020"))
   fip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fip2020"))
   fip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("fip2020"))
   gbperfb2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("gbperfb2020"))
   gbperfb2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("gbperfb2020"))
   gbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("gbpercent2020"))
   gbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("gbpercent2020"))
   iffbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("iffbpercent2020"))
   iffbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("iffbpercent2020"))
   ldpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("ldpercent2020"))
   ldpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("ldpercent2020"))
   fbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fbpercent2020"))
   fbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("fbpercent2020"))
   rar2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("rar2020"))
   rar2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("rar2020"))
   tera2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("tera2020"))
   tera2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("tera2020"))
   xfip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xfip2020"))
   xfip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("xfip2020"))
   wpa2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("wpa2020"))
   wpa2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("wpa2020"))
   retwentyfour2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("retwentyfour2020"))
   retwentyfour2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("retwentyfour2020"))
   clutch2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("clutch2020"))
   clutch2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("clutch2020"))
   outsidezoneswingpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("outsidezoneswingpercent2020"))
   outsidezoneswingpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("outsidezoneswingpercent2020"))
   firstpitchstrikepercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("firstpitchstrikepercent2020"))
   firstpitchstrikepercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("firstpitchstrikepercent2020"))
   swingingstrikespercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("swingingstrikespercent2020"))
   swingingstrikespercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("swingingstrikespercent2020"))
   shutdowns2020stddev = pitcher.objects.all().filter(loaded_2020 = True).exclude(shutdowns2020 = 0).aggregate(StdDev("shutdowns2020"))
   shutdowns2020mean = pitcher.objects.all().filter(loaded_2020 = True).exclude(shutdowns2020 = 0).aggregate(Avg("shutdowns2020"))
   meltdowns2020stddev = pitcher.objects.all().filter(loaded_2020 = True).exclude(meltdowns2020 = 0).aggregate(StdDev("meltdowns2020"))
   meltdowns2020mean = pitcher.objects.all().filter(loaded_2020 = True).exclude(meltdowns2020 = 0).aggregate(Avg("meltdowns2020"))
   eraminus2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("eraminus2020"))
   eraminus2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("eraminus2020"))
   fipminus2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("fipminus2020"))
   fipminus2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("fipminus2020"))
   xfipminus2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xfipminus2020"))
   xfipminus2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("xfipminus2020"))
   bbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("bbpercent2020"))
   bbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("bbpercent2020"))
   cswpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("cswpercent2020"))
   cswpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("cswpercent2020"))
   softpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("softpercent2020"))
   softpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("softpercent2020"))
   mediumpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("mediumpercent2020"))
   mediumpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("mediumpercent2020"))
   softplusmediumpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("softplusmediumpercent2020"))
   softplusmediumpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("softplusmediumpercent2020"))
   runsaverage2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("runsaverage2020"))
   runsaverage2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("runsaverage2020"))
   softplusmediumpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("softplusmediumpercent2020"))
   softplusmediumpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("softplusmediumpercent2020"))
   kwera2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("kwera2020"))
   kwera2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("kwera2020"))
   kpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("kpercent2020"))
   kpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("kpercent2020"))
   weakpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("weakpercent2020"))
   weakpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("weakpercent2020"))
   siera2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("siera2020"))
   siera2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("siera2020"))
   plus_k_per_nine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_k_per_nine2020"))
   plus_k_per_nine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_k_per_nine2020"))
   plus_bb_per_nine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_bb_per_nine2020"))
   plus_bb_per_nine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_bb_per_nine2020"))
   plus_k_per_bb2020stddev = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_2020 = True).aggregate(StdDev("plus_k_per_bb2020"))
   plus_k_per_bb2020mean = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_2020 = True).aggregate(Avg("plus_k_per_bb2020"))
   plus_h_per_nine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_h_per_nine2020"))
   plus_h_per_nine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_h_per_nine2020"))
   plus_hr_per_nine2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_hr_per_nine2020"))
   plus_hr_per_nine2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_hr_per_nine2020"))
   plus_avg2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_avg2020"))
   plus_avg2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_avg2020"))
   plus_whip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_whip2020"))
   plus_whip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_whip2020"))
   plus_babip2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_babip2020"))
   plus_babip2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_babip2020"))
   plus_lobpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_lobpercent2020"))
   plus_lobpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_lobpercent2020"))
   plus_kpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_kpercent2020"))
   plus_kpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_kpercent2020"))
   plus_bbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_bbpercent2020"))
   plus_bbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_bbpercent2020"))
   plus_ldpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_ldpercent2020"))
   plus_ldpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_ldpercent2020"))
   plus_gbpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_gbpercent2020"))
   plus_gbpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_gbpercent2020"))
   plus_hrperfb2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_hrperfb2020"))
   plus_hrperfb2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_hrperfb2020"))
   plus_softpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_softpercent2020"))
   plus_softpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_softpercent2020"))
   plus_mediumpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("plus_mediumpercent2020"))
   plus_mediumpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("plus_mediumpercent2020"))
   barrel_percent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("barrel_percent2020"))
   barrel_percent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("barrel_percent2020"))
   hardhitpercent2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("hardhitpercent2020"))
   hardhitpercent2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("hardhitpercent2020"))
   averageev2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("averageev2020"))
   averageev2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("averageev2020"))
   averagela2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("averagela2020"))
   averagela2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("averagela2020"))
   xera2020stddev = pitcher.objects.all().filter(loaded_2020 = True).aggregate(StdDev("xera2020"))
   xera2020mean = pitcher.objects.all().filter(loaded_2020 = True).aggregate(Avg("xera2020"))
 
   #baseball savant barrel 2020
   bbevents2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("bbevents2020"))
   bbevents2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("bbevents2020"))
   #avghitangle2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("avghitangle2020"))
   #avghitangle2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("avghitangle2020"))
   anglesweetspotpercent2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("anglesweetspotpercent2020"))
   anglesweetspotpercent2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("anglesweetspotpercent2020"))
   #anglehitspeed2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("anglehitspeed2020"))
   #anglehitspeed2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("anglehitspeed2020"))
   #bsgbpercent2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("bsgbpercent2020"))
   #bsgbpercent2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("bsgbpercent2020"))
   avgdistance2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("avgdistance2020"))
   avgdistance2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("avgdistance2020"))
   ev95plus2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("ev95plus2020"))
   ev95plus2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("ev95plus2020"))
   #brlpercent2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("brlpercent2020"))
   #brlpercent2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("brlpercent2020"))
   ev95pluspercent2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("ev95pluspercent2020"))
   ev95pluspercent2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("ev95pluspercent2020"))
   brlperpa2020stddev = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(StdDev("brlperpa2020"))
   brlperpa2020mean = pitcher.objects.all().filter(loaded_bs_barrel_2020 = True).aggregate(Avg("brlperpa2020"))
 
   #baseball savant expected 2020
   bip2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("bip2020"))
   bip2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("bip2020"))
   xavg2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xavg2020"))
   xavg2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xavg2020"))
   xavgdiff2020stddev = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_bs_x_2020 = True).aggregate(StdDev("xavgdiff2020"))
   xavgdiff2020mean = pitcher.objects.all().filter(loaded_k_per_bb2020 = True).filter(loaded_bs_x_2020 = True).aggregate(Avg("xavgdiff2020"))
   slg2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("slg2020"))
   slg2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("slg2020"))
   xslg2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xslg2020"))
   xslg2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xslg2020"))
   xslgdiff2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xslgdiff2020"))
   xslgdiff2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xslgdiff2020"))
   woba2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("woba2020"))
   woba2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("woba2020"))
   xwoba2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xwoba2020"))
   xwoba2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xwoba2020"))
   xwobadiff2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xwobadiff2020"))
   xwobadiff2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xwobadiff2020"))
   #2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("bsera2020"))
   #bsera2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("bsera2020"))
   #bsxera2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("bsxera2020"))
   #bsxera2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("bsxera2020"))
   xeradiff2020stddev = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(StdDev("xeradiff2020"))
   xeradiff2020mean = pitcher.objects.all().filter(loaded_bs_x_2020 = True).aggregate(Avg("xeradiff2020"))
 
 
   for zpitcher in pitcher.objects.all().filter(loaded_2020 = True):
     zpitcher.zwinningpercent2020 = (zpitcher.winningpercent2020 - winningpercent2020mean["winningpercent2020__avg"]) / winningpercent2020stddev["winningpercent2020__stddev"]
     zpitcher.zwar2020 = (zpitcher.war2020 - war2020mean["war2020__avg"]) / war2020stddev["war2020__stddev"]
     #must invert z-score
     zpitcher.zera2020 = -(zpitcher.era2020 - era2020mean["era2020__avg"]) / era2020stddev["era2020__stddev"]
     zpitcher.zshutouts2020 = (zpitcher.shutouts2020 - shutouts2020mean["shutouts2020__avg"]) / shutouts2020stddev["shutouts2020__stddev"]
     if zpitcher.saves2020 > 1:
       zpitcher.zsaves2020 = (zpitcher.saves2020 - saves2020mean["saves2020__avg"]) / saves2020stddev["saves2020__stddev"]
       zpitcher.zsavepercent2020 = (zpitcher.savepercent2020 - savepercent2020mean["savepercent2020__avg"]) / savepercent2020stddev["savepercent2020__stddev"]
     else:
       zpitcher.zsaves2020 = 0
       zpitcher.zsavepercent2020 = 0
     zpitcher.zinnings2020 = (zpitcher.innings2020 - innings2020mean["innings2020__avg"]) / innings2020stddev["innings2020__stddev"]
     zpitcher.zbattersfaced2020 = (zpitcher.battersfaced2020 - battersfaced2020mean["battersfaced2020__avg"]) / battersfaced2020stddev["battersfaced2020__stddev"]
     zpitcher.zhits2020 = (zpitcher.hits2020 - hits2020mean["hits2020__avg"]) / hits2020stddev["hits2020__stddev"]
     zpitcher.zruns2020 = (zpitcher.runs2020 - runs2020mean["runs2020__avg"]) / runs2020stddev["runs2020__stddev"]
     # #must invert z-score
     # zpitcher.zrunsaverage2020 = -(zpitcher.runsaverage2020 - runsaverage2020mean["runsaverage2020__avg"]) / runsaverage2020stddev["runsaverage2020__stddev"]
     zpitcher.zhomeruns2020 = (zpitcher.homeruns2020 - homeruns2020mean["homeruns2020__avg"]) / homeruns2020stddev["homeruns2020__stddev"]
     zpitcher.zbbhbp2020 = (zpitcher.bbhbp2020 - bbhbp2020mean["bbhbp2020__avg"]) / bbhbp2020stddev["bbhbp2020__stddev"]
     zpitcher.zk2020 = (zpitcher.k2020 - k2020mean["k2020__avg"]) / k2020stddev["k2020__stddev"]
     zpitcher.zthrownforkpercent2020 = (zpitcher.thrownforkpercent2020 - thrownforkpercent2020mean["thrownforkpercent2020__avg"]) / thrownforkpercent2020stddev["thrownforkpercent2020__stddev"]
     zpitcher.zkpernine2020 = (zpitcher.kpernine2020 - kpernine2020mean["kpernine2020__avg"]) / kpernine2020stddev["kpernine2020__stddev"]
     #must invert z-score
     zpitcher.zbbpernine2020 = -(zpitcher.bbpernine2020 - bbpernine2020mean["bbpernine2020__avg"]) / bbpernine2020stddev["bbpernine2020__stddev"]
     #must invert z-score
     zpitcher.zhitpernine2020 = -(zpitcher.hitpernine2020 - hitpernine2020mean["hitpernine2020__avg"]) / hitpernine2020stddev["hitpernine2020__stddev"]
     #must invert z-score
     zpitcher.zhrpernine2020 = -(zpitcher.hrpernine2020 - hrpernine2020mean["hrpernine2020__avg"]) / hrpernine2020stddev["hrpernine2020__stddev"]
     zpitcher.zkperbb2020 = (zpitcher.kperbb2020 - kperbb2020mean["kperbb2020__avg"]) / kperbb2020stddev["kperbb2020__stddev"]
     #must invert z-score
     zpitcher.zavg2020 = -(zpitcher.avg2020 - avg2020mean["avg2020__avg"]) / avg2020stddev["avg2020__stddev"]
     #must invert z-score
     zpitcher.zwhip2020 = -(zpitcher.whip2020 - whip2020mean["whip2020__avg"]) / whip2020stddev["whip2020__stddev"]
     #must invert z-score
     zpitcher.zbabip2020 = -(zpitcher.babip2020 - babip2020mean["babip2020__avg"]) / babip2020stddev["babip2020__stddev"]
     #must invert z-score
     zpitcher.zhrperfb2020 = -(zpitcher.hrperfb2020 - hrperfb2020mean["hrperfb2020__avg"]) / hrperfb2020stddev["hrperfb2020__stddev"]
     #must invert z-score
     zpitcher.zfip2020 = -(zpitcher.fip2020 - fip2020mean["fip2020__avg"]) / fip2020stddev["fip2020__stddev"]
     zpitcher.zgbperfb2020 = (zpitcher.gbperfb2020 - gbperfb2020mean["gbperfb2020__avg"]) / gbperfb2020stddev["gbperfb2020__stddev"]
     zpitcher.zgbpercent2020 = (zpitcher.gbpercent2020 - gbpercent2020mean["gbpercent2020__avg"]) / gbpercent2020stddev["gbpercent2020__stddev"]
     zpitcher.ziffbpercent2020 = (zpitcher.iffbpercent2020 - iffbpercent2020mean["iffbpercent2020__avg"]) / iffbpercent2020stddev["iffbpercent2020__stddev"]
     #must invert z-score
     zpitcher.zldpercent2020 = -(zpitcher.ldpercent2020 - ldpercent2020mean["ldpercent2020__avg"]) / ldpercent2020stddev["ldpercent2020__stddev"]
     #must invert z-score
     zpitcher.zfbpercent2020 = -(zpitcher.fbpercent2020 - fbpercent2020mean["fbpercent2020__avg"]) / fbpercent2020stddev["fbpercent2020__stddev"]
     zpitcher.zrar2020 = (zpitcher.rar2020 - rar2020mean["rar2020__avg"]) / rar2020stddev["rar2020__stddev"]
     #must invert z-score
     zpitcher.ztera2020 = -(zpitcher.tera2020 - tera2020mean["tera2020__avg"]) / tera2020stddev["tera2020__stddev"]
     #must invert z-score
     zpitcher.zxfip2020 = -(zpitcher.xfip2020 - xfip2020mean["xfip2020__avg"]) / xfip2020stddev["xfip2020__stddev"]
     zpitcher.zwpa2020 = (zpitcher.wpa2020 - wpa2020mean["wpa2020__avg"]) / wpa2020stddev["wpa2020__stddev"]
     zpitcher.zretwentyfour2020 = (zpitcher.retwentyfour2020 - retwentyfour2020mean["retwentyfour2020__avg"]) / retwentyfour2020stddev["retwentyfour2020__stddev"]
     zpitcher.zclutch2020 = (zpitcher.clutch2020 - clutch2020mean["clutch2020__avg"]) / clutch2020stddev["clutch2020__stddev"]
     zpitcher.zoutsidezoneswingpercent2020 = (zpitcher.outsidezoneswingpercent2020 - outsidezoneswingpercent2020mean["outsidezoneswingpercent2020__avg"]) / outsidezoneswingpercent2020stddev["outsidezoneswingpercent2020__stddev"]
     zpitcher.zfirstpitchstrikepercent2020 = (zpitcher.firstpitchstrikepercent2020 - firstpitchstrikepercent2020mean["firstpitchstrikepercent2020__avg"]) / firstpitchstrikepercent2020stddev["firstpitchstrikepercent2020__stddev"]
     zpitcher.zswingingstrikespercent2020 = (zpitcher.swingingstrikespercent2020 - swingingstrikespercent2020mean["swingingstrikespercent2020__avg"]) / swingingstrikespercent2020stddev["swingingstrikespercent2020__stddev"]
     #below code temporarily removed due to sudden decimal error
    #  if zpitcher.shutdowns2020 > 0:
    #    zpitcher.zshutdowns2020 = (zpitcher.shutdowns2020 - shutdowns2020mean["shutdowns2020__avg"]) / shutdowns2020stddev["shutdowns2020__stddev"]
    #  else:
    #    zpitcher.zshutdowns2020 = 0
    #  if zpitcher.meltdowns2020 > 0:
    #    zpitcher.zmeltdowns2020 = (zpitcher.meltdowns2020 - meltdowns2020mean["meltdowns2020__avg"]) / meltdowns2020stddev["meltdowns2020__stddev"]
    #  else:
    #    zpitcher.zmeltdowns2020 = 0
     zpitcher.zeraminus2020 = (zpitcher.eraminus2020 - eraminus2020mean["eraminus2020__avg"]) / eraminus2020stddev["eraminus2020__stddev"]
     zpitcher.zfipminus2020 = (zpitcher.fipminus2020 - fipminus2020mean["fipminus2020__avg"]) / fipminus2020stddev["fipminus2020__stddev"]
     zpitcher.zxfipminus2020 = (zpitcher.xfipminus2020 - xfipminus2020mean["xfipminus2020__avg"]) / xfipminus2020stddev["xfipminus2020__stddev"]
     #must invert z-score
     zpitcher.zbbpercent2020 = -(zpitcher.bbpercent2020 - bbpercent2020mean["bbpercent2020__avg"]) / bbpercent2020stddev["bbpercent2020__stddev"]
     zpitcher.zcswpercent2020 = (zpitcher.cswpercent2020 - cswpercent2020mean["cswpercent2020__avg"]) / cswpercent2020stddev["cswpercent2020__stddev"]
     zpitcher.zsoftpercent2020 = (zpitcher.softpercent2020 - softpercent2020mean["softpercent2020__avg"]) / softpercent2020stddev["softpercent2020__stddev"]
     zpitcher.zmediumpercent2020 = (zpitcher.mediumpercent2020 - mediumpercent2020mean["mediumpercent2020__avg"]) / mediumpercent2020stddev["mediumpercent2020__stddev"]
     zpitcher.zsoftplusmediumpercent2020 = (zpitcher.softplusmediumpercent2020 - softplusmediumpercent2020mean["softplusmediumpercent2020__avg"]) / softplusmediumpercent2020stddev["softplusmediumpercent2020__stddev"]
     #must invert z-score
     zpitcher.zrunsaverage2020 = -(zpitcher.runsaverage2020 - runsaverage2020mean["runsaverage2020__avg"]) / runsaverage2020stddev["runsaverage2020__stddev"]
     zpitcher.zsoftplusmediumpercent2020 = (zpitcher.softplusmediumpercent2020 - softplusmediumpercent2020mean["softplusmediumpercent2020__avg"]) / softplusmediumpercent2020stddev["softplusmediumpercent2020__stddev"]
     #must invert z-score
     zpitcher.zkwera2020 = -(zpitcher.kwera2020 - kwera2020mean["kwera2020__avg"]) / kwera2020stddev["kwera2020__stddev"]
     zpitcher.zkpercent2020 = (zpitcher.kpercent2020 - kpercent2020mean["kpercent2020__avg"]) / kpercent2020stddev["kpercent2020__stddev"]
     zpitcher.zweakpercent2020 = (zpitcher.weakpercent2020 - weakpercent2020mean["weakpercent2020__avg"]) / weakpercent2020stddev["weakpercent2020__stddev"]
     #must invert z-score
     zpitcher.zsiera2020 = -(zpitcher.siera2020 - siera2020mean["siera2020__avg"]) / siera2020stddev["siera2020__stddev"]
     zpitcher.zplus_k_per_nine2020 = (zpitcher.plus_k_per_nine2020 - plus_k_per_nine2020mean["plus_k_per_nine2020__avg"]) / plus_k_per_nine2020stddev["plus_k_per_nine2020__stddev"]
     #must invert z-score
     zpitcher.zplus_bb_per_nine2020 = -(zpitcher.plus_bb_per_nine2020 - plus_bb_per_nine2020mean["plus_bb_per_nine2020__avg"]) / plus_bb_per_nine2020stddev["plus_bb_per_nine2020__stddev"]
     zpitcher.zplus_k_per_bb2020 = (zpitcher.plus_k_per_bb2020 - plus_k_per_bb2020mean["plus_k_per_bb2020__avg"]) / plus_k_per_bb2020stddev["plus_k_per_bb2020__stddev"]
     #must invert z-score
     zpitcher.zplus_h_per_nine2020 = -(zpitcher.plus_h_per_nine2020 - plus_h_per_nine2020mean["plus_h_per_nine2020__avg"]) / plus_h_per_nine2020stddev["plus_h_per_nine2020__stddev"]
     #must invert z-score
     zpitcher.zplus_hr_per_nine2020 = -(zpitcher.plus_hr_per_nine2020 - plus_hr_per_nine2020mean["plus_hr_per_nine2020__avg"]) / plus_hr_per_nine2020stddev["plus_hr_per_nine2020__stddev"]
     #must invert z-score
     zpitcher.zplus_avg2020 = -(zpitcher.plus_avg2020 - plus_avg2020mean["plus_avg2020__avg"]) / plus_avg2020stddev["plus_avg2020__stddev"]
     #must invert z-score
     zpitcher.zplus_whip2020 = -(zpitcher.plus_whip2020 - plus_whip2020mean["plus_whip2020__avg"]) / plus_whip2020stddev["plus_whip2020__stddev"]
     #must invert z-score
     zpitcher.zplus_babip2020 = -(zpitcher.plus_babip2020 - plus_babip2020mean["plus_babip2020__avg"]) / plus_babip2020stddev["plus_babip2020__stddev"]
     zpitcher.zplus_lobpercent2020 = (zpitcher.plus_lobpercent2020 - plus_lobpercent2020mean["plus_lobpercent2020__avg"]) / plus_lobpercent2020stddev["plus_lobpercent2020__stddev"]
     zpitcher.zplus_kpercent2020 = (zpitcher.plus_kpercent2020 - plus_kpercent2020mean["plus_kpercent2020__avg"]) / plus_kpercent2020stddev["plus_kpercent2020__stddev"]
     #must invert z-score
     zpitcher.zplus_bbpercent2020 = -(zpitcher.plus_bbpercent2020 - plus_bbpercent2020mean["plus_bbpercent2020__avg"]) / plus_bbpercent2020stddev["plus_bbpercent2020__stddev"]
     #must invert z-score
     zpitcher.zplus_ldpercent2020 = -(zpitcher.plus_ldpercent2020 - plus_ldpercent2020mean["plus_ldpercent2020__avg"]) / plus_ldpercent2020stddev["plus_ldpercent2020__stddev"]
     zpitcher.zplus_gbpercent2020 = (zpitcher.plus_gbpercent2020 - plus_gbpercent2020mean["plus_gbpercent2020__avg"]) / plus_gbpercent2020stddev["plus_gbpercent2020__stddev"]
     #must invert z-score
     zpitcher.zplus_hrperfb2020 = -(zpitcher.plus_hrperfb2020 - plus_hrperfb2020mean["plus_hrperfb2020__avg"]) / plus_hrperfb2020stddev["plus_hrperfb2020__stddev"]
     zpitcher.zplus_softpercent2020 = (zpitcher.plus_softpercent2020 - plus_softpercent2020mean["plus_softpercent2020__avg"]) / plus_softpercent2020stddev["plus_softpercent2020__stddev"]
     zpitcher.zplus_mediumpercent2020 = (zpitcher.plus_mediumpercent2020 - plus_mediumpercent2020mean["plus_mediumpercent2020__avg"]) / plus_mediumpercent2020stddev["plus_mediumpercent2020__stddev"]
     #must invert z-score
     zpitcher.zbarrel_percent2020 = -(zpitcher.barrel_percent2020 - barrel_percent2020mean["barrel_percent2020__avg"]) / barrel_percent2020stddev["barrel_percent2020__stddev"]
     #must invert z-score
     zpitcher.zhardhitpercent2020 = -(zpitcher.hardhitpercent2020 - hardhitpercent2020mean["hardhitpercent2020__avg"]) / hardhitpercent2020stddev["hardhitpercent2020__stddev"]
     #must invert z-score
     zpitcher.zaverageev2020 = -(zpitcher.averageev2020 - averageev2020mean["averageev2020__avg"]) / averageev2020stddev["averageev2020__stddev"]
     zpitcher.zaveragela2020 = (zpitcher.averagela2020 - averagela2020mean["averagela2020__avg"]) / averagela2020stddev["averagela2020__stddev"]
     #must invert z-score
     zpitcher.zxera2020 = -(zpitcher.xera2020 - xera2020mean["xera2020__avg"]) / xera2020stddev["xera2020__stddev"]
     if zpitcher.loaded_bs_barrel_2020 == True:
       zpitcher.zbbevents2020 = (zpitcher.bbevents2020 - bbevents2020mean["bbevents2020__avg"]) / bbevents2020stddev["bbevents2020__stddev"]
       #zpitcher.zavghitangle2020 = (zpitcher.avghitangle2020 - avghitangle2020mean["avghitangle2020__avg"]) / avghitangle2020stddev["avghitangle2020__stddev"]
       #must invert z-score
       zpitcher.zanglesweetspotpercent2020 = -(zpitcher.anglesweetspotpercent2020 - anglesweetspotpercent2020mean["anglesweetspotpercent2020__avg"]) / anglesweetspotpercent2020stddev["anglesweetspotpercent2020__stddev"]
       #zpitcher.zanglehitspeed2020 = (zpitcher.anglehitspeed2020 - anglehitspeed2020mean["anglehitspeed2020__avg"]) / anglehitspeed2020stddev["anglehitspeed2020__stddev"]
       #zpitcher.zbsgbpercent2020 = (zpitcher.bsgbpercent2020 - bsgbpercent2020mean["bsgbpercent2020__avg"]) / bsgbpercent2020stddev["bsgbpercent2020__stddev"]
       #must invert z-score
       zpitcher.zavgdistance2020 = -(zpitcher.avgdistance2020 - avgdistance2020mean["avgdistance2020__avg"]) / avgdistance2020stddev["avgdistance2020__stddev"]
       zpitcher.zev95plus2020 = (zpitcher.ev95plus2020 - ev95plus2020mean["ev95plus2020__avg"]) / ev95plus2020stddev["ev95plus2020__stddev"]
       #zpitcher.zbrlpercent2020 = (zpitcher.brlpercent2020 - brlpercent2020mean["brlpercent2020__avg"]) / brlpercent2020stddev["brlpercent2020__stddev"]
       #must invert z-score
       zpitcher.zev95pluspercent2020 = -(zpitcher.ev95pluspercent2020 - ev95pluspercent2020mean["ev95pluspercent2020__avg"]) / ev95pluspercent2020stddev["ev95pluspercent2020__stddev"]
       #must invert z-score
       zpitcher.zbrlperpa2020 = -(zpitcher.brlperpa2020 - brlperpa2020mean["brlperpa2020__avg"]) / brlperpa2020stddev["brlperpa2020__stddev"]
     if zpitcher.loaded_bs_x_2020 == True:
       zpitcher.zbip2020 = (zpitcher.bip2020 - bip2020mean["bip2020__avg"]) / bip2020stddev["bip2020__stddev"]
       #must invert z-score
       zpitcher.zxavg2020 = -(zpitcher.xavg2020 - xavg2020mean["xavg2020__avg"]) / xavg2020stddev["xavg2020__stddev"]
       zpitcher.zxavgdiff2020 = (zpitcher.xavgdiff2020 - xavgdiff2020mean["xavgdiff2020__avg"]) / xavgdiff2020stddev["xavgdiff2020__stddev"]
       #must invert z-score
       zpitcher.zslg2020 = -(zpitcher.slg2020 - slg2020mean["slg2020__avg"]) / slg2020stddev["slg2020__stddev"]
       #must invert z-score
       zpitcher.zxslg2020 = -(zpitcher.xslg2020 - xslg2020mean["xslg2020__avg"]) / xslg2020stddev["xslg2020__stddev"]
       zpitcher.zxslgdiff2020 = (zpitcher.xslgdiff2020 - xslgdiff2020mean["xslgdiff2020__avg"]) / xslgdiff2020stddev["xslgdiff2020__stddev"]
       #must invert z-score
       zpitcher.zwoba2020 = -(zpitcher.woba2020 - woba2020mean["woba2020__avg"]) / woba2020stddev["woba2020__stddev"]
       #must invert z-score
       zpitcher.zxwoba2020 = -(zpitcher.xwoba2020 - xwoba2020mean["xwoba2020__avg"]) / xwoba2020stddev["xwoba2020__stddev"]
       zpitcher.zxwobadiff2020 = (zpitcher.xwobadiff2020 - xwobadiff2020mean["xwobadiff2020__avg"]) / xwobadiff2020stddev["xwobadiff2020__stddev"]
       #zpitcher.zbsera2020 = (zpitcher.bsera2020 - bsera2020mean["bsera2020__avg"]) / bsera2020stddev["bsera2020__stddev"]
       #zpitcher.zbsxera2020 = (zpitcher.bsxera2020 - bsxera2020mean["bsxera2020__avg"]) / bsxera2020stddev["bsxera2020__stddev"]
       zpitcher.zxeradiff2020 = (zpitcher.xeradiff2020 - xeradiff2020mean["xeradiff2020__avg"]) / xeradiff2020stddev["xeradiff2020__stddev"]
     zpitcher.save()