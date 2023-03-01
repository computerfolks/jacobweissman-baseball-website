import decimal
from django.core.management.base import BaseCommand
from app_bb.models import pitcher
from django.db.models.aggregates import StdDev, Avg

class Command(BaseCommand):
 def handle(self, *args, **options):
   if pitcher.objects.filter(lastname = "dummy").exists():
     pitcher.objects.filter(lastname = "dummy").delete()
   winningpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("winningpercent2021"))
   winningpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("winningpercent2021"))
   war2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("war2021"))
   war2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("war2021"))
   era2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("era2021"))
   era2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("era2021"))
   shutouts2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("shutouts2021"))
   shutouts2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("shutouts2021"))
   saves2021stddev = pitcher.objects.all().filter(loaded_2021 = True).exclude(saves2021 = 0).aggregate(StdDev("saves2021"))
   saves2021mean = pitcher.objects.all().filter(loaded_2021 = True).exclude(saves2021 = 0).aggregate(Avg("saves2021"))
   savepercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).exclude(saves2021 = 0).aggregate(StdDev("savepercent2021"))
   savepercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).exclude(saves2021 = 0).aggregate(Avg("savepercent2021"))
   innings2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("innings2021"))
   innings2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("innings2021"))
   battersfaced2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("battersfaced2021"))
   battersfaced2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("battersfaced2021"))
   hits2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hits2021"))
   hits2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("hits2021"))
   runs2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("runs2021"))
   runs2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("runs2021"))
   # runsaverage2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("runsaverage2021"))
   # runsaverage2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("runsaverage2021"))
   homeruns2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("homeruns2021"))
   homeruns2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("homeruns2021"))
   bbhbp2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bbhbp2021"))
   bbhbp2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("bbhbp2021"))
   k2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("k2021"))
   k2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("k2021"))
   thrownforkpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("thrownforkpercent2021"))
   thrownforkpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("thrownforkpercent2021"))
   kpernine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("kpernine2021"))
   kpernine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("kpernine2021"))
   bbpernine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bbpernine2021"))
   bbpernine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("bbpernine2021"))
   hitpernine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hitpernine2021"))
   hitpernine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("hitpernine2021"))
   hrpernine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hrpernine2021"))
   hrpernine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("hrpernine2021"))
   kperbb2021stddev = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_2021 = True).aggregate(StdDev("kperbb2021"))
   kperbb2021mean = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_2021 = True).aggregate(Avg("kperbb2021"))
   avg2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("avg2021"))
   avg2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("avg2021"))
   whip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("whip2021"))
   whip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("whip2021"))
   babip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("babip2021"))
   babip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("babip2021"))
   lobpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("lobpercent2021"))
   lobpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("lobpercent2021"))
   hrperfb2021stddev = pitcher.objects.all().filter(loaded_hrperfb2021 = True).filter(loaded_2021 = True).aggregate(StdDev("hrperfb2021"))
   hrperfb2021mean = pitcher.objects.all().filter(loaded_hrperfb2021 = True).filter(loaded_2021 = True).aggregate(Avg("hrperfb2021"))
   fip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fip2021"))
   fip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("fip2021"))
   gbperfb2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("gbperfb2021"))
   gbperfb2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("gbperfb2021"))
   gbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("gbpercent2021"))
   gbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("gbpercent2021"))
   iffbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("iffbpercent2021"))
   iffbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("iffbpercent2021"))
   ldpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("ldpercent2021"))
   ldpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("ldpercent2021"))
   fbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fbpercent2021"))
   fbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("fbpercent2021"))
   rar2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("rar2021"))
   rar2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("rar2021"))
   tera2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("tera2021"))
   tera2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("tera2021"))
   xfip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xfip2021"))
   xfip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("xfip2021"))
   wpa2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("wpa2021"))
   wpa2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("wpa2021"))
   retwentyfour2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("retwentyfour2021"))
   retwentyfour2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("retwentyfour2021"))
   clutch2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("clutch2021"))
   clutch2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("clutch2021"))
   outsidezoneswingpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("outsidezoneswingpercent2021"))
   outsidezoneswingpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("outsidezoneswingpercent2021"))
   firstpitchstrikepercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("firstpitchstrikepercent2021"))
   firstpitchstrikepercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("firstpitchstrikepercent2021"))
   swingingstrikespercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("swingingstrikespercent2021"))
   swingingstrikespercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("swingingstrikespercent2021"))
   shutdowns2021stddev = pitcher.objects.all().filter(loaded_2021 = True).exclude(shutdowns2021 = 0).aggregate(StdDev("shutdowns2021"))
   shutdowns2021mean = pitcher.objects.all().filter(loaded_2021 = True).exclude(shutdowns2021 = 0).aggregate(Avg("shutdowns2021"))
   meltdowns2021stddev = pitcher.objects.all().filter(loaded_2021 = True).exclude(meltdowns2021 = 0).aggregate(StdDev("meltdowns2021"))
   meltdowns2021mean = pitcher.objects.all().filter(loaded_2021 = True).exclude(meltdowns2021 = 0).aggregate(Avg("meltdowns2021"))
   eraminus2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("eraminus2021"))
   eraminus2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("eraminus2021"))
   fipminus2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("fipminus2021"))
   fipminus2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("fipminus2021"))
   xfipminus2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xfipminus2021"))
   xfipminus2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("xfipminus2021"))
   bbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("bbpercent2021"))
   bbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("bbpercent2021"))
   cswpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("cswpercent2021"))
   cswpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("cswpercent2021"))
   softpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("softpercent2021"))
   softpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("softpercent2021"))
   mediumpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("mediumpercent2021"))
   mediumpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("mediumpercent2021"))
   softplusmediumpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("softplusmediumpercent2021"))
   softplusmediumpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("softplusmediumpercent2021"))
   runsaverage2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("runsaverage2021"))
   runsaverage2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("runsaverage2021"))
   softplusmediumpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("softplusmediumpercent2021"))
   softplusmediumpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("softplusmediumpercent2021"))
   kwera2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("kwera2021"))
   kwera2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("kwera2021"))
   kpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("kpercent2021"))
   kpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("kpercent2021"))
   weakpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("weakpercent2021"))
   weakpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("weakpercent2021"))
   siera2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("siera2021"))
   siera2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("siera2021"))
   plus_k_per_nine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_k_per_nine2021"))
   plus_k_per_nine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_k_per_nine2021"))
   plus_bb_per_nine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_bb_per_nine2021"))
   plus_bb_per_nine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_bb_per_nine2021"))
   plus_k_per_bb2021stddev = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_2021 = True).aggregate(StdDev("plus_k_per_bb2021"))
   plus_k_per_bb2021mean = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_2021 = True).aggregate(Avg("plus_k_per_bb2021"))
   plus_h_per_nine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_h_per_nine2021"))
   plus_h_per_nine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_h_per_nine2021"))
   plus_hr_per_nine2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_hr_per_nine2021"))
   plus_hr_per_nine2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_hr_per_nine2021"))
   plus_avg2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_avg2021"))
   plus_avg2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_avg2021"))
   plus_whip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_whip2021"))
   plus_whip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_whip2021"))
   plus_babip2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_babip2021"))
   plus_babip2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_babip2021"))
   plus_lobpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_lobpercent2021"))
   plus_lobpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_lobpercent2021"))
   plus_kpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_kpercent2021"))
   plus_kpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_kpercent2021"))
   plus_bbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_bbpercent2021"))
   plus_bbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_bbpercent2021"))
   plus_ldpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_ldpercent2021"))
   plus_ldpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_ldpercent2021"))
   plus_gbpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_gbpercent2021"))
   plus_gbpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_gbpercent2021"))
   plus_hrperfb2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_hrperfb2021"))
   plus_hrperfb2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_hrperfb2021"))
   plus_softpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_softpercent2021"))
   plus_softpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_softpercent2021"))
   plus_mediumpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("plus_mediumpercent2021"))
   plus_mediumpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("plus_mediumpercent2021"))
   barrel_percent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("barrel_percent2021"))
   barrel_percent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("barrel_percent2021"))
   hardhitpercent2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("hardhitpercent2021"))
   hardhitpercent2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("hardhitpercent2021"))
   averageev2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("averageev2021"))
   averageev2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("averageev2021"))
   averagela2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("averagela2021"))
   averagela2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("averagela2021"))
   xera2021stddev = pitcher.objects.all().filter(loaded_2021 = True).aggregate(StdDev("xera2021"))
   xera2021mean = pitcher.objects.all().filter(loaded_2021 = True).aggregate(Avg("xera2021"))
 
   #baseball savant barrel 2021
   bbevents2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("bbevents2021"))
   bbevents2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("bbevents2021"))
   #avghitangle2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("avghitangle2021"))
   #avghitangle2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("avghitangle2021"))
   anglesweetspotpercent2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("anglesweetspotpercent2021"))
   anglesweetspotpercent2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("anglesweetspotpercent2021"))
   #anglehitspeed2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("anglehitspeed2021"))
   #anglehitspeed2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("anglehitspeed2021"))
   #bsgbpercent2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("bsgbpercent2021"))
   #bsgbpercent2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("bsgbpercent2021"))
   avgdistance2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("avgdistance2021"))
   avgdistance2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("avgdistance2021"))
   ev95plus2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("ev95plus2021"))
   ev95plus2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("ev95plus2021"))
   #brlpercent2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("brlpercent2021"))
   #brlpercent2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("brlpercent2021"))
   ev95pluspercent2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("ev95pluspercent2021"))
   ev95pluspercent2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("ev95pluspercent2021"))
   brlperpa2021stddev = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(StdDev("brlperpa2021"))
   brlperpa2021mean = pitcher.objects.all().filter(loaded_bs_barrel_2021 = True).aggregate(Avg("brlperpa2021"))
 
   #baseball savant expected 2021
   bip2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("bip2021"))
   bip2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("bip2021"))
   xavg2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xavg2021"))
   xavg2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xavg2021"))
   xavgdiff2021stddev = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_bs_x_2021 = True).aggregate(StdDev("xavgdiff2021"))
   xavgdiff2021mean = pitcher.objects.all().filter(loaded_k_per_bb2021 = True).filter(loaded_bs_x_2021 = True).aggregate(Avg("xavgdiff2021"))
   slg2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("slg2021"))
   slg2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("slg2021"))
   xslg2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xslg2021"))
   xslg2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xslg2021"))
   xslgdiff2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xslgdiff2021"))
   xslgdiff2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xslgdiff2021"))
   woba2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("woba2021"))
   woba2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("woba2021"))
   xwoba2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xwoba2021"))
   xwoba2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xwoba2021"))
   xwobadiff2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xwobadiff2021"))
   xwobadiff2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xwobadiff2021"))
   #2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("bsera2021"))
   #bsera2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("bsera2021"))
   #bsxera2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("bsxera2021"))
   #bsxera2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("bsxera2021"))
   xeradiff2021stddev = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(StdDev("xeradiff2021"))
   xeradiff2021mean = pitcher.objects.all().filter(loaded_bs_x_2021 = True).aggregate(Avg("xeradiff2021"))
 
 
   for zpitcher in pitcher.objects.all().filter(loaded_2021 = True):
     zpitcher.zwinningpercent2021 = (zpitcher.winningpercent2021 - winningpercent2021mean["winningpercent2021__avg"]) / winningpercent2021stddev["winningpercent2021__stddev"]
     zpitcher.zwar2021 = (zpitcher.war2021 - war2021mean["war2021__avg"]) / war2021stddev["war2021__stddev"]
     #must invert z-score
     zpitcher.zera2021 = -(zpitcher.era2021 - era2021mean["era2021__avg"]) / era2021stddev["era2021__stddev"]
     zpitcher.zshutouts2021 = (zpitcher.shutouts2021 - shutouts2021mean["shutouts2021__avg"]) / shutouts2021stddev["shutouts2021__stddev"]
     if zpitcher.saves2021 > 1:
       zpitcher.zsaves2021 = (zpitcher.saves2021 - saves2021mean["saves2021__avg"]) / saves2021stddev["saves2021__stddev"]
       zpitcher.zsavepercent2021 = (zpitcher.savepercent2021 - savepercent2021mean["savepercent2021__avg"]) / savepercent2021stddev["savepercent2021__stddev"]
     else:
       zpitcher.zsaves2021 = 0
       zpitcher.zsavepercent2021 = 0
     zpitcher.zinnings2021 = (zpitcher.innings2021 - innings2021mean["innings2021__avg"]) / innings2021stddev["innings2021__stddev"]
     zpitcher.zbattersfaced2021 = (zpitcher.battersfaced2021 - battersfaced2021mean["battersfaced2021__avg"]) / battersfaced2021stddev["battersfaced2021__stddev"]
     zpitcher.zhits2021 = (zpitcher.hits2021 - hits2021mean["hits2021__avg"]) / hits2021stddev["hits2021__stddev"]
     zpitcher.zruns2021 = (zpitcher.runs2021 - runs2021mean["runs2021__avg"]) / runs2021stddev["runs2021__stddev"]
     # #must invert z-score
     # zpitcher.zrunsaverage2021 = -(zpitcher.runsaverage2021 - runsaverage2021mean["runsaverage2021__avg"]) / runsaverage2021stddev["runsaverage2021__stddev"]
     zpitcher.zhomeruns2021 = (zpitcher.homeruns2021 - homeruns2021mean["homeruns2021__avg"]) / homeruns2021stddev["homeruns2021__stddev"]
     zpitcher.zbbhbp2021 = (zpitcher.bbhbp2021 - bbhbp2021mean["bbhbp2021__avg"]) / bbhbp2021stddev["bbhbp2021__stddev"]
     zpitcher.zk2021 = (zpitcher.k2021 - k2021mean["k2021__avg"]) / k2021stddev["k2021__stddev"]
     zpitcher.zthrownforkpercent2021 = (zpitcher.thrownforkpercent2021 - thrownforkpercent2021mean["thrownforkpercent2021__avg"]) / thrownforkpercent2021stddev["thrownforkpercent2021__stddev"]
     zpitcher.zkpernine2021 = (zpitcher.kpernine2021 - kpernine2021mean["kpernine2021__avg"]) / kpernine2021stddev["kpernine2021__stddev"]
     #must invert z-score
     zpitcher.zbbpernine2021 = -(zpitcher.bbpernine2021 - bbpernine2021mean["bbpernine2021__avg"]) / bbpernine2021stddev["bbpernine2021__stddev"]
     #must invert z-score
     zpitcher.zhitpernine2021 = -(zpitcher.hitpernine2021 - hitpernine2021mean["hitpernine2021__avg"]) / hitpernine2021stddev["hitpernine2021__stddev"]
     #must invert z-score
     zpitcher.zhrpernine2021 = -(zpitcher.hrpernine2021 - hrpernine2021mean["hrpernine2021__avg"]) / hrpernine2021stddev["hrpernine2021__stddev"]
     zpitcher.zkperbb2021 = (zpitcher.kperbb2021 - kperbb2021mean["kperbb2021__avg"]) / kperbb2021stddev["kperbb2021__stddev"]
     #must invert z-score
     zpitcher.zavg2021 = -(zpitcher.avg2021 - avg2021mean["avg2021__avg"]) / avg2021stddev["avg2021__stddev"]
     #must invert z-score
     zpitcher.zwhip2021 = -(zpitcher.whip2021 - whip2021mean["whip2021__avg"]) / whip2021stddev["whip2021__stddev"]
     #must invert z-score
     zpitcher.zbabip2021 = -(zpitcher.babip2021 - babip2021mean["babip2021__avg"]) / babip2021stddev["babip2021__stddev"]
     #must invert z-score
     zpitcher.zhrperfb2021 = -(zpitcher.hrperfb2021 - hrperfb2021mean["hrperfb2021__avg"]) / hrperfb2021stddev["hrperfb2021__stddev"]
     #must invert z-score
     zpitcher.zfip2021 = -(zpitcher.fip2021 - fip2021mean["fip2021__avg"]) / fip2021stddev["fip2021__stddev"]
     zpitcher.zgbperfb2021 = (zpitcher.gbperfb2021 - gbperfb2021mean["gbperfb2021__avg"]) / gbperfb2021stddev["gbperfb2021__stddev"]
     zpitcher.zgbpercent2021 = (zpitcher.gbpercent2021 - gbpercent2021mean["gbpercent2021__avg"]) / gbpercent2021stddev["gbpercent2021__stddev"]
     zpitcher.ziffbpercent2021 = (zpitcher.iffbpercent2021 - iffbpercent2021mean["iffbpercent2021__avg"]) / iffbpercent2021stddev["iffbpercent2021__stddev"]
     #must invert z-score
     zpitcher.zldpercent2021 = -(zpitcher.ldpercent2021 - ldpercent2021mean["ldpercent2021__avg"]) / ldpercent2021stddev["ldpercent2021__stddev"]
     #must invert z-score
     zpitcher.zfbpercent2021 = -(zpitcher.fbpercent2021 - fbpercent2021mean["fbpercent2021__avg"]) / fbpercent2021stddev["fbpercent2021__stddev"]
     zpitcher.zrar2021 = (zpitcher.rar2021 - rar2021mean["rar2021__avg"]) / rar2021stddev["rar2021__stddev"]
     #must invert z-score
     zpitcher.ztera2021 = -(zpitcher.tera2021 - tera2021mean["tera2021__avg"]) / tera2021stddev["tera2021__stddev"]
     #must invert z-score
     zpitcher.zxfip2021 = -(zpitcher.xfip2021 - xfip2021mean["xfip2021__avg"]) / xfip2021stddev["xfip2021__stddev"]
     zpitcher.zwpa2021 = (zpitcher.wpa2021 - wpa2021mean["wpa2021__avg"]) / wpa2021stddev["wpa2021__stddev"]
     zpitcher.zretwentyfour2021 = (zpitcher.retwentyfour2021 - retwentyfour2021mean["retwentyfour2021__avg"]) / retwentyfour2021stddev["retwentyfour2021__stddev"]
     zpitcher.zclutch2021 = (zpitcher.clutch2021 - clutch2021mean["clutch2021__avg"]) / clutch2021stddev["clutch2021__stddev"]
     zpitcher.zoutsidezoneswingpercent2021 = (zpitcher.outsidezoneswingpercent2021 - outsidezoneswingpercent2021mean["outsidezoneswingpercent2021__avg"]) / outsidezoneswingpercent2021stddev["outsidezoneswingpercent2021__stddev"]
     zpitcher.zfirstpitchstrikepercent2021 = (zpitcher.firstpitchstrikepercent2021 - firstpitchstrikepercent2021mean["firstpitchstrikepercent2021__avg"]) / firstpitchstrikepercent2021stddev["firstpitchstrikepercent2021__stddev"]
     zpitcher.zswingingstrikespercent2021 = (zpitcher.swingingstrikespercent2021 - swingingstrikespercent2021mean["swingingstrikespercent2021__avg"]) / swingingstrikespercent2021stddev["swingingstrikespercent2021__stddev"]
     if zpitcher.shutdowns2021 > 0:
       zpitcher.zshutdowns2021 = (zpitcher.shutdowns2021 - shutdowns2021mean["shutdowns2021__avg"]) / shutdowns2021stddev["shutdowns2021__stddev"]
     else:
       zpitcher.zshutdowns2021 = 0
     if zpitcher.meltdowns2021 > 0:
       zpitcher.zmeltdowns2021 = (zpitcher.meltdowns2021 - meltdowns2021mean["meltdowns2021__avg"]) / meltdowns2021stddev["meltdowns2021__stddev"]
     else:
       zpitcher.zmeltdowns2021 = 0
     zpitcher.zeraminus2021 = (zpitcher.eraminus2021 - eraminus2021mean["eraminus2021__avg"]) / eraminus2021stddev["eraminus2021__stddev"]
     zpitcher.zfipminus2021 = (zpitcher.fipminus2021 - fipminus2021mean["fipminus2021__avg"]) / fipminus2021stddev["fipminus2021__stddev"]
     zpitcher.zxfipminus2021 = (zpitcher.xfipminus2021 - xfipminus2021mean["xfipminus2021__avg"]) / xfipminus2021stddev["xfipminus2021__stddev"]
     #must invert z-score
     zpitcher.zbbpercent2021 = -(zpitcher.bbpercent2021 - bbpercent2021mean["bbpercent2021__avg"]) / bbpercent2021stddev["bbpercent2021__stddev"]
     zpitcher.zcswpercent2021 = (zpitcher.cswpercent2021 - cswpercent2021mean["cswpercent2021__avg"]) / cswpercent2021stddev["cswpercent2021__stddev"]
     zpitcher.zsoftpercent2021 = (zpitcher.softpercent2021 - softpercent2021mean["softpercent2021__avg"]) / softpercent2021stddev["softpercent2021__stddev"]
     zpitcher.zmediumpercent2021 = (zpitcher.mediumpercent2021 - mediumpercent2021mean["mediumpercent2021__avg"]) / mediumpercent2021stddev["mediumpercent2021__stddev"]
     zpitcher.zsoftplusmediumpercent2021 = (zpitcher.softplusmediumpercent2021 - softplusmediumpercent2021mean["softplusmediumpercent2021__avg"]) / softplusmediumpercent2021stddev["softplusmediumpercent2021__stddev"]
     #must invert z-score
     zpitcher.zrunsaverage2021 = -(zpitcher.runsaverage2021 - runsaverage2021mean["runsaverage2021__avg"]) / runsaverage2021stddev["runsaverage2021__stddev"]
     zpitcher.zsoftplusmediumpercent2021 = (zpitcher.softplusmediumpercent2021 - softplusmediumpercent2021mean["softplusmediumpercent2021__avg"]) / softplusmediumpercent2021stddev["softplusmediumpercent2021__stddev"]
     #must invert z-score
     zpitcher.zkwera2021 = -(zpitcher.kwera2021 - kwera2021mean["kwera2021__avg"]) / kwera2021stddev["kwera2021__stddev"]
     zpitcher.zkpercent2021 = (zpitcher.kpercent2021 - kpercent2021mean["kpercent2021__avg"]) / kpercent2021stddev["kpercent2021__stddev"]
     zpitcher.zweakpercent2021 = (zpitcher.weakpercent2021 - weakpercent2021mean["weakpercent2021__avg"]) / weakpercent2021stddev["weakpercent2021__stddev"]
     #must invert z-score
     zpitcher.zsiera2021 = -(zpitcher.siera2021 - siera2021mean["siera2021__avg"]) / siera2021stddev["siera2021__stddev"]
     zpitcher.zplus_k_per_nine2021 = (zpitcher.plus_k_per_nine2021 - plus_k_per_nine2021mean["plus_k_per_nine2021__avg"]) / plus_k_per_nine2021stddev["plus_k_per_nine2021__stddev"]
     #must invert z-score
     zpitcher.zplus_bb_per_nine2021 = -(zpitcher.plus_bb_per_nine2021 - plus_bb_per_nine2021mean["plus_bb_per_nine2021__avg"]) / plus_bb_per_nine2021stddev["plus_bb_per_nine2021__stddev"]
     zpitcher.zplus_k_per_bb2021 = (zpitcher.plus_k_per_bb2021 - plus_k_per_bb2021mean["plus_k_per_bb2021__avg"]) / plus_k_per_bb2021stddev["plus_k_per_bb2021__stddev"]
     #must invert z-score
     zpitcher.zplus_h_per_nine2021 = -(zpitcher.plus_h_per_nine2021 - plus_h_per_nine2021mean["plus_h_per_nine2021__avg"]) / plus_h_per_nine2021stddev["plus_h_per_nine2021__stddev"]
     #must invert z-score
     zpitcher.zplus_hr_per_nine2021 = -(zpitcher.plus_hr_per_nine2021 - plus_hr_per_nine2021mean["plus_hr_per_nine2021__avg"]) / plus_hr_per_nine2021stddev["plus_hr_per_nine2021__stddev"]
     #must invert z-score
     zpitcher.zplus_avg2021 = -(zpitcher.plus_avg2021 - plus_avg2021mean["plus_avg2021__avg"]) / plus_avg2021stddev["plus_avg2021__stddev"]
     #must invert z-score
     zpitcher.zplus_whip2021 = -(zpitcher.plus_whip2021 - plus_whip2021mean["plus_whip2021__avg"]) / plus_whip2021stddev["plus_whip2021__stddev"]
     #must invert z-score
     zpitcher.zplus_babip2021 = -(zpitcher.plus_babip2021 - plus_babip2021mean["plus_babip2021__avg"]) / plus_babip2021stddev["plus_babip2021__stddev"]
     zpitcher.zplus_lobpercent2021 = (zpitcher.plus_lobpercent2021 - plus_lobpercent2021mean["plus_lobpercent2021__avg"]) / plus_lobpercent2021stddev["plus_lobpercent2021__stddev"]
     zpitcher.zplus_kpercent2021 = (zpitcher.plus_kpercent2021 - plus_kpercent2021mean["plus_kpercent2021__avg"]) / plus_kpercent2021stddev["plus_kpercent2021__stddev"]
     #must invert z-score
     zpitcher.zplus_bbpercent2021 = -(zpitcher.plus_bbpercent2021 - plus_bbpercent2021mean["plus_bbpercent2021__avg"]) / plus_bbpercent2021stddev["plus_bbpercent2021__stddev"]
     #must invert z-score
     zpitcher.zplus_ldpercent2021 = -(zpitcher.plus_ldpercent2021 - plus_ldpercent2021mean["plus_ldpercent2021__avg"]) / plus_ldpercent2021stddev["plus_ldpercent2021__stddev"]
     zpitcher.zplus_gbpercent2021 = (zpitcher.plus_gbpercent2021 - plus_gbpercent2021mean["plus_gbpercent2021__avg"]) / plus_gbpercent2021stddev["plus_gbpercent2021__stddev"]
     #must invert z-score
     zpitcher.zplus_hrperfb2021 = -(zpitcher.plus_hrperfb2021 - plus_hrperfb2021mean["plus_hrperfb2021__avg"]) / plus_hrperfb2021stddev["plus_hrperfb2021__stddev"]
     zpitcher.zplus_softpercent2021 = (zpitcher.plus_softpercent2021 - plus_softpercent2021mean["plus_softpercent2021__avg"]) / plus_softpercent2021stddev["plus_softpercent2021__stddev"]
     zpitcher.zplus_mediumpercent2021 = (zpitcher.plus_mediumpercent2021 - plus_mediumpercent2021mean["plus_mediumpercent2021__avg"]) / plus_mediumpercent2021stddev["plus_mediumpercent2021__stddev"]
     #must invert z-score
     zpitcher.zbarrel_percent2021 = -(zpitcher.barrel_percent2021 - barrel_percent2021mean["barrel_percent2021__avg"]) / barrel_percent2021stddev["barrel_percent2021__stddev"]
     #must invert z-score
     zpitcher.zhardhitpercent2021 = -(zpitcher.hardhitpercent2021 - hardhitpercent2021mean["hardhitpercent2021__avg"]) / hardhitpercent2021stddev["hardhitpercent2021__stddev"]
     #must invert z-score
     zpitcher.zaverageev2021 = -(zpitcher.averageev2021 - averageev2021mean["averageev2021__avg"]) / averageev2021stddev["averageev2021__stddev"]
     zpitcher.zaveragela2021 = (zpitcher.averagela2021 - averagela2021mean["averagela2021__avg"]) / averagela2021stddev["averagela2021__stddev"]
     #must invert z-score
     zpitcher.zxera2021 = -(zpitcher.xera2021 - xera2021mean["xera2021__avg"]) / xera2021stddev["xera2021__stddev"]
     if zpitcher.loaded_bs_barrel_2021 == True:
       zpitcher.zbbevents2021 = (zpitcher.bbevents2021 - bbevents2021mean["bbevents2021__avg"]) / bbevents2021stddev["bbevents2021__stddev"]
       #zpitcher.zavghitangle2021 = (zpitcher.avghitangle2021 - avghitangle2021mean["avghitangle2021__avg"]) / avghitangle2021stddev["avghitangle2021__stddev"]
       #must invert z-score
       zpitcher.zanglesweetspotpercent2021 = -(zpitcher.anglesweetspotpercent2021 - anglesweetspotpercent2021mean["anglesweetspotpercent2021__avg"]) / anglesweetspotpercent2021stddev["anglesweetspotpercent2021__stddev"]
       #zpitcher.zanglehitspeed2021 = (zpitcher.anglehitspeed2021 - anglehitspeed2021mean["anglehitspeed2021__avg"]) / anglehitspeed2021stddev["anglehitspeed2021__stddev"]
       #zpitcher.zbsgbpercent2021 = (zpitcher.bsgbpercent2021 - bsgbpercent2021mean["bsgbpercent2021__avg"]) / bsgbpercent2021stddev["bsgbpercent2021__stddev"]
       #must invert z-score
       zpitcher.zavgdistance2021 = -(zpitcher.avgdistance2021 - avgdistance2021mean["avgdistance2021__avg"]) / avgdistance2021stddev["avgdistance2021__stddev"]
       zpitcher.zev95plus2021 = (zpitcher.ev95plus2021 - ev95plus2021mean["ev95plus2021__avg"]) / ev95plus2021stddev["ev95plus2021__stddev"]
       #zpitcher.zbrlpercent2021 = (zpitcher.brlpercent2021 - brlpercent2021mean["brlpercent2021__avg"]) / brlpercent2021stddev["brlpercent2021__stddev"]
       #must invert z-score
       zpitcher.zev95pluspercent2021 = -(zpitcher.ev95pluspercent2021 - ev95pluspercent2021mean["ev95pluspercent2021__avg"]) / ev95pluspercent2021stddev["ev95pluspercent2021__stddev"]
       #must invert z-score
       zpitcher.zbrlperpa2021 = -(zpitcher.brlperpa2021 - brlperpa2021mean["brlperpa2021__avg"]) / brlperpa2021stddev["brlperpa2021__stddev"]
     if zpitcher.loaded_bs_x_2021 == True:
       zpitcher.zbip2021 = (zpitcher.bip2021 - bip2021mean["bip2021__avg"]) / bip2021stddev["bip2021__stddev"]
       #must invert z-score
       zpitcher.zxavg2021 = -(zpitcher.xavg2021 - xavg2021mean["xavg2021__avg"]) / xavg2021stddev["xavg2021__stddev"]
       zpitcher.zxavgdiff2021 = (zpitcher.xavgdiff2021 - xavgdiff2021mean["xavgdiff2021__avg"]) / xavgdiff2021stddev["xavgdiff2021__stddev"]
       #must invert z-score
       zpitcher.zslg2021 = -(zpitcher.slg2021 - slg2021mean["slg2021__avg"]) / slg2021stddev["slg2021__stddev"]
       #must invert z-score
       zpitcher.zxslg2021 = -(zpitcher.xslg2021 - xslg2021mean["xslg2021__avg"]) / xslg2021stddev["xslg2021__stddev"]
       zpitcher.zxslgdiff2021 = (zpitcher.xslgdiff2021 - xslgdiff2021mean["xslgdiff2021__avg"]) / xslgdiff2021stddev["xslgdiff2021__stddev"]
       #must invert z-score
       zpitcher.zwoba2021 = -(zpitcher.woba2021 - woba2021mean["woba2021__avg"]) / woba2021stddev["woba2021__stddev"]
       #must invert z-score
       zpitcher.zxwoba2021 = -(zpitcher.xwoba2021 - xwoba2021mean["xwoba2021__avg"]) / xwoba2021stddev["xwoba2021__stddev"]
       zpitcher.zxwobadiff2021 = (zpitcher.xwobadiff2021 - xwobadiff2021mean["xwobadiff2021__avg"]) / xwobadiff2021stddev["xwobadiff2021__stddev"]
       #zpitcher.zbsera2021 = (zpitcher.bsera2021 - bsera2021mean["bsera2021__avg"]) / bsera2021stddev["bsera2021__stddev"]
       #zpitcher.zbsxera2021 = (zpitcher.bsxera2021 - bsxera2021mean["bsxera2021__avg"]) / bsxera2021stddev["bsxera2021__stddev"]
       zpitcher.zxeradiff2021 = (zpitcher.xeradiff2021 - xeradiff2021mean["xeradiff2021__avg"]) / xeradiff2021stddev["xeradiff2021__stddev"]
     zpitcher.save()