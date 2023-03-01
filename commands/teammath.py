import decimal
from django.core.management.base import BaseCommand
from app_bb.models import team
from django.db.models.aggregates import StdDev, Avg

# for other math scripts, you will need to filter for some of the stats. How to handle pitcher-batters? increase sample size requirement?
#takes 4 seconds to run

#not available: slugging, many other categories

class Command(BaseCommand):
  def handle(self, *args, **options):
    errorsstddev = team.objects.all().aggregate(StdDev("errors"))
    errorsmean = team.objects.all().aggregate(Avg("errors"))
    doubleplaysstddev = team.objects.all().aggregate(StdDev("doubleplays"))
    doubleplaysmean = team.objects.all().aggregate(Avg("doubleplays"))
    fieldingpercentagestddev = team.objects.all().aggregate(StdDev("fieldingpercentage"))
    fieldingpercentagemean = team.objects.all().aggregate(Avg("fieldingpercentage"))
    sbagainststddev = team.objects.all().aggregate(StdDev("sbagainst"))
    sbagainstmean = team.objects.all().aggregate(Avg("sbagainst"))
    csagainststddev = team.objects.all().aggregate(StdDev("csagainst"))
    csagainstmean = team.objects.all().aggregate(Avg("csagainst"))
    xsbsavedagainststddev = team.objects.all().aggregate(StdDev("xsbsavedagainst"))
    xsbsavedagainstmean = team.objects.all().aggregate(Avg("xsbsavedagainst"))
    wildpitchespluspassedballsstddev = team.objects.all().aggregate(StdDev("wildpitchespluspassedballs"))
    wildpitchespluspassedballsmean = team.objects.all().aggregate(Avg("wildpitchespluspassedballs"))
    defensiverunssavedstddev = team.objects.all().aggregate(StdDev("defensiverunssaved"))
    defensiverunssavedmean = team.objects.all().aggregate(Avg("defensiverunssaved"))
    ultimatezoneratingstddev = team.objects.all().aggregate(StdDev("ultimatezonerating"))
    ultimatezoneratingmean = team.objects.all().aggregate(Avg("ultimatezonerating"))
    defensestddev = team.objects.all().aggregate(StdDev("defense"))
    defensemean = team.objects.all().aggregate(Avg("defense"))
    barrel_percentbpstddev = team.objects.all().aggregate(StdDev("barrel_percentbp"))
    barrel_percentbpmean = team.objects.all().aggregate(Avg("barrel_percentbp"))
    brl_per_pabpstddev = team.objects.all().aggregate(StdDev("brl_per_pabp"))
    brl_per_pabpmean = team.objects.all().aggregate(Avg("brl_per_pabp"))
    hardhitpercentbpstddev = team.objects.all().aggregate(StdDev("hardhitpercentbp"))
    hardhitpercentbpmean = team.objects.all().aggregate(Avg("hardhitpercentbp"))
    averageevbpstddev = team.objects.all().aggregate(StdDev("averageevbp"))
    averageevbpmean = team.objects.all().aggregate(Avg("averageevbp"))
    averagelabpstddev = team.objects.all().aggregate(StdDev("averagelabp"))
    averagelabpmean = team.objects.all().aggregate(Avg("averagelabp"))
    plus_k_per_ninebpstddev = team.objects.all().aggregate(StdDev("plus_k_per_ninebp"))
    plus_k_per_ninebpmean = team.objects.all().aggregate(Avg("plus_k_per_ninebp"))
    plus_bb_per_ninebpstddev = team.objects.all().aggregate(StdDev("plus_bb_per_ninebp"))
    plus_bb_per_ninebpmean = team.objects.all().aggregate(Avg("plus_bb_per_ninebp"))
    plus_k_per_bbbpstddev = team.objects.all().aggregate(StdDev("plus_k_per_bbbp"))
    plus_k_per_bbbpmean = team.objects.all().aggregate(Avg("plus_k_per_bbbp"))
    plus_hr_per_ninebpstddev = team.objects.all().aggregate(StdDev("plus_hr_per_ninebp"))
    plus_hr_per_ninebpmean = team.objects.all().aggregate(Avg("plus_hr_per_ninebp"))
    plus_avgbpstddev = team.objects.all().aggregate(StdDev("plus_avgbp"))
    plus_avgbpmean = team.objects.all().aggregate(Avg("plus_avgbp"))
    plus_whipbpstddev = team.objects.all().aggregate(StdDev("plus_whipbp"))
    plus_whipbpmean = team.objects.all().aggregate(Avg("plus_whipbp"))
    plus_babipbpstddev = team.objects.all().aggregate(StdDev("plus_babipbp"))
    plus_babipbpmean = team.objects.all().aggregate(Avg("plus_babipbp"))
    plus_lobpercentbpstddev = team.objects.all().aggregate(StdDev("plus_lobpercentbp"))
    plus_lobpercentbpmean = team.objects.all().aggregate(Avg("plus_lobpercentbp"))
    plus_kpercentbpstddev = team.objects.all().aggregate(StdDev("plus_kpercentbp"))
    plus_kpercentbpmean = team.objects.all().aggregate(Avg("plus_kpercentbp"))
    plus_bbpercentbpstddev = team.objects.all().aggregate(StdDev("plus_bbpercentbp"))
    plus_bbpercentbpmean = team.objects.all().aggregate(Avg("plus_bbpercentbp"))
    plus_ldpercentbpstddev = team.objects.all().aggregate(StdDev("plus_ldpercentbp"))
    plus_ldpercentbpmean = team.objects.all().aggregate(Avg("plus_ldpercentbp"))
    plus_gbpercentbpstddev = team.objects.all().aggregate(StdDev("plus_gbpercentbp"))
    plus_gbpercentbpmean = team.objects.all().aggregate(Avg("plus_gbpercentbp"))
    warbpstddev = team.objects.all().aggregate(StdDev("warbp"))
    warbpmean = team.objects.all().aggregate(Avg("warbp"))
    rarbpstddev = team.objects.all().aggregate(StdDev("rarbp"))
    rarbpmean = team.objects.all().aggregate(Avg("rarbp"))
    cswpercentbpstddev = team.objects.all().aggregate(StdDev("cswpercentbp"))
    cswpercentbpmean = team.objects.all().aggregate(Avg("cswpercentbp"))
    swingingstrikespercentbpstddev = team.objects.all().aggregate(StdDev("swingingstrikespercentbp"))
    swingingstrikespercentbpmean = team.objects.all().aggregate(Avg("swingingstrikespercentbp"))
    firstpitchstrikepercentbpstddev = team.objects.all().aggregate(StdDev("firstpitchstrikepercentbp"))
    firstpitchstrikepercentbpmean = team.objects.all().aggregate(Avg("firstpitchstrikepercentbp"))
    outsidezoneswingpercentbpstddev = team.objects.all().aggregate(StdDev("outsidezoneswingpercentbp"))
    outsidezoneswingpercentbpmean = team.objects.all().aggregate(Avg("outsidezoneswingpercentbp"))
    wpabpstddev = team.objects.all().aggregate(StdDev("wpabp"))
    wpabpmean = team.objects.all().aggregate(Avg("wpabp"))
    retwentyfourbpstddev = team.objects.all().aggregate(StdDev("retwentyfourbp"))
    retwentyfourbpmean = team.objects.all().aggregate(Avg("retwentyfourbp"))
    clutchbpstddev = team.objects.all().aggregate(StdDev("clutchbp"))
    clutchbpmean = team.objects.all().aggregate(Avg("clutchbp"))
    shutdownbpstddev = team.objects.all().aggregate(StdDev("shutdownbp"))
    shutdownbpmean = team.objects.all().aggregate(Avg("shutdownbp"))
    meltdownbpstddev = team.objects.all().aggregate(StdDev("meltdownbp"))
    meltdownbpmean = team.objects.all().aggregate(Avg("meltdownbp"))
    shutdownpermeltdownbpstddev = team.objects.all().aggregate(StdDev("shutdownpermeltdownbp"))
    shutdownpermeltdownbpmean = team.objects.all().aggregate(Avg("shutdownpermeltdownbp"))
    #weakpercentbpstddev = team.objects.all().aggregate(StdDev("weakpercentbp"))
    #weakpercentbpmean = team.objects.all().aggregate(Avg("weakpercentbp"))
    softplusmediumpercentbpstddev = team.objects.all().aggregate(StdDev("softplusmediumpercentbp"))
    softplusmediumpercentbpmean = team.objects.all().aggregate(Avg("softplusmediumpercentbp"))
    mediumpercentbpstddev = team.objects.all().aggregate(StdDev("mediumpercentbp"))
    mediumpercentbpmean = team.objects.all().aggregate(Avg("mediumpercentbp"))
    softpercentbpstddev = team.objects.all().aggregate(StdDev("softpercentbp"))
    softpercentbpmean = team.objects.all().aggregate(Avg("softpercentbp"))
    #hrperfbbpstddev = team.objects.all().aggregate(StdDev("hrperfbbp"))
    #hrperfbbpmean = team.objects.all().aggregate(Avg("hrperfbbp"))
    thrownforkpercentbpstddev = team.objects.all().aggregate(StdDev("thrownforkpercentbp"))
    thrownforkpercentbpmean = team.objects.all().aggregate(Avg("thrownforkpercentbp"))
    iffbpercentbpstddev = team.objects.all().aggregate(StdDev("iffbpercentbp"))
    iffbpercentbpmean = team.objects.all().aggregate(Avg("iffbpercentbp"))
    fbpercentbpstddev = team.objects.all().aggregate(StdDev("fbpercentbp"))
    fbpercentbpmean = team.objects.all().aggregate(Avg("fbpercentbp"))
    ldpercentbpstddev = team.objects.all().aggregate(StdDev("ldpercentbp"))
    ldpercentbpmean = team.objects.all().aggregate(Avg("ldpercentbp"))
    gbpercentbpstddev = team.objects.all().aggregate(StdDev("gbpercentbp"))
    gbpercentbpmean = team.objects.all().aggregate(Avg("gbpercentbp"))
    gbperfbbpstddev = team.objects.all().aggregate(StdDev("gbperfbbp"))
    gbperfbbpmean = team.objects.all().aggregate(Avg("gbperfbbp"))
    sierabpstddev = team.objects.all().aggregate(StdDev("sierabp"))
    sierabpmean = team.objects.all().aggregate(Avg("sierabp"))
    xfipbpstddev = team.objects.all().aggregate(StdDev("xfipbp"))
    xfipbpmean = team.objects.all().aggregate(Avg("xfipbp"))
    fipbpstddev = team.objects.all().aggregate(StdDev("fipbp"))
    fipbpmean = team.objects.all().aggregate(Avg("fipbp"))
    xfipminusbpstddev = team.objects.all().aggregate(StdDev("xfipminusbp"))
    xfipminusbpmean = team.objects.all().aggregate(Avg("xfipminusbp"))
    fipminusbpstddev = team.objects.all().aggregate(StdDev("fipminusbp"))
    fipminusbpmean = team.objects.all().aggregate(Avg("fipminusbp"))
    eraminusbpstddev = team.objects.all().aggregate(StdDev("eraminusbp"))
    eraminusbpmean = team.objects.all().aggregate(Avg("eraminusbp"))
    lobpercentbpstddev = team.objects.all().aggregate(StdDev("lobpercentbp"))
    lobpercentbpmean = team.objects.all().aggregate(Avg("lobpercentbp"))
    babipbpstddev = team.objects.all().aggregate(StdDev("babipbp"))
    babipbpmean = team.objects.all().aggregate(Avg("babipbp"))
    whipbpstddev = team.objects.all().aggregate(StdDev("whipbp"))
    whipbpmean = team.objects.all().aggregate(Avg("whipbp"))
    avgbpstddev = team.objects.all().aggregate(StdDev("avgbp"))
    avgbpmean = team.objects.all().aggregate(Avg("avgbp"))
    kpercentminusbbpercentbpstddev = team.objects.all().aggregate(StdDev("kpercentminusbbpercentbp"))
    kpercentminusbbpercentbpmean = team.objects.all().aggregate(Avg("kpercentminusbbpercentbp"))
    bbpercentbpstddev = team.objects.all().aggregate(StdDev("bbpercentbp"))
    bbpercentbpmean = team.objects.all().aggregate(Avg("bbpercentbp"))
    kpercentbpstddev = team.objects.all().aggregate(StdDev("kpercentbp"))
    kpercentbpmean = team.objects.all().aggregate(Avg("kpercentbp"))
    hrperninebpstddev = team.objects.all().aggregate(StdDev("hrperninebp"))
    hrperninebpmean = team.objects.all().aggregate(Avg("hrperninebp"))
    kperbbbpstddev = team.objects.all().aggregate(StdDev("kperbbbp"))
    kperbbbpmean = team.objects.all().aggregate(Avg("kperbbbp"))
    bbperninebpstddev = team.objects.all().aggregate(StdDev("bbperninebp"))
    bbperninebpmean = team.objects.all().aggregate(Avg("bbperninebp"))
    kperninebpstddev = team.objects.all().aggregate(StdDev("kperninebp"))
    kperninebpmean = team.objects.all().aggregate(Avg("kperninebp"))
    kbpstddev = team.objects.all().aggregate(StdDev("kbp"))
    kbpmean = team.objects.all().aggregate(Avg("kbp"))
    bbhbpbpstddev = team.objects.all().aggregate(StdDev("bbhbpbp"))
    bbhbpbpmean = team.objects.all().aggregate(Avg("bbhbpbp"))
    homerunsbpstddev = team.objects.all().aggregate(StdDev("homerunsbp"))
    homerunsbpmean = team.objects.all().aggregate(Avg("homerunsbp"))
    hitsperninebpstddev = team.objects.all().aggregate(StdDev("hitsperninebp"))
    hitsperninebpmean = team.objects.all().aggregate(Avg("hitsperninebp"))
    runsaveragebpstddev = team.objects.all().aggregate(StdDev("runsaveragebp"))
    runsaveragebpmean = team.objects.all().aggregate(Avg("runsaveragebp"))
    runsbpstddev = team.objects.all().aggregate(StdDev("runsbp"))
    runsbpmean = team.objects.all().aggregate(Avg("runsbp"))
    hitsbpstddev = team.objects.all().aggregate(StdDev("hitsbp"))
    hitsbpmean = team.objects.all().aggregate(Avg("hitsbp"))
    savepercentbpstddev = team.objects.all().aggregate(StdDev("savepercentbp"))
    savepercentbpmean = team.objects.all().aggregate(Avg("savepercentbp"))
    savesbpstddev = team.objects.all().aggregate(StdDev("savesbp"))
    savesbpmean = team.objects.all().aggregate(Avg("savesbp"))
    battersfacedbpstddev = team.objects.all().aggregate(StdDev("battersfacedbp"))
    battersfacedbpmean = team.objects.all().aggregate(Avg("battersfacedbp"))
    inningsbpstddev = team.objects.all().aggregate(StdDev("inningsbp"))
    inningsbpmean = team.objects.all().aggregate(Avg("inningsbp"))
    winningpercentbpstddev = team.objects.all().aggregate(StdDev("winningpercentbp"))
    winningpercentbpmean = team.objects.all().aggregate(Avg("winningpercentbp"))
    erabpstddev = team.objects.all().aggregate(StdDev("erabp"))
    erabpmean = team.objects.all().aggregate(Avg("erabp"))

    for zteam in team.objects.all():
      zteam.zerrors = (zteam.errors - errorsmean["errors__avg"]) / errorsstddev["errors__stddev"]
      zteam.zdoubleplays = (zteam.doubleplays - doubleplaysmean["doubleplays__avg"]) / doubleplaysstddev["doubleplays__stddev"]
      zteam.zfieldingpercentage = (zteam.fieldingpercentage - fieldingpercentagemean["fieldingpercentage__avg"]) / fieldingpercentagestddev["fieldingpercentage__stddev"]
      zteam.zsbagainst = (zteam.sbagainst - sbagainstmean["sbagainst__avg"]) / sbagainststddev["sbagainst__stddev"]
      zteam.zcsagainst = (zteam.csagainst - csagainstmean["csagainst__avg"]) / csagainststddev["csagainst__stddev"]
      zteam.zxsbsavedagainst = (zteam.xsbsavedagainst - xsbsavedagainstmean["xsbsavedagainst__avg"]) / xsbsavedagainststddev["xsbsavedagainst__stddev"]
      #must invert z-score
      zteam.zwildpitchespluspassedballs = -(zteam.wildpitchespluspassedballs - wildpitchespluspassedballsmean["wildpitchespluspassedballs__avg"]) / wildpitchespluspassedballsstddev["wildpitchespluspassedballs__stddev"]
      zteam.zdefensiverunssaved = (zteam.defensiverunssaved - defensiverunssavedmean["defensiverunssaved__avg"]) / defensiverunssavedstddev["defensiverunssaved__stddev"]
      zteam.zultimatezonerating = (zteam.ultimatezonerating - ultimatezoneratingmean["ultimatezonerating__avg"]) / ultimatezoneratingstddev["ultimatezonerating__stddev"]
      zteam.zdefense = (zteam.defense - defensemean["defense__avg"]) / defensestddev["defense__stddev"]
      #must invert z-score
      zteam.zbarrel_percentbp = -(zteam.barrel_percentbp - barrel_percentbpmean["barrel_percentbp__avg"]) / barrel_percentbpstddev["barrel_percentbp__stddev"]
      #must invert z-score
      zteam.zbrl_per_pabp = -(zteam.brl_per_pabp - brl_per_pabpmean["brl_per_pabp__avg"]) / brl_per_pabpstddev["brl_per_pabp__stddev"]
      #must invert z-score
      zteam.zhardhitpercentbp = -(zteam.hardhitpercentbp - hardhitpercentbpmean["hardhitpercentbp__avg"]) / hardhitpercentbpstddev["hardhitpercentbp__stddev"]
      #must invert z-score
      zteam.zaverageevbp = -(zteam.averageevbp - averageevbpmean["averageevbp__avg"]) / averageevbpstddev["averageevbp__stddev"]
      zteam.zaveragelabp = (zteam.averagelabp - averagelabpmean["averagelabp__avg"]) / averagelabpstddev["averagelabp__stddev"]
      zteam.zplus_k_per_ninebp = (zteam.plus_k_per_ninebp - plus_k_per_ninebpmean["plus_k_per_ninebp__avg"]) / plus_k_per_ninebpstddev["plus_k_per_ninebp__stddev"]
      #must invert z-score
      zteam.zplus_bb_per_ninebp = -(zteam.plus_bb_per_ninebp - plus_bb_per_ninebpmean["plus_bb_per_ninebp__avg"]) / plus_bb_per_ninebpstddev["plus_bb_per_ninebp__stddev"]
      zteam.zplus_k_per_bbbp = (zteam.plus_k_per_bbbp - plus_k_per_bbbpmean["plus_k_per_bbbp__avg"]) / plus_k_per_bbbpstddev["plus_k_per_bbbp__stddev"]
      #must invert z-score
      zteam.zplus_hr_per_ninebp = -(zteam.plus_hr_per_ninebp - plus_hr_per_ninebpmean["plus_hr_per_ninebp__avg"]) / plus_hr_per_ninebpstddev["plus_hr_per_ninebp__stddev"]
      #must invert z-score
      zteam.zplus_avgbp = -(zteam.plus_avgbp - plus_avgbpmean["plus_avgbp__avg"]) / plus_avgbpstddev["plus_avgbp__stddev"]
      #must invert z-score
      zteam.zplus_whipbp = -(zteam.plus_whipbp - plus_whipbpmean["plus_whipbp__avg"]) / plus_whipbpstddev["plus_whipbp__stddev"]
      #must invert z-score
      zteam.zplus_babipbp = -(zteam.plus_babipbp - plus_babipbpmean["plus_babipbp__avg"]) / plus_babipbpstddev["plus_babipbp__stddev"]
      zteam.zplus_lobpercentbp = (zteam.plus_lobpercentbp - plus_lobpercentbpmean["plus_lobpercentbp__avg"]) / plus_lobpercentbpstddev["plus_lobpercentbp__stddev"]
      zteam.zplus_kpercentbp = (zteam.plus_kpercentbp - plus_kpercentbpmean["plus_kpercentbp__avg"]) / plus_kpercentbpstddev["plus_kpercentbp__stddev"]
      #must invert z-score
      zteam.zplus_bbpercentbp = -(zteam.plus_bbpercentbp - plus_bbpercentbpmean["plus_bbpercentbp__avg"]) / plus_bbpercentbpstddev["plus_bbpercentbp__stddev"]
      #must invert z-score
      zteam.zplus_ldpercentbp = -(zteam.plus_ldpercentbp - plus_ldpercentbpmean["plus_ldpercentbp__avg"]) / plus_ldpercentbpstddev["plus_ldpercentbp__stddev"]
      zteam.zplus_gbpercentbp = (zteam.plus_gbpercentbp - plus_gbpercentbpmean["plus_gbpercentbp__avg"]) / plus_gbpercentbpstddev["plus_gbpercentbp__stddev"]
      zteam.zwarbp = (zteam.warbp - warbpmean["warbp__avg"]) / warbpstddev["warbp__stddev"]
      zteam.zrarbp = (zteam.rarbp - rarbpmean["rarbp__avg"]) / rarbpstddev["rarbp__stddev"]
      zteam.zcswpercentbp = (zteam.cswpercentbp - cswpercentbpmean["cswpercentbp__avg"]) / cswpercentbpstddev["cswpercentbp__stddev"]
      zteam.zswingingstrikespercentbp = (zteam.swingingstrikespercentbp - swingingstrikespercentbpmean["swingingstrikespercentbp__avg"]) / swingingstrikespercentbpstddev["swingingstrikespercentbp__stddev"]
      zteam.zfirstpitchstrikepercentbp = (zteam.firstpitchstrikepercentbp - firstpitchstrikepercentbpmean["firstpitchstrikepercentbp__avg"]) / firstpitchstrikepercentbpstddev["firstpitchstrikepercentbp__stddev"]
      zteam.zoutsidezoneswingpercentbp = (zteam.outsidezoneswingpercentbp - outsidezoneswingpercentbpmean["outsidezoneswingpercentbp__avg"]) / outsidezoneswingpercentbpstddev["outsidezoneswingpercentbp__stddev"]
      zteam.zwpabp = (zteam.wpabp - wpabpmean["wpabp__avg"]) / wpabpstddev["wpabp__stddev"]
      zteam.zretwentyfourbp = (zteam.retwentyfourbp - retwentyfourbpmean["retwentyfourbp__avg"]) / retwentyfourbpstddev["retwentyfourbp__stddev"]
      zteam.zclutchbp = (zteam.clutchbp - clutchbpmean["clutchbp__avg"]) / clutchbpstddev["clutchbp__stddev"]
      zteam.zshutdownbp = (zteam.shutdownbp - shutdownbpmean["shutdownbp__avg"]) / shutdownbpstddev["shutdownbp__stddev"]
      zteam.zmeltdownbp = (zteam.meltdownbp - meltdownbpmean["meltdownbp__avg"]) / meltdownbpstddev["meltdownbp__stddev"]
      zteam.zshutdownpermeltdownbp = (zteam.shutdownpermeltdownbp - shutdownpermeltdownbpmean["shutdownpermeltdownbp__avg"]) / shutdownpermeltdownbpstddev["shutdownpermeltdownbp__stddev"]
      #zteam.zweakpercentbp = (zteam.weakpercentbp - weakpercentbpmean["weakpercentbp__avg"]) / weakpercentbpstddev["weakpercentbp__stddev"]
      zteam.zsoftplusmediumpercentbp = (zteam.softplusmediumpercentbp - softplusmediumpercentbpmean["softplusmediumpercentbp__avg"]) / softplusmediumpercentbpstddev["softplusmediumpercentbp__stddev"]
      zteam.zmediumpercentbp = (zteam.mediumpercentbp - mediumpercentbpmean["mediumpercentbp__avg"]) / mediumpercentbpstddev["mediumpercentbp__stddev"]
      zteam.zsoftpercentbp = (zteam.softpercentbp - softpercentbpmean["softpercentbp__avg"]) / softpercentbpstddev["softpercentbp__stddev"]
      #zteam.zhrperfbbp = (zteam.hrperfbbp - hrperfbbpmean["hrperfbbp__avg"]) / hrperfbbpstddev["hrperfbbp__stddev"]
      zteam.zthrownforkpercentbp = (zteam.thrownforkpercentbp - thrownforkpercentbpmean["thrownforkpercentbp__avg"]) / thrownforkpercentbpstddev["thrownforkpercentbp__stddev"]
      zteam.ziffbpercentbp = (zteam.iffbpercentbp - iffbpercentbpmean["iffbpercentbp__avg"]) / iffbpercentbpstddev["iffbpercentbp__stddev"]
      #must invert z-score
      zteam.zfbpercentbp = -(zteam.fbpercentbp - fbpercentbpmean["fbpercentbp__avg"]) / fbpercentbpstddev["fbpercentbp__stddev"]
      #must invert z-score
      zteam.zldpercentbp = -(zteam.ldpercentbp - ldpercentbpmean["ldpercentbp__avg"]) / ldpercentbpstddev["ldpercentbp__stddev"]
      zteam.zgbpercentbp = (zteam.gbpercentbp - gbpercentbpmean["gbpercentbp__avg"]) / gbpercentbpstddev["gbpercentbp__stddev"]
      zteam.zgbperfbbp = (zteam.gbperfbbp - gbperfbbpmean["gbperfbbp__avg"]) / gbperfbbpstddev["gbperfbbp__stddev"]
      #must invert z-score
      zteam.zsierabp = -(zteam.sierabp - sierabpmean["sierabp__avg"]) / sierabpstddev["sierabp__stddev"]
      #must invert z-score
      zteam.zxfipbp = -(zteam.xfipbp - xfipbpmean["xfipbp__avg"]) / xfipbpstddev["xfipbp__stddev"]
      #must invert z-score
      zteam.zfipbp = -(zteam.fipbp - fipbpmean["fipbp__avg"]) / fipbpstddev["fipbp__stddev"]
      #must invert z-score
      zteam.zxfipminusbp = -(zteam.xfipminusbp - xfipminusbpmean["xfipminusbp__avg"]) / xfipminusbpstddev["xfipminusbp__stddev"]
      #must invert z-score
      zteam.zfipminusbp = -(zteam.fipminusbp - fipminusbpmean["fipminusbp__avg"]) / fipminusbpstddev["fipminusbp__stddev"]
      #must invert z-score
      zteam.zeraminusbp = -(zteam.eraminusbp - eraminusbpmean["eraminusbp__avg"]) / eraminusbpstddev["eraminusbp__stddev"]
      zteam.zlobpercentbp = (zteam.lobpercentbp - lobpercentbpmean["lobpercentbp__avg"]) / lobpercentbpstddev["lobpercentbp__stddev"]
      #must invert z-score
      zteam.zbabipbp = -(zteam.babipbp - babipbpmean["babipbp__avg"]) / babipbpstddev["babipbp__stddev"]
      #must invert z-score
      zteam.zwhipbp = -(zteam.whipbp - whipbpmean["whipbp__avg"]) / whipbpstddev["whipbp__stddev"]
      #must invert z-score
      zteam.zavgbp = -(zteam.avgbp - avgbpmean["avgbp__avg"]) / avgbpstddev["avgbp__stddev"]
      zteam.zkpercentminusbbpercentbp = (zteam.kpercentminusbbpercentbp - kpercentminusbbpercentbpmean["kpercentminusbbpercentbp__avg"]) / kpercentminusbbpercentbpstddev["kpercentminusbbpercentbp__stddev"]
      #must invert z-score
      zteam.zbbpercentbp = -(zteam.bbpercentbp - bbpercentbpmean["bbpercentbp__avg"]) / bbpercentbpstddev["bbpercentbp__stddev"]
      zteam.zkpercentbp = (zteam.kpercentbp - kpercentbpmean["kpercentbp__avg"]) / kpercentbpstddev["kpercentbp__stddev"]
      #must invert z-score
      zteam.zhrperninebp = -(zteam.hrperninebp - hrperninebpmean["hrperninebp__avg"]) / hrperninebpstddev["hrperninebp__stddev"]
      zteam.zkperbbbp = (zteam.kperbbbp - kperbbbpmean["kperbbbp__avg"]) / kperbbbpstddev["kperbbbp__stddev"]
      #must invert z-score
      zteam.zbbperninebp = -(zteam.bbperninebp - bbperninebpmean["bbperninebp__avg"]) / bbperninebpstddev["bbperninebp__stddev"]
      zteam.zkperninebp = (zteam.kperninebp - kperninebpmean["kperninebp__avg"]) / kperninebpstddev["kperninebp__stddev"]
      zteam.zkbp = (zteam.kbp - kbpmean["kbp__avg"]) / kbpstddev["kbp__stddev"]
      zteam.zbbhbpbp = (zteam.bbhbpbp - bbhbpbpmean["bbhbpbp__avg"]) / bbhbpbpstddev["bbhbpbp__stddev"]
      zteam.zhomerunsbp = (zteam.homerunsbp - homerunsbpmean["homerunsbp__avg"]) / homerunsbpstddev["homerunsbp__stddev"]
      #must invert z-score
      zteam.zhitsperninebp = -(zteam.hitsperninebp - hitsperninebpmean["hitsperninebp__avg"]) / hitsperninebpstddev["hitsperninebp__stddev"]
      #must invert z-score
      zteam.zrunsaveragebp = -(zteam.runsaveragebp - runsaveragebpmean["runsaveragebp__avg"]) / runsaveragebpstddev["runsaveragebp__stddev"]
      zteam.zrunsbp = (zteam.runsbp - runsbpmean["runsbp__avg"]) / runsbpstddev["runsbp__stddev"]
      zteam.zhitsbp = (zteam.hitsbp - hitsbpmean["hitsbp__avg"]) / hitsbpstddev["hitsbp__stddev"]
      zteam.zsavepercentbp = (zteam.savepercentbp - savepercentbpmean["savepercentbp__avg"]) / savepercentbpstddev["savepercentbp__stddev"]
      zteam.zsavesbp = (zteam.savesbp - savesbpmean["savesbp__avg"]) / savesbpstddev["savesbp__stddev"]
      zteam.zbattersfacedbp = (zteam.battersfacedbp - battersfacedbpmean["battersfacedbp__avg"]) / battersfacedbpstddev["battersfacedbp__stddev"]
      zteam.zinningsbp = (zteam.inningsbp - inningsbpmean["inningsbp__avg"]) / inningsbpstddev["inningsbp__stddev"]
      zteam.zwinningpercentbp = (zteam.winningpercentbp - winningpercentbpmean["winningpercentbp__avg"]) / winningpercentbpstddev["winningpercentbp__stddev"]
      #must invert z-score
      zteam.zerabp = -(zteam.erabp - erabpmean["erabp__avg"]) / erabpstddev["erabp__stddev"]
      zteam.save()