from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
# is hard hit the same as ev95pluspercent???

class batter(models.Model):
  fangraphs_id = models.IntegerField(default="0")
  key_bbref = models.CharField(max_length=200, default="0")
  key_retro = models.CharField(max_length=200, default="0")
  key_mlbam = models.IntegerField(default="0")
  #the following variable will be used to assist in determining if a player's stats are either empty or loaded for a given year for fangraphs
  loaded_2022 = models.BooleanField(default=False)
  loaded_2021 = models.BooleanField(default=False)
  loaded_2020 = models.BooleanField(default=False)
  loaded_hr_per_fb2022 = models.BooleanField(default=False)
  loaded_hr_per_fb2021 = models.BooleanField(default=False)
  loaded_hr_per_fb2020 = models.BooleanField(default=False)
  lastname = models.CharField(max_length=200, default="BRATT")
  firstname = models.CharField(max_length=200, default="JESPER")
  teamname = models.CharField(max_length=3, default="---")
  pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  obp2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_obp2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  slg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_slg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ops2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bb_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_bb_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  k_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_k_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  r_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  rbi_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  gdp_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wRAA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wOBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  wRC2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_wRC2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iso2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_iso2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ld_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  gb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iffb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hr_per_fb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ld_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_gb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_fb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_hr_per_fb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  spd2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  clutch2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fwar2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  hardpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  plus_hardpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #barrel_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309 repetitive with baseball savant
  #maxEV2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  hardhitpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #xBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316 repetitive with baseball savant
  #fgxSLG2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317 repetitive with baseball savant
  #fgxWOBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318 repetitive with baseball savant xwoba
  fwar_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  outsidezoneswingpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  firstpitchstrikepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  swingcontactpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  swingingstrikespercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  foff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204 offense runs above average, batting + baserunning
  fdef2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200 defense runs above average
  foff_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fdef_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  ffld2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fldloaded_2022 = models.BooleanField(default=False) #to track if fielding data is available for the player (or, typically, if they are DH)
  fbat2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ffld_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbat_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  #z-score
  zpa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zobp2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_obp2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_slg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zops2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbb_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_bb_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zk_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_k_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zr_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrbi_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgdp_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwRAA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwOBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  zwRC2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_wRC2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziso2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_iso2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbabip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zld_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zgb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziffb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhr_per_fb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ld_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_gb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_fb_per_bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_hr_per_fb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zspd2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zclutch2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfwar2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  zhardpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  zplus_hardpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #zbarrel_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309 repetitive with baseball savant
  #zmaxEV2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zhardhitpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #zxBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316 repetitive with baseball savant
  #zfgxSLG2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317 repetitive with baseball savant
  #zfgxWOBA2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318 repetitive with baseball savant xwoba
  zfwar_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zoutsidezoneswingpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  zfirstpitchstrikepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  zswingcontactpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  zswingingstrikespercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  zfoff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204 offense runs above average, batting + baserunning
  zfdef2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200 defense runs above average
  zfoff_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfdef_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  zffld2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zffld_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment


  # 2021 DATA
  # follows below
  pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  obp2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_obp2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  slg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_slg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ops2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bb_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_bb_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  k_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_k_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  r_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  rbi_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  gdp_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wRAA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wOBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  wRC2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_wRC2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iso2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_iso2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ld_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  gb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iffb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hr_per_fb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ld_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_gb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_fb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_hr_per_fb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  spd2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  clutch2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fwar2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  hardpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  plus_hardpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #barrel_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  #maxEV2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  hardhitpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #xBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  #fgxSLG2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317
  #fgxWOBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318

  fwar_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  outsidezoneswingpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  firstpitchstrikepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  swingcontactpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  swingingstrikespercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  foff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204
  fdef2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200
  foff_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fdef_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ffld2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbat2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fldloaded_2021 = models.BooleanField(default=False) #to track if fielding data is available for the player (or, typically, if they are DH)
  ffld_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbat_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  #z-score
  zpa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zobp2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_obp2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_slg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zops2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbb_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_bb_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zk_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_k_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zr_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrbi_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgdp_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwRAA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwOBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  zwRC2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_wRC2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziso2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_iso2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbabip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zld_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziffb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhr_per_fb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ld_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_gb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_fb_per_bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_hr_per_fb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zspd2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zclutch2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfwar2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  
  zhardpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  zplus_hardpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #zbarrel_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309 repetitive with baseball savant
  #zmaxEV2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zhardhitpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #zxBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316 repetitive with baseball savant
  #zfgxSLG2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317 repetitive with baseball savant
  #zfgxWOBA2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318 repetitive with baseball savant xwoba
  zfwar_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zoutsidezoneswingpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  zfirstpitchstrikepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  zswingcontactpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  zswingingstrikespercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  zfoff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204 offense runs above average, batting + baserunning
  zfdef2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200 defense runs above average
  zfoff_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfdef_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  zffld2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zffld_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment



  # 2020 DATA
  # follows below
  pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  obp2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_obp2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  slg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_slg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ops2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bb_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_bb_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  k_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_k_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  r_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  rbi_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  gdp_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xSB_added_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wRAA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wOBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  wRC2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_wRC2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iso2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_iso2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ld_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  gb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iffb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hr_per_fb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ld_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_gb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_fb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_hr_per_fb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  spd2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  clutch2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fwar2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  hardpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  plus_hardpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #barrel_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  #maxEV2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  hardhitpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #xBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  #fgxSLG2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317
  #fgxWOBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318
  fwar_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bsr_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  outsidezoneswingpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  firstpitchstrikepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  swingcontactpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  swingingstrikespercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  foff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204
  fdef2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200
  foff_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fdef_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ffld2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbat2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fldloaded_2020 = models.BooleanField(default=False) #to track if fielding data is available for the player (or, typically, if they are DH)
  ffld_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbat_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  #z-score
  zpa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zobp2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_obp2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_slg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zops2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbb_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_bb_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zk_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_k_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zr_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrbi_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgdp_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxSB_added_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwRAA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwOBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # note: in the third column
  zwRC2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_wRC2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziso2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_iso2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbabip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zld_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziffb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhr_per_fb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ld_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_gb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_fb_per_bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_hr_per_fb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zspd2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zclutch2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfwar2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  
  zhardpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 212, criteria unclear
  zplus_hardpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305, criteria unclear
  #zbarrel_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309 repetitive with baseball savant
  #zmaxEV2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zhardhitpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  #zxBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316 repetitive with baseball savant
  #zfgxSLG2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 317 repetitive with baseball savant
  #zfgxWOBA2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 318 repetitive with baseball savant xwoba
  zfwar_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbsr_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zoutsidezoneswingpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 103
  zfirstpitchstrikepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 110
  zswingcontactpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 108
  zswingingstrikespercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 111
  zfoff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 204 offense runs above average, batting + baserunning
  zfdef2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 200 defense runs above average
  zfoff_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfdef_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment
  zffld2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zffld_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbat_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # fielding runs and positional adjustment


  # note: adding another year would take about five minutes and would just require copying and pasting the createbatter and models files, 
  # then doing control f to change the years, add in the loaded_year variable also, then migrate as usual and you are good to go

  # baseball reference data
  loaded_bref_2022 = models.BooleanField(default=False)
  loaded_bref_2021 = models.BooleanField(default=False)
  loaded_bref_2020 = models.BooleanField(default=False)

  #below is the 2022 baseball reference data
  bref_batting_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ops2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  bref_batting_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score
  zbref_batting_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zbref_runs_above_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ops2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  zbref_batting_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off_per_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)


  #below is the 2021 baseball reference data
  bref_batting_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ops2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  bref_batting_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score
  zbref_batting_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zbref_runs_above_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ops2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  zbref_batting_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off_per_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #below is the 2020 baseball reference data
  bref_batting_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ops2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  bref_batting_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_bsr_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_gdp_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_def_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_runs_above_avg_off_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_def_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bref_war_off_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score
  zbref_batting_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zbref_runs_above_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ops2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # per pa
  zbref_batting_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_bsr_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_gdp_runs_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_def_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_runs_above_avg_off_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_def_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbref_war_off_per_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #basball savant data
  loaded_bs_barrel_2022 = models.BooleanField(default=False)
  loaded_bs_barrel_2021 = models.BooleanField(default=False)
  loaded_bs_barrel_2020 = models.BooleanField(default=False)
  loaded_bs_x_2022 = models.BooleanField(default=False)
  loaded_bs_x_2021 = models.BooleanField(default=False)
  loaded_bs_x_2020 = models.BooleanField(default=False)

  #below is the 2022 baseball savant data
  bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwoba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwobadiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  anglesweetspotpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_hit_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_hit_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_distance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_distance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ev95percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score
  zbip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not using any of the diff stats
  zxslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxslgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwoba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwobadiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zanglesweetspotpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_hit_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_hit_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_distance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_distance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zev95percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_pa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #below is the 2021 baseball savant data
  bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwoba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwobadiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  anglesweetspotpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_hit_speed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_hit_speed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_distance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_distance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ev95percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
   #z-score
  zbip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not using any of the diff stats
  zxslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxslgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwoba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwobadiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zanglesweetspotpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_hit_speed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_hit_speed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_distance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_distance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zev95percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_pa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #below is the 2020 baseball savant data
  bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xavgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xslgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwoba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xwobadiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  anglesweetspotpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_hit_speed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_hit_speed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  max_distance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  avg_distance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ev95percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score
  zbip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxavgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not using any of the diff stats
  zxslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxslgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwoba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxwobadiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zanglesweetspotpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_hit_speed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_hit_speed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmax_distance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE: not being used
  zavg_distance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zev95percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_pa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0)


  #BAESBALL SAVANT 2022
  loaded_bs_fielding_2022 = models.BooleanField(default=False)
  # loaded_bs_fielding_2021 = models.BooleanField(default=False) need to be unblocked next time createbatter is run
  # loaded_bs_fielding_2020 = models.BooleanField(default=False)
  loaded_bs_running_2022 = models.BooleanField(default=False)
  #FIELDING
  outs_above_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  fielding_runs_prevented2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6
  zouts_above_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zfielding_runs_prevented2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6
  #BASERUNNING
  home_to_first2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  sprint_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 9
  zhome_to_first2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  zsprint_speed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 9
  #BAESBALL SAVANT 2021
  #FIELDING
  outs_above_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  fielding_runs_prevented2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6
  zouts_above_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zfielding_runs_prevented2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6
  #BAESBALL SAVANT 2020
  #FIELDING
  outs_above_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  fielding_runs_prevented2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6
  zouts_above_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zfielding_runs_prevented2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 6

  def __str__(self):
    self_title = self.lastname + ", " + self.firstname + ": " + self.teamname + "--- Fangraph's ID: " + str(self.fangraphs_id)
    return self_title

  #code here creates a dictionary of name of each zvariable to actual zvalue for the batter, to match dictionary used when user weights are collected with same key names in views.py by design
  def accesszbatter2022dict(self):
    zbatter2022dict = {
     "zpa":self.zpa2022,
     "zavg":self.zavg2022,
     "zplus_avg":self.zplus_avg2022,
     "zobp":self.zobp2022,
     "zplus_obp":self.zplus_obp2022,
     "zslg":self.zslg2022,
     "zplus_slg":self.zplus_slg2022,
     "zops":self.zops2022,
     "zbb_per_pa":self.zbb_per_pa2022,
     "zplus_bb_per_pa":self.zplus_bb_per_pa2022,
     "zk_per_pa":self.zk_per_pa2022,
     "zplus_k_per_pa":self.zplus_k_per_pa2022,
     "zr_per_pa":self.zr_per_pa2022,
     "zrbi_per_pa":self.zrbi_per_pa2022,
     "zgdp_per_pa":self.zgdp_per_pa2022,
     "zxSB_added":self.zxSB_added2022,
     "zxSB_added_percent":self.zxSB_added_percent2022,
     "zwRAA":self.zwRAA2022,
     "zwOBA":self.zwOBA2022,
     "zwRC":self.zwRC2022,
     "zplus_wRC":self.zplus_wRC2022,
     "ziso":self.ziso2022,
     "zplus_iso":self.zplus_iso2022,
     "zbabip":self.zbabip2022,
     "zplus_babip":self.zplus_babip2022,
     "zld_per_bip":self.zld_per_bip2022,
     "zgb_per_bip":self.zgb_per_bip2022,
     "zfb_per_bip":self.zfb_per_bip2022,
     "ziffb_per_bip":self.ziffb_per_bip2022,
     "zhr_per_fb":self.zhr_per_fb2022,
     "zplus_ld_per_bip":self.zplus_ld_per_bip2022,
     "zplus_gb_per_bip":self.zplus_gb_per_bip2022,
     "zplus_fb_per_bip":self.zplus_fb_per_bip2022,
     "zplus_hr_per_fb":self.zplus_hr_per_fb2022,
     "zspd":self.zspd2022,
     "zbsr":self.zbsr2022,
     "zclutch":self.zclutch2022,
     "zfwar":self.zfwar2022,
     "zhardpercent":self.zhardpercent2022,
     "zplus_hardpercent":self.zplus_hardpercent2022,
     "zhardhitpercent":self.zhardhitpercent2022,
     "zfwar_per_pa":self.zfwar_per_pa2022,
     "zbsr_per_pa":self.zbsr_per_pa2022,
     "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2022,
     "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2022,
     "zswingcontactpercent":self.zswingcontactpercent2022,
     "zswingingstrikespercent":self.zswingingstrikespercent2022,
     "zfoff":self.zfoff2022,
     "zfdef":self.zfdef2022,
     "zfoff_per_pa":self.zfoff_per_pa2022,
     "zfdef_per_pa":self.zfdef_per_pa2022,
     "zffld":self.zffld2022,
     "zfbat":self.zfbat2022,
     "zffld_per_pa":self.zffld_per_pa2022,
     "zfbat_per_pa":self.zfbat_per_pa2022,
     "zbref_batting_runs":self.zbref_batting_runs2022,
     "zbref_bsr_runs":self.zbref_bsr_runs2022,
     "zbref_gdp_runs":self.zbref_gdp_runs2022,
     "zbref_runs_above_avg":self.zbref_runs_above_avg2022,
     "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2022,
     "zbref_runs_above_avg_off":self.zbref_runs_above_avg_off2022,
     "zbref_war":self.zbref_war2022,
     "zbref_war_def":self.zbref_war_def2022,
     "zbref_war_off":self.zbref_war_off2022,
     "zplus_ops":self.zplus_ops2022,
     "zbref_batting_runs_per_pa":self.zbref_batting_runs_per_pa2022,
     "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2022,
     "zbref_gdp_runs_per_pa":self.zbref_gdp_runs_per_pa2022,
     "zbref_runs_above_avg_per_pa":self.zbref_runs_above_avg_per_pa2022,
     "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2022,
     "zbref_runs_above_avg_off_per_pa":self.zbref_runs_above_avg_off_per_pa2022,
     "zbref_war_per_pa":self.zbref_war_per_pa2022,
     "zbref_war_def_per_pa":self.zbref_war_def_per_pa2022,
     "zbref_war_off_per_pa":self.zbref_war_off_per_pa2022,
     "zbip":self.zbip2022,
     "zxavg":self.zxavg2022,
     "zxavgdiff":self.zxavgdiff2022,
     "zxslg":self.zxslg2022,
     "zxslgdiff":self.zxslgdiff2022,
     "zxwoba":self.zxwoba2022,
     "zxwobadiff":self.zxwobadiff2022,
     "zanglesweetspotpercent":self.zanglesweetspotpercent2022,
     "zmax_hit_speed":self.zmax_hit_speed2022,
     "zavg_hit_speed":self.zavg_hit_speed2022,
     "zmax_distance":self.zmax_distance2022,
     "zavg_distance":self.zavg_distance2022,
     "zev95percent":self.zev95percent2022,
     "zbrl_percent":self.zbrl_percent2022,
     "zbrl_pa":self.zbrl_pa2022,
     "zouts_above_avg":self.zouts_above_avg2022,
     "zfielding_runs_prevented":self.zfielding_runs_prevented2022,
     "zhome_to_first":self.zhome_to_first2022,
     "zsprint_speed":self.zsprint_speed2022
    }
    return zbatter2022dict
    #this will share key names with another four dictionaries (batting, running, fielding, general (then use position value to exclude dh from fielding and any other exclusions)) in views.py collected from the user, which will have name of each zvariable as keys and user provided weights as values

  def accesszbatter2021dict(self):
   zbatter2021dict = {
    "zpa":self.zpa2021,
    "zavg":self.zavg2021,
    "zplus_avg":self.zplus_avg2021,
    "zobp":self.zobp2021,
    "zplus_obp":self.zplus_obp2021,
    "zslg":self.zslg2021,
    "zplus_slg":self.zplus_slg2021,
    "zops":self.zops2021,
    "zbb_per_pa":self.zbb_per_pa2021,
    "zplus_bb_per_pa":self.zplus_bb_per_pa2021,
    "zk_per_pa":self.zk_per_pa2021,
    "zplus_k_per_pa":self.zplus_k_per_pa2021,
    "zr_per_pa":self.zr_per_pa2021,
    "zrbi_per_pa":self.zrbi_per_pa2021,
    "zgdp_per_pa":self.zgdp_per_pa2021,
    "zxSB_added":self.zxSB_added2021,
    "zxSB_added_percent":self.zxSB_added_percent2021,
    "zwRAA":self.zwRAA2021,
    "zwOBA":self.zwOBA2021,
    "zwRC":self.zwRC2021,
    "zplus_wRC":self.zplus_wRC2021,
    "ziso":self.ziso2021,
    "zplus_iso":self.zplus_iso2021,
    "zbabip":self.zbabip2021,
    "zplus_babip":self.zplus_babip2021,
    "zld_per_bip":self.zld_per_bip2021,
    "zgb_per_bip":self.zgb_per_bip2021,
    "zfb_per_bip":self.zfb_per_bip2021,
    "ziffb_per_bip":self.ziffb_per_bip2021,
    "zhr_per_fb":self.zhr_per_fb2021,
    "zplus_ld_per_bip":self.zplus_ld_per_bip2021,
    "zplus_gb_per_bip":self.zplus_gb_per_bip2021,
    "zplus_fb_per_bip":self.zplus_fb_per_bip2021,
    "zplus_hr_per_fb":self.zplus_hr_per_fb2021,
    "zspd":self.zspd2021,
    "zbsr":self.zbsr2021,
    "zclutch":self.zclutch2021,
    "zfwar":self.zfwar2021,
    "zhardpercent":self.zhardpercent2021,
    "zplus_hardpercent":self.zplus_hardpercent2021,
    "zhardhitpercent":self.zhardhitpercent2021,
    "zfwar_per_pa":self.zfwar_per_pa2021,
    "zbsr_per_pa":self.zbsr_per_pa2021,
    "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2021,
    "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2021,
    "zswingcontactpercent":self.zswingcontactpercent2021,
    "zswingingstrikespercent":self.zswingingstrikespercent2021,
    "zfoff":self.zfoff2021,
    "zfdef":self.zfdef2021,
    "zfoff_per_pa":self.zfoff_per_pa2021,
    "zfdef_per_pa":self.zfdef_per_pa2021,
    "zffld":self.zffld2021,
    "zfbat":self.zfbat2021,
    "zffld_per_pa":self.zffld_per_pa2021,
    "zfbat_per_pa":self.zfbat_per_pa2021,
    "zbref_batting_runs":self.zbref_batting_runs2021,
    "zbref_bsr_runs":self.zbref_bsr_runs2021,
    "zbref_gdp_runs":self.zbref_gdp_runs2021,
    "zbref_runs_above_avg":self.zbref_runs_above_avg2021,
    "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2021,
    "zbref_runs_above_avg_off":self.zbref_runs_above_avg_off2021,
    "zbref_war":self.zbref_war2021,
    "zbref_war_def":self.zbref_war_def2021,
    "zbref_war_off":self.zbref_war_off2021,
    "zplus_ops":self.zplus_ops2021,
    "zbref_batting_runs_per_pa":self.zbref_batting_runs_per_pa2021,
    "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2021,
    "zbref_gdp_runs_per_pa":self.zbref_gdp_runs_per_pa2021,
    "zbref_runs_above_avg_per_pa":self.zbref_runs_above_avg_per_pa2021,
    "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2021,
    "zbref_runs_above_avg_off_per_pa":self.zbref_runs_above_avg_off_per_pa2021,
    "zbref_war_per_pa":self.zbref_war_per_pa2021,
    "zbref_war_def_per_pa":self.zbref_war_def_per_pa2021,
    "zbref_war_off_per_pa":self.zbref_war_off_per_pa2021,
    "zbip":self.zbip2021,
    "zxavg":self.zxavg2021,
    "zxavgdiff":self.zxavgdiff2021,
    "zxslg":self.zxslg2021,
    "zxslgdiff":self.zxslgdiff2021,
    "zxwoba":self.zxwoba2021,
    "zxwobadiff":self.zxwobadiff2021,
    "zanglesweetspotpercent":self.zanglesweetspotpercent2021,
    "zmax_hit_speed":self.zmax_hit_speed2021,
    "zavg_hit_speed":self.zavg_hit_speed2021,
    "zmax_distance":self.zmax_distance2021,
    "zavg_distance":self.zavg_distance2021,
    "zev95percent":self.zev95percent2021,
    "zbrl_percent":self.zbrl_percent2021,
    "zbrl_pa":self.zbrl_pa2021,
    "zouts_above_avg":self.zouts_above_avg2021,
    "zfielding_runs_prevented":self.zfielding_runs_prevented2021,
   }
   return zbatter2021dict

  def accesszbatter2020dict(self):
    zbatter2020dict = {
      "zpa":self.zpa2020,
      "zavg":self.zavg2020,
      "zplus_avg":self.zplus_avg2020,
      "zobp":self.zobp2020,
      "zplus_obp":self.zplus_obp2020,
      "zslg":self.zslg2020,
      "zplus_slg":self.zplus_slg2020,
      "zops":self.zops2020,
      "zbb_per_pa":self.zbb_per_pa2020,
      "zplus_bb_per_pa":self.zplus_bb_per_pa2020,
      "zk_per_pa":self.zk_per_pa2020,
      "zplus_k_per_pa":self.zplus_k_per_pa2020,
      "zr_per_pa":self.zr_per_pa2020,
      "zrbi_per_pa":self.zrbi_per_pa2020,
      "zgdp_per_pa":self.zgdp_per_pa2020,
      "zxSB_added":self.zxSB_added2020,
      "zxSB_added_percent":self.zxSB_added_percent2020,
      "zwRAA":self.zwRAA2020,
      "zwOBA":self.zwOBA2020,
      "zwRC":self.zwRC2020,
      "zplus_wRC":self.zplus_wRC2020,
      "ziso":self.ziso2020,
      "zplus_iso":self.zplus_iso2020,
      "zbabip":self.zbabip2020,
      "zplus_babip":self.zplus_babip2020,
      "zld_per_bip":self.zld_per_bip2020,
      "zgb_per_bip":self.zgb_per_bip2020,
      "zfb_per_bip":self.zfb_per_bip2020,
      "ziffb_per_bip":self.ziffb_per_bip2020,
      "zhr_per_fb":self.zhr_per_fb2020,
      "zplus_ld_per_bip":self.zplus_ld_per_bip2020,
      "zplus_gb_per_bip":self.zplus_gb_per_bip2020,
      "zplus_fb_per_bip":self.zplus_fb_per_bip2020,
      "zplus_hr_per_fb":self.zplus_hr_per_fb2020,
      "zspd":self.zspd2020,
      "zbsr":self.zbsr2020,
      "zclutch":self.zclutch2020,
      "zfwar":self.zfwar2020,
      "zhardpercent":self.zhardpercent2020,
      "zplus_hardpercent":self.zplus_hardpercent2020,
      "zhardhitpercent":self.zhardhitpercent2020,
      "zfwar_per_pa":self.zfwar_per_pa2020,
      "zbsr_per_pa":self.zbsr_per_pa2020,
      "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2020,
      "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2020,
      "zswingcontactpercent":self.zswingcontactpercent2020,
      "zswingingstrikespercent":self.zswingingstrikespercent2020,
      "zfoff":self.zfoff2020,
      "zfdef":self.zfdef2020,
      "zfoff_per_pa":self.zfoff_per_pa2020,
      "zfdef_per_pa":self.zfdef_per_pa2020,
      "zffld":self.zffld2020,
      "zfbat":self.zfbat2020,
      "zffld_per_pa":self.zffld_per_pa2020,
      "zfbat_per_pa":self.zfbat_per_pa2020,
      "zbref_batting_runs":self.zbref_batting_runs2020,
      "zbref_bsr_runs":self.zbref_bsr_runs2020,
      "zbref_gdp_runs":self.zbref_gdp_runs2020,
      "zbref_runs_above_avg":self.zbref_runs_above_avg2020,
      "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2020,
      "zbref_runs_above_avg_off":self.zbref_runs_above_avg_off2020,
      "zbref_war":self.zbref_war2020,
      "zbref_war_def":self.zbref_war_def2020,
      "zbref_war_off":self.zbref_war_off2020,
      "zplus_ops":self.zplus_ops2020,
      "zbref_batting_runs_per_pa":self.zbref_batting_runs_per_pa2020,
      "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2020,
      "zbref_gdp_runs_per_pa":self.zbref_gdp_runs_per_pa2020,
      "zbref_runs_above_avg_per_pa":self.zbref_runs_above_avg_per_pa2020,
      "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2020,
      "zbref_runs_above_avg_off_per_pa":self.zbref_runs_above_avg_off_per_pa2020,
      "zbref_war_per_pa":self.zbref_war_per_pa2020,
      "zbref_war_def_per_pa":self.zbref_war_def_per_pa2020,
      "zbref_war_off_per_pa":self.zbref_war_off_per_pa2020,
      "zbip":self.zbip2020,
      "zxavg":self.zxavg2020,
      "zxavgdiff":self.zxavgdiff2020,
      "zxslg":self.zxslg2020,
      "zxslgdiff":self.zxslgdiff2020,
      "zxwoba":self.zxwoba2020,
      "zxwobadiff":self.zxwobadiff2020,
      "zanglesweetspotpercent":self.zanglesweetspotpercent2020,
      "zmax_hit_speed":self.zmax_hit_speed2020,
      "zavg_hit_speed":self.zavg_hit_speed2020,
      "zmax_distance":self.zmax_distance2020,
      "zavg_distance":self.zavg_distance2020,
      "zev95percent":self.zev95percent2020,
      "zbrl_percent":self.zbrl_percent2020,
      "zbrl_pa":self.zbrl_pa2020,
      "zouts_above_avg":self.zouts_above_avg2020,
      "zfielding_runs_prevented":self.zfielding_runs_prevented2020,
    }
    return zbatter2020dict
  
  def accesszfielder2022dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zfielder2022dict = {
      "zouts_above_avg":self.zouts_above_avg2022,
      "zfielding_runs_prevented":self.zfielding_runs_prevented2022,
      "zfdef":self.zfdef2022,
      "zfdef_per_pa":self.zfdef_per_pa2022,
      "zffld":self.zffld2022,
      "zffld_per_pa":self.zffld_per_pa2022,
      "zbref_war_def":self.zbref_war_def2022,
      "zbref_war_def_per_pa":self.zbref_war_def_per_pa2022,
      "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2022,
      "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2022,
    }
    return zfielder2022dict

  def accesszfielder2021dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zfielder2021dict = {
      "zouts_above_avg":self.zouts_above_avg2021,
      "zfielding_runs_prevented":self.zfielding_runs_prevented2021,
      "zfdef":self.zfdef2021,
      "zfdef_per_pa":self.zfdef_per_pa2021,
      "zffld":self.zffld2021,
      "zffld_per_pa":self.zffld_per_pa2021,
      "zbref_war_def":self.zbref_war_def2021,
      "zbref_war_def_per_pa":self.zbref_war_def_per_pa2021,
      "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2021,
      "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2021,
    }
    return zfielder2021dict

  def accesszfielder2020dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zfielder2020dict = {
    "zouts_above_avg":self.zouts_above_avg2020,
    "zfielding_runs_prevented":self.zfielding_runs_prevented2020,
    "zfdef":self.zfdef2020,
    "zfdef_per_pa":self.zfdef_per_pa2020,
    "zffld":self.zffld2020,
    "zffld_per_pa":self.zffld_per_pa2020,
    "zbref_war_def":self.zbref_war_def2020,
    "zbref_war_def_per_pa":self.zbref_war_def_per_pa2020,
    "zbref_runs_above_avg_def":self.zbref_runs_above_avg_def2020,
    "zbref_runs_above_avg_def_per_pa":self.zbref_runs_above_avg_def_per_pa2020,
  }
    return zfielder2020dict

  def accesszbaserunner2022dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zbaserunner2022dict = {
      "zhome_to_first":self.zhome_to_first2022,
      "zsprint_speed":self.zsprint_speed2022,
      "zspd":self.zspd2022,
      "zxSB_added":self.zxSB_added2022,
      "zxSB_added_percent":self.zxSB_added_percent2022,
      "zbsr":self.zbsr2022,
      "zbsr_per_pa":self.zbsr_per_pa2022,
      "zbref_bsr_runs":self.zbref_bsr_runs2022,
      "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2022,
    }
    return zbaserunner2022dict

  def accesszbaserunner2021dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zbaserunner2021dict = {
      "zhome_to_first":self.zhome_to_first2021,
      "zsprint_speed":self.zsprint_speed2021,
      "zspd":self.zspd2021,
      "zxSB_added":self.zxSB_added2021,
      "zxSB_added_percent":self.zxSB_added_percent2021,
      "zbsr":self.zbsr2021,
      "zbsr_per_pa":self.zbsr_per_pa2021,
      "zbref_bsr_runs":self.zbref_bsr_runs2021,
      "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2021,
    }
    return zbaserunner2021dict
  
  def accesszbaserunner2020dict(self):
    #NOTE: this may not be the complete list of defense statistics
    zbaserunner2020dict = {
      "zhome_to_first":self.zhome_to_first2020,
      "zsprint_speed":self.zsprint_speed2020,
      "zspd":self.zspd2020,
      "zxSB_added":self.zxSB_added2020,
      "zxSB_added_percent":self.zxSB_added_percent2020,
      "zbsr":self.zbsr2020,
      "zbsr_per_pa":self.zbsr_per_pa2020,
      "zbref_bsr_runs":self.zbref_bsr_runs2020,
      "zbref_bsr_runs_per_pa":self.zbref_bsr_runs_per_pa2020,
    }
    return zbaserunner2020dict

  class Admin:
      pass



class pitcher(models.Model):
  #season in column 1
  fangraphs_id = models.IntegerField(default="0") #column 0
  key_bbref = models.CharField(max_length=200, default="0")
  key_retro = models.CharField(max_length=200, default="0")
  key_mlbam = models.IntegerField(default="0") # tried making the primary key but it causd an error
  lastname = models.CharField(max_length=200, default="BRATT") #column 2 is name
  firstname = models.CharField(max_length=200, default="JESPER")
  teamname = models.CharField(max_length=3, default="---")
  #the following variable will be used to assist in determining if a player's stats are either empty or loaded for a given year for fangraphs
  loaded_2022 = models.BooleanField(default=False)
  loaded_2021 = models.BooleanField(default=False)
  loaded_2020 = models.BooleanField(default=False)

  loaded_k_per_bb2022 = models.BooleanField(default=False)
  loaded_k_per_bb2021 = models.BooleanField(default=False)
  loaded_k_per_bb2020 = models.BooleanField(default=False)

  loaded_hrperfb2022 = models.BooleanField(default=False)
  loaded_hrperfb2021 = models.BooleanField(default=False)
  loaded_hrperfb2020 = models.BooleanField(default=False)

  # 2022 stats
  winningpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  war2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  era2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  shutouts2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  saves2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  savepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  innings2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  battersfaced2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  hits2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #hitpercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  runs2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #runspercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  runsaverage2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #earnedrunspercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  homeruns2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  bbhbp2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #bbhbppercentinning2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  k2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  thrownforkpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  kpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  bbpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  hitpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  hrpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  kperbb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  whip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  lobpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  hrperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  fip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  gbperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  gbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  iffbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  ldpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  fbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  rar2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  tera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  xfip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  wpa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  retwentyfour2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  clutch2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  outsidezoneswingpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  firstpitchstrikepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  swingingstrikespercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114
  shutdowns2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116
  meltdowns2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117
  eraminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  fipminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  xfipminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  bbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  cswpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  softpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  mediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  softplusmediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  kwera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  kpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  weakpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs
  siera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  plus_k_per_nine2022= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  plus_bb_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  plus_k_per_bb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  plus_h_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  plus_hr_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  plus_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  plus_whip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  plus_babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  plus_lobpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  plus_kpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  plus_bbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  plus_ldpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  plus_gbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  plus_hrperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  plus_softpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  plus_mediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  barrel_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  hardhitpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  averageev2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  averagela2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  xera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333

  # z-score 2022 stats
  zwinningpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  zwar2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  zshutouts2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  zsaves2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  zsavepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  zinnings2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  zbattersfaced2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  zhits2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #zhitpercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  zruns2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #zrunspercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  zrunsaverage2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #zearnedrunspercentbatter2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  zhomeruns2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  zbbhbp2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #zbbhbppercentinning2022  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  zk2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  zthrownforkpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  zkpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  zbbpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  zhitpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  zhrpernine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  zkperbb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  zavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  zwhip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  zbabip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  zlobpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  zhrperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  zfip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  zgbperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  zgbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  ziffbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  zldpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  zfbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  zrar2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  ztera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  zxfip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  zwpa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  zretwentyfour2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  zclutch2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  zoutsidezoneswingpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  zfirstpitchstrikepercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  zswingingstrikespercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114

  zshutdowns2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116
  zmeltdowns2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117
  zeraminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  zfipminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  zxfipminus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  zbbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  zcswpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  zsoftpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  zmediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  zsoftplusmediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  zkwera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  zkpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  zweakpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs
  zsiera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  zplus_k_per_nine2022= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  zplus_bb_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  zplus_k_per_bb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  zplus_h_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  zplus_hr_per_nine2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  zplus_avg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  zplus_whip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  zplus_babip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  zplus_lobpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zplus_kpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  zplus_bbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  zplus_ldpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  zplus_gbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  zplus_hrperfb2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  zplus_softpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  zplus_mediumpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  zbarrel_percent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  zhardhitpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  zaverageev2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  zaveragela2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  zxera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333


  # 2021 stats
  winningpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  war2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  era2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  shutouts2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  saves2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  savepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  innings2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  battersfaced2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  hits2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #hitpercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  runs2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #runspercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  runsaverage2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #earnedrunspercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  homeruns2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  bbhbp2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #bbhbppercentinning2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  k2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  thrownforkpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  kpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  bbpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  hitpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  hrpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  kperbb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  whip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  lobpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  hrperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  fip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  gbperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  gbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  iffbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  ldpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  fbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  rar2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  tera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  xfip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  wpa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  retwentyfour2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  clutch2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  outsidezoneswingpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  firstpitchstrikepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  swingingstrikespercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114
  shutdowns2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116 / figure out percent
  meltdowns2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117 / figure out percent
  eraminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  fipminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  xfipminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  bbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  cswpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  softpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  mediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  softplusmediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  kwera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  kpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  weakpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb + gb
  siera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  plus_k_per_nine2021= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  plus_bb_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  plus_k_per_bb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  plus_h_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  plus_hr_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  plus_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  plus_whip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  plus_babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  plus_lobpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  plus_kpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  plus_bbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  plus_ldpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  plus_gbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  plus_hrperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  plus_softpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  plus_mediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  barrel_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  hardhitpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  averageev2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  averagela2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  xera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333

  # z-score 2021 stats
  zwinningpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  zwar2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  zshutouts2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  zsaves2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  zsavepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  zinnings2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  zbattersfaced2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  zhits2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #zhitpercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  zruns2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #zrunspercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  zrunsaverage2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #zearnedrunspercentbatter2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  zhomeruns2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  zbbhbp2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #zbbhbppercentinning2021  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  zk2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  zthrownforkpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  zkpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  zbbpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  zhitpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  zhrpernine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  zkperbb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  zavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  zwhip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  zbabip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  zlobpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  zhrperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  zfip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  zgbperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  zgbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  ziffbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  zldpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  zfbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  zrar2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  ztera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  zxfip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  zwpa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  zretwentyfour2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  zclutch2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  zoutsidezoneswingpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  zfirstpitchstrikepercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  zswingingstrikespercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114
  
  zshutdowns2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116
  zmeltdowns2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117
  zeraminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  zfipminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  zxfipminus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  zbbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  zcswpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  zsoftpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  zmediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  zsoftplusmediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  zkwera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  zkpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  zweakpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs
  zsiera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  zplus_k_per_nine2021= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  zplus_bb_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  zplus_k_per_bb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  zplus_h_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  zplus_hr_per_nine2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  zplus_avg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  zplus_whip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  zplus_babip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  zplus_lobpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zplus_kpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  zplus_bbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  zplus_ldpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  zplus_gbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  zplus_hrperfb2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  zplus_softpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  zplus_mediumpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  zbarrel_percent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  zhardhitpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  zaverageev2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  zaveragela2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  zxera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333


  # 2020 stats
  winningpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  war2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  era2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  shutouts2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  saves2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  savepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  innings2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  battersfaced2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  hits2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #hitpercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  runs2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #runspercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  runsaverage2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #earnedrunspercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  homeruns2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  bbhbp2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #bbhbppercentinning2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  k2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  thrownforkpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  kpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  bbpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  hitpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  hrpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  kperbb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  whip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  lobpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  hrperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  fip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  gbperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  gbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  iffbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  ldpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  fbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  rar2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  tera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  xfip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  wpa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  retwentyfour2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  clutch2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  outsidezoneswingpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  firstpitchstrikepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  swingingstrikespercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114
  shutdowns2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116 / figure out percent
  meltdowns2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117 / figure out percent
  eraminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  fipminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  xfipminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  bbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  cswpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  softpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  mediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  softplusmediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  kwera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  kpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  weakpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb + gb
  siera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  plus_k_per_nine2020= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  plus_bb_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  plus_k_per_bb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  plus_h_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  plus_hr_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  plus_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  plus_whip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  plus_babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  plus_lobpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  plus_kpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  plus_bbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  plus_ldpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  plus_gbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  plus_hrperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  plus_softpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  plus_mediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  barrel_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  hardhitpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  averageev2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  averagela2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  xera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333

  # z-score 2020 stats
  zwinningpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 5 / column 6
  zwar2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 7
  zera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 8
  zshutouts2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 12
  zsaves2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 13
  zsavepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 14
  zinnings2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 15
  zbattersfaced2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 16
  zhits2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17
  #zhitpercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 17 / column 16
  zruns2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18
  #zrunspercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 18 / column 16
  zrunsaverage2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 18 * 9) / column 15
  #zearnedrunspercentbatter2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 19 / column 16
  zhomeruns2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 20
  zbbhbp2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 21 + column 23, does not include intentional
  #zbbhbppercentinning2020  = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #(column 21 + column 23) / column 15
  zk2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 26
  zthrownforkpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 32 / column 33 includes foul balls
  zkpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 38
  zbbpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 39
  zhitpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 41
  zhrpernine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 42
  zkperbb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 40
  zavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 43
  zwhip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 44
  zbabip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 45
  zlobpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 46 percent of pitcher's own runners they leave on base
  zhrperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 53
  zfip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 47
  zgbperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 48
  zgbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 50
  ziffbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 52
  zldpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 49
  zfbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 51
  zrar2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 60 based on FIP
  ztera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 62 tERA true runs allowed
  zxfip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 63
  zwpa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 64
  zretwentyfour2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 67
  zclutch2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 75
  zoutsidezoneswingpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 106
  zfirstpitchstrikepercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 113
  zswingingstrikespercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 114
  
  zshutdowns2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 116
  zmeltdowns2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 117
  zeraminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 118
  zfipminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 119
  zxfipminus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 120
  zbbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 122
  zcswpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 332 does not include foul balls
  zsoftpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222
  zmediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 223
  zsoftplusmediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 222 + column 223
  zkwera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 225 era based on walks/strikeouts
  zkpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 121
  zweakpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs
  zsiera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #column 123
  zplus_k_per_nine2020= models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 302
  zplus_bb_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 303
  zplus_k_per_bb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 304
  zplus_h_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 305
  zplus_hr_per_nine2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 306
  zplus_avg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 307
  zplus_whip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 308
  zplus_babip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 309
  zplus_lobpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 310
  zplus_kpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 311
  zplus_bbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 312
  zplus_ldpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 313
  zplus_gbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 314
  zplus_hrperfb2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 316
  zplus_softpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 320, criteria unclear
  zplus_mediumpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 321, criteria unclear
  zbarrel_percent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 326
  zhardhitpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 329
  zaverageev2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 323
  zaveragela2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 324
  zxera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 333


  # skip bref for now

  #baseball savant
  #basball savant data
  loaded_bs_barrel_2022 = models.BooleanField(default=False)
  loaded_bs_barrel_2021 = models.BooleanField(default=False)
  loaded_bs_barrel_2020 = models.BooleanField(default=False)
  loaded_bs_x_2022 = models.BooleanField(default=False)
  loaded_bs_x_2021 = models.BooleanField(default=False)
  loaded_bs_x_2020 = models.BooleanField(default=False)

  # 2022 barrel
  bbevents2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #avghitangle2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4, repetitive with averagela from fangraphs
  anglesweetspotpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #anglehitspeed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7 repetitive with average ev from fangraphs
  #bsgbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3 not sure what is going wrong with this stat but it does not line up with fangraphs at all
  avgdistance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  ev95plus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 this is a total event, so not immediately useful
  ev95pluspercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #brlpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs barrel percent
  brlperpa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17
  #z-score barrel
  zbbevents2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #zavghitangle2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4, repetitive with averagela from fangraphs
  zanglesweetspotpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #zanglehitspeed2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7 repetitive with average ev from fangraphs
  #zbsgbpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3 not sure what is going wrong with this stat but it does not line up with fangraphs at all
  zavgdistance2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zev95plus2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 this is a total event, so not immediately useful
  zev95pluspercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbrlpercent2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs barrel percent
  zbrlperpa2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17

  # 2021 barrel
  bbevents2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #avghitangle2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4
  anglesweetspotpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #anglehitspeed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  #bsgbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3
  avgdistance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  ev95plus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 ? just confirm these are total events
  ev95pluspercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #brlpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16
  brlperpa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17
  #z-score barrel
  zbbevents2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #zavghitangle2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4, repetitive with averagela from fangraphs
  zanglesweetspotpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #zanglehitspeed2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7 repetitive with average ev from fangraphs
  #zbsgbpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3 not sure what is going wrong with this stat but it does not line up with fangraphs at all
  zavgdistance2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zev95plus2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 this is a total event, so not immediately useful
  zev95pluspercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbrlpercent2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs barrel percent
  zbrlperpa2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17

   # 2020
  bbevents2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #avghitangle2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4
  anglesweetspotpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #anglehitspeed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  #bsgbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3
  avgdistance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  ev95plus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 ? just confirm these are total events
  ev95pluspercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #brlpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16
  brlperpa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17
  #z-score barrel
  zbbevents2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 3, batted ball events
  #zavghitangle2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 4, repetitive with averagela from fangraphs
  zanglesweetspotpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  #zanglehitspeed2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7 repetitive with average ev from fangraphs
  #zbsgbpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9 / column 3 not sure what is going wrong with this stat but it does not line up with fangraphs at all
  zavgdistance2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zev95plus2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13 this is a total event, so not immediately useful
  zev95pluspercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbrlpercent2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs barrel percent
  zbrlperpa2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17


  #below is the 2022 expected baseball savant data
  bip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  xavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  xavgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  slg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  xslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  xslgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  woba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  xwoba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  xwobadiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #bsera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15 works fine, but no reason to double count when fangraphs era was already pulled
  #bsxera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs xera
  xeradiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly
  # z-score 2022 expected
  zbip2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  zxavg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  zxavgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  zslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  zxslg2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  zxslgdiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zwoba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  zxwoba2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  zxwobadiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbsera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15 works fine, but no reason to double count when fangraphs era was already pulled
  #zbsxera2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs xera
  zxeradiff2022 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly

  #below is the 2021 expected baseball savant data
  bip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  xavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  xavgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  slg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  xslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  xslgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  woba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  xwoba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  xwobadiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #bsera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15
  #bsxera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16
  xeradiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly
  # z-score 2021 expected
  zbip2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  zxavg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  zxavgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  zslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  zxslg2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  zxslgdiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zwoba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  zxwoba2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  zxwobadiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbsera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15 works fine, but no reason to double count when fangraphs era was already pulled
  #zbsxera2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs xera
  zxeradiff2021 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly

  #below is the 2020 expected baseball savant data
  bip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  xavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  xavgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  slg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  xslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  xslgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  woba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  xwoba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  xwobadiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #bsera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15
  #bsxera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16
  xeradiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly
  # z-score 2020 expected
  zbip2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 5
  zxavg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 7
  zxavgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 8
  zslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 9
  zxslg2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 10
  zxslgdiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 11
  zwoba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 12
  zxwoba2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 13
  zxwobadiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 14
  #zbsera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 15 works fine, but no reason to double count when fangraphs era was already pulled
  #zbsxera2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 16 repetitive with fangraphs xera
  zxeradiff2020 = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # column 17, doesn't seem to work correctly
  
  def __str__(self):
    self_title = self.lastname + ", " + self.firstname + ": " + self.teamname + "--- Fangraph's ID: " + str(self.fangraphs_id)
    return self_title

  def accesszpitcher2022dict(self):
    zpitcher2022dict = {
     "zwinningpercent":self.zwinningpercent2022,
     "zwar":self.zwar2022,
     "zera":self.zera2022,
     "zshutouts":self.zshutouts2022,
     "zsaves":self.zsaves2022,
     "zsavepercent":self.zsavepercent2022,
     "zinnings":self.zinnings2022,
     "zbattersfaced2022 ":self.zbattersfaced2022,
     "zhits":self.zhits2022,
     "zruns":self.zruns2022,
     "zrunsaverage":self.zrunsaverage2022,
     "zhomeruns":self.zhomeruns2022,
     "zbbhbp":self.zbbhbp2022,
     "zk":self.zk2022,
     "zthrownforkpercent":self.zthrownforkpercent2022,
     "zkpernine":self.zkpernine2022,
     "zbbpernine":self.zbbpernine2022,
     "zhitpernine":self.zhitpernine2022,
     "zhrpernine":self.zhrpernine2022,
     "zkperbb":self.zkperbb2022,
     "zavg":self.zavg2022,
     "zwhip":self.zwhip2022,
     "zbabip":self.zbabip2022,
     "zlobpercent":self.zlobpercent2022,
     "zhrperfb":self.zhrperfb2022,
     "zfip":self.zfip2022,
     "zgbperfb":self.zgbperfb2022,
     "zgbpercent":self.zgbpercent2022,
     "ziffbpercent":self.ziffbpercent2022,
     "zldpercent":self.zldpercent2022,
     "zfbpercent":self.zfbpercent2022,
     "zrar":self.zrar2022,
     "ztera":self.ztera2022,
     "zxfip":self.zxfip2022,
     "zwpa":self.zwpa2022,
     "zretwentyfour":self.zretwentyfour2022,
     "zclutch":self.zclutch2022,
     "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2022,
     "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2022,
     "zswingingstrikespercent":self.zswingingstrikespercent2022,
     "zshutdowns":self.zshutdowns2022,
     "zmeltdowns":self.zmeltdowns2022,
     "zeraminus":self.zeraminus2022,
     "zfipminus":self.zfipminus2022,
     "zxfipminus":self.zxfipminus2022,
     "zbbpercent":self.zbbpercent2022,
     "zcswpercent":self.zcswpercent2022,
     "zsoftpercent":self.zsoftpercent2022,
     "zmediumpercent":self.zmediumpercent2022,
     "zsoftplusmediumpercent":self.zsoftplusmediumpercent2022,
     "zkwera":self.zkwera2022,
     "zkpercent":self.zkpercent2022,
     "zweakpercent":self.zweakpercent2022,
     "zsiera":self.zsiera2022,
     "zplus_k_per_nine":self.zplus_k_per_nine2022,
     "zplus_bb_per_nine":self.zplus_bb_per_nine2022,
     "zplus_k_per_bb":self.zplus_k_per_bb2022,
     "zplus_h_per_nine":self.zplus_h_per_nine2022,
     "zplus_hr_per_nine":self.zplus_hr_per_nine2022,
     "zplus_avg":self.zplus_avg2022,
     "zplus_whip":self.zplus_whip2022,
     "zplus_babip":self.zplus_babip2022,
     "zplus_lobpercent":self.zplus_lobpercent2022,
     "zplus_kpercent":self.zplus_kpercent2022,
     "zplus_bbpercent":self.zplus_bbpercent2022,
     "zplus_ldpercent":self.zplus_ldpercent2022,
     "zplus_gbpercent":self.zplus_gbpercent2022,
     "zplus_hrperfb":self.zplus_hrperfb2022,
     "zplus_softpercent":self.zplus_softpercent2022,
     "zplus_mediumpercent":self.zplus_mediumpercent2022,
     "zbarrel_percent":self.zbarrel_percent2022,
     "zhardhitpercent":self.zhardhitpercent2022,
     "zaverageev":self.zaverageev2022,
     "zaveragela":self.zaveragela2022,
     "zxera":self.zxera2022,
     "zbbevents":self.zbbevents2022,
     "zanglesweetspotpercent":self.zanglesweetspotpercent2022,
     "zavgdistance":self.zavgdistance2022,
     "zev95plus":self.zev95plus2022,
     "zev95pluspercent":self.zev95pluspercent2022,
     "zbrlperpa":self.zbrlperpa2022,
     "zbip":self.zbip2022,
     "zxavg":self.zxavg2022,
     "zxavgdiff":self.zxavgdiff2022,
     "zslg":self.zslg2022,
     "zxslg":self.zxslg2022,
     "zxslgdiff":self.zxslgdiff2022,
     "zwoba":self.zwoba2022,
     "zxwoba":self.zxwoba2022,
     "zxwobadiff":self.zxwobadiff2022,
     "zxeradiff":self.zxeradiff2022
    }
    return zpitcher2022dict

  def accesszpitcher2021dict(self):
   zpitcher2021dict = {
    "zwinningpercent":self.zwinningpercent2021,
    "zwar":self.zwar2021,
    "zera":self.zera2021,
    "zshutouts":self.zshutouts2021,
    "zsaves":self.zsaves2021,
    "zsavepercent":self.zsavepercent2021,
    "zinnings":self.zinnings2021,
    "zbattersfaced2021 ":self.zbattersfaced2021,
    "zhits":self.zhits2021,
    "zruns":self.zruns2021,
    "zrunsaverage":self.zrunsaverage2021,
    "zhomeruns":self.zhomeruns2021,
    "zbbhbp":self.zbbhbp2021,
    "zk":self.zk2021,
    "zthrownforkpercent":self.zthrownforkpercent2021,
    "zkpernine":self.zkpernine2021,
    "zbbpernine":self.zbbpernine2021,
    "zhitpernine":self.zhitpernine2021,
    "zhrpernine":self.zhrpernine2021,
    "zkperbb":self.zkperbb2021,
    "zavg":self.zavg2021,
    "zwhip":self.zwhip2021,
    "zbabip":self.zbabip2021,
    "zlobpercent":self.zlobpercent2021,
    "zhrperfb":self.zhrperfb2021,
    "zfip":self.zfip2021,
    "zgbperfb":self.zgbperfb2021,
    "zgbpercent":self.zgbpercent2021,
    "ziffbpercent":self.ziffbpercent2021,
    "zldpercent":self.zldpercent2021,
    "zfbpercent":self.zfbpercent2021,
    "zrar":self.zrar2021,
    "ztera":self.ztera2021,
    "zxfip":self.zxfip2021,
    "zwpa":self.zwpa2021,
    "zretwentyfour":self.zretwentyfour2021,
    "zclutch":self.zclutch2021,
    "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2021,
    "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2021,
    "zswingingstrikespercent":self.zswingingstrikespercent2021,
    "zshutdowns":self.zshutdowns2021,
    "zmeltdowns":self.zmeltdowns2021,
    "zeraminus":self.zeraminus2021,
    "zfipminus":self.zfipminus2021,
    "zxfipminus":self.zxfipminus2021,
    "zbbpercent":self.zbbpercent2021,
    "zcswpercent":self.zcswpercent2021,
    "zsoftpercent":self.zsoftpercent2021,
    "zmediumpercent":self.zmediumpercent2021,
    "zsoftplusmediumpercent":self.zsoftplusmediumpercent2021,
    "zkwera":self.zkwera2021,
    "zkpercent":self.zkpercent2021,
    "zweakpercent":self.zweakpercent2021,
    "zsiera":self.zsiera2021,
    "zplus_k_per_nine":self.zplus_k_per_nine2021,
    "zplus_bb_per_nine":self.zplus_bb_per_nine2021,
    "zplus_k_per_bb":self.zplus_k_per_bb2021,
    "zplus_h_per_nine":self.zplus_h_per_nine2021,
    "zplus_hr_per_nine":self.zplus_hr_per_nine2021,
    "zplus_avg":self.zplus_avg2021,
    "zplus_whip":self.zplus_whip2021,
    "zplus_babip":self.zplus_babip2021,
    "zplus_lobpercent":self.zplus_lobpercent2021,
    "zplus_kpercent":self.zplus_kpercent2021,
    "zplus_bbpercent":self.zplus_bbpercent2021,
    "zplus_ldpercent":self.zplus_ldpercent2021,
    "zplus_gbpercent":self.zplus_gbpercent2021,
    "zplus_hrperfb":self.zplus_hrperfb2021,
    "zplus_softpercent":self.zplus_softpercent2021,
    "zplus_mediumpercent":self.zplus_mediumpercent2021,
    "zbarrel_percent":self.zbarrel_percent2021,
    "zhardhitpercent":self.zhardhitpercent2021,
    "zaverageev":self.zaverageev2021,
    "zaveragela":self.zaveragela2021,
    "zxera":self.zxera2021,
    "zbbevents":self.zbbevents2021,
    "zanglesweetspotpercent":self.zanglesweetspotpercent2021,
    "zavgdistance":self.zavgdistance2021,
    "zev95plus":self.zev95plus2021,
    "zev95pluspercent":self.zev95pluspercent2021,
    "zbrlperpa":self.zbrlperpa2021,
    "zbip":self.zbip2021,
    "zxavg":self.zxavg2021,
    "zxavgdiff":self.zxavgdiff2021,
    "zslg":self.zslg2021,
    "zxslg":self.zxslg2021,
    "zxslgdiff":self.zxslgdiff2021,
    "zwoba":self.zwoba2021,
    "zxwoba":self.zxwoba2021,
    "zxwobadiff":self.zxwobadiff2021,
    "zxeradiff":self.zxeradiff2021
   }
   return zpitcher2021dict

  def accesszpitcher2020dict(self):
   zpitcher2020dict = {
    "zwinningpercent":self.zwinningpercent2020,
    "zwar":self.zwar2020,
    "zera":self.zera2020,
    "zshutouts":self.zshutouts2020,
    "zsaves":self.zsaves2020,
    "zsavepercent":self.zsavepercent2020,
    "zinnings":self.zinnings2020,
    "zbattersfaced2020 ":self.zbattersfaced2020,
    "zhits":self.zhits2020,
    "zruns":self.zruns2020,
    "zrunsaverage":self.zrunsaverage2020,
    "zhomeruns":self.zhomeruns2020,
    "zbbhbp":self.zbbhbp2020,
    "zk":self.zk2020,
    "zthrownforkpercent":self.zthrownforkpercent2020,
    "zkpernine":self.zkpernine2020,
    "zbbpernine":self.zbbpernine2020,
    "zhitpernine":self.zhitpernine2020,
    "zhrpernine":self.zhrpernine2020,
    "zkperbb":self.zkperbb2020,
    "zavg":self.zavg2020,
    "zwhip":self.zwhip2020,
    "zbabip":self.zbabip2020,
    "zlobpercent":self.zlobpercent2020,
    "zhrperfb":self.zhrperfb2020,
    "zfip":self.zfip2020,
    "zgbperfb":self.zgbperfb2020,
    "zgbpercent":self.zgbpercent2020,
    "ziffbpercent":self.ziffbpercent2020,
    "zldpercent":self.zldpercent2020,
    "zfbpercent":self.zfbpercent2020,
    "zrar":self.zrar2020,
    "ztera":self.ztera2020,
    "zxfip":self.zxfip2020,
    "zwpa":self.zwpa2020,
    "zretwentyfour":self.zretwentyfour2020,
    "zclutch":self.zclutch2020,
    "zoutsidezoneswingpercent":self.zoutsidezoneswingpercent2020,
    "zfirstpitchstrikepercent":self.zfirstpitchstrikepercent2020,
    "zswingingstrikespercent":self.zswingingstrikespercent2020,
    "zshutdowns":self.zshutdowns2020,
    "zmeltdowns":self.zmeltdowns2020,
    "zeraminus":self.zeraminus2020,
    "zfipminus":self.zfipminus2020,
    "zxfipminus":self.zxfipminus2020,
    "zbbpercent":self.zbbpercent2020,
    "zcswpercent":self.zcswpercent2020,
    "zsoftpercent":self.zsoftpercent2020,
    "zmediumpercent":self.zmediumpercent2020,
    "zsoftplusmediumpercent":self.zsoftplusmediumpercent2020,
    "zkwera":self.zkwera2020,
    "zkpercent":self.zkpercent2020,
    "zweakpercent":self.zweakpercent2020,
    "zsiera":self.zsiera2020,
    "zplus_k_per_nine":self.zplus_k_per_nine2020,
    "zplus_bb_per_nine":self.zplus_bb_per_nine2020,
    "zplus_k_per_bb":self.zplus_k_per_bb2020,
    "zplus_h_per_nine":self.zplus_h_per_nine2020,
    "zplus_hr_per_nine":self.zplus_hr_per_nine2020,
    "zplus_avg":self.zplus_avg2020,
    "zplus_whip":self.zplus_whip2020,
    "zplus_babip":self.zplus_babip2020,
    "zplus_lobpercent":self.zplus_lobpercent2020,
    "zplus_kpercent":self.zplus_kpercent2020,
    "zplus_bbpercent":self.zplus_bbpercent2020,
    "zplus_ldpercent":self.zplus_ldpercent2020,
    "zplus_gbpercent":self.zplus_gbpercent2020,
    "zplus_hrperfb":self.zplus_hrperfb2020,
    "zplus_softpercent":self.zplus_softpercent2020,
    "zplus_mediumpercent":self.zplus_mediumpercent2020,
    "zbarrel_percent":self.zbarrel_percent2020,
    "zhardhitpercent":self.zhardhitpercent2020,
    "zaverageev":self.zaverageev2020,
    "zaveragela":self.zaveragela2020,
    "zxera":self.zxera2020,
    "zbbevents":self.zbbevents2020,
    "zanglesweetspotpercent":self.zanglesweetspotpercent2020,
    "zavgdistance":self.zavgdistance2020,
    "zev95plus":self.zev95plus2020,
    "zev95pluspercent":self.zev95pluspercent2020,
    "zbrlperpa":self.zbrlperpa2020,
    "zbip":self.zbip2020,
    "zxavg":self.zxavg2020,
    "zxavgdiff":self.zxavgdiff2020,
    "zslg":self.zslg2020,
    "zxslg":self.zxslg2020,
    "zxslgdiff":self.zxslgdiff2020,
    "zwoba":self.zwoba2020,
    "zxwoba":self.zxwoba2020,
    "zxwobadiff":self.zxwobadiff2020,
    "zxeradiff":self.zxeradiff2020
   }
   return zpitcher2020dict

  class Admin:
      pass

class team(models.Model):
  # fangraph's has the team_batting function which seems to be exactly the same as the individual batter. you can load this if you want, but you might want to stick with player-based model
  # team fielding has so many variables, loop back at the end and incorporate the team fielding and team batting. right now I gotta keep on moving
  # team pitching same deal as starter pitching with only a few columns different perhaps. same instructions as above
  name = models.CharField(max_length=3)
  fullname = models.CharField(max_length=20)
  city = models.CharField(max_length=30)
  logopath = models.CharField(max_length = 150)
  # the goal is to obtain whatever I obtained for starting pitchers to allow for a seamless transition from starters to bullpen in terms of stat usage by the user
  # I only care about the current year


  # standard stats
  erabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #
  winningpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  inningsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  battersfacedbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  savesbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  savepercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hitsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  runsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  runsaveragebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hitsperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  homerunsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bbhbpbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  kbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # z-score standard stats
  zerabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #
  zwinningpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zinningsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbattersfacedbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsavesbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsavepercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhitsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrunsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrunsaveragebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhitsperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhomerunsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbbhbpbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zkbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  
  #advanced
  kperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bbperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  kperbbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hrperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  kpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  bbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  kpercentminusbbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE this stat not currently in SP but should be
  avgbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  whipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  babipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  lobpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  eraminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fipminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xfipminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xfipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  sierabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score advanced
  zkperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbbperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zkperbbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhrperninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zkpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zkpercentminusbbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #NOTE this stat not currently in SP but should be
  zavgbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwhipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbabipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zlobpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zeraminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfipminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxfipminusbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxfipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsierabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  # batted ball
  gbperfbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  gbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ldpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  iffbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  thrownforkpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hrperfbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  softpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  mediumpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  softplusmediumpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  weakpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs
  # z-score batted ball
  zgbperfbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zgbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zldpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ziffbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zthrownforkpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhrperfbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsoftpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmediumpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsoftplusmediumpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zweakpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) #kpercent + iffb/battedballs + gb/battedballs

  # win probability
  wpabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  retwentyfourbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  clutchbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  shutdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  meltdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  shutdownpermeltdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # check for error, as with all per stats
  # z-score win probability
  zwpabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zretwentyfourbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zclutchbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zshutdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zmeltdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zshutdownpermeltdownbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) # check for error, as with all per stats

  # plate discipline
  outsidezoneswingpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  firstpitchstrikepercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  swingingstrikespercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  cswpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # z-score plate discipline
  zoutsidezoneswingpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfirstpitchstrikepercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zswingingstrikespercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zcswpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #value
  warbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  rarbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #z-score value
  zwarbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zrarbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  #plus
  plus_k_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_bb_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_k_per_bbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_hr_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_avgbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_whipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_babipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_lobpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  plus_kpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_bbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_ldpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  plus_gbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  #plus z-score
  zplus_k_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_bb_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_k_per_bbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_hr_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_avgbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_whipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_babipbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_lobpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zplus_kpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_bbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_ldpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zplus_gbpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  # statcast new
  bbeeventsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  barrel_percentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  brl_per_pabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  hardhitpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  averageevbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  averagelabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  #statcast new z-score
  # zbbeeventsbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) no use in z-score
  zbarrel_percentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zbrl_per_pabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zhardhitpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zaverageevbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  zaveragelabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 

  # not found but used for SP

  #weakpercent has not been loaded in yet
  # terabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # kwerabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # plus_h_per_ninebp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  # plus_hrperfbbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # plus_softpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  # plus_mediumpercentbp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) 
  #xerabp = models.DecimalField(max_digits = 19, decimal_places=10, default=0) save for baseball savant

  # team fielding
  errors = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  doubleplays = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  fieldingpercentage = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  sbagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  csagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  xsbsavedagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  wildpitchespluspassedballs = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  defensiverunssaved = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  ultimatezonerating = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  defense = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  # team fielding z-score
  zerrors = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zdoubleplays = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zfieldingpercentage = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zsbagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zcsagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zxsbsavedagainst = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zwildpitchespluspassedballs = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zdefensiverunssaved = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zultimatezonerating = models.DecimalField(max_digits = 19, decimal_places=10, default=0)
  zdefense = models.DecimalField(max_digits = 19, decimal_places=10, default=0)

  
  


  def __str__(self):
    self_title = self.name
    return self_title

  def accesszteam2022dict(self):
    zteam2022dict = {
      "zera":self.zerabp,
      "zwinningpercent":self.zwinningpercentbp,
      "zinnings":self.zinningsbp,
      "zbattersfaced":self.zbattersfacedbp,
      "zsaves":self.zsavesbp,
      "zsavepercent":self.zsavepercentbp,
      "zhits":self.zhitsbp,
      "zruns":self.zrunsbp,
      "zrunsaverage":self.zrunsaveragebp,
      "zhitpernine":self.zhitsperninebp,
      "zhomeruns":self.zhomerunsbp,
      "zbbhbp":self.zbbhbpbp,
      "zk":self.zkbp,
      "zkpernine":self.zkperninebp,
      "zbbpernine":self.zbbperninebp,
      "zkperbb":self.zkperbbbp,
      "zhrpernine":self.zhrperninebp,
      "zkpercent":self.zkpercentbp,
      "zbbpercent":self.zbbpercentbp,
      "zkpercentminusbbpercent":self.zkpercentminusbbpercentbp, #NOTE: repetitive
      "zavg":self.zavgbp,
      "zwhip":self.zwhipbp,
      "zbabip":self.zbabipbp,
      "zlobpercent":self.zlobpercentbp,
      "zeraminus":self.zeraminusbp,
      "zfipminus":self.zfipminusbp,
      "zxfipminus":self.zxfipminusbp,
      "zfip":self.zfipbp,
      "zxfip":self.zxfipbp,
      "zsiera":self.zsierabp,
      "zgbperfb":self.zgbperfbbp,
      "zgbpercent":self.zgbpercentbp,
      "zldpercent":self.zldpercentbp,
      "zfbpercent":self.zfbpercentbp,
      "ziffbpercent":self.ziffbpercentbp,
      "zthrownforkpercent":self.zthrownforkpercentbp,
      "zhrperfb":self.zhrperfbbp,
      "zsoftpercent":self.zsoftpercentbp,
      "zmediumpercent":self.zmediumpercentbp,
      "zsoftplusmediumpercent":self.zsoftplusmediumpercentbp,
      "zweakpercent":self.zweakpercentbp,
      "zwpa":self.zwpabp,
      "zretwentyfour":self.zretwentyfourbp,
      "zclutch":self.zclutchbp,
      "zshutdown":self.zshutdownbp,
      "zmeltdown":self.zmeltdownbp,
      "zshutdownpermeltdown":self.zshutdownpermeltdownbp,
      "zoutsidezoneswingpercent":self.zoutsidezoneswingpercentbp,
      "zfirstpitchstrikepercent":self.zfirstpitchstrikepercentbp,
      "zswingingstrikespercent":self.zswingingstrikespercentbp,
      "zcswpercent":self.zcswpercentbp,
      "zwar":self.zwarbp,
      "zrar":self.zrarbp,
      "zplus_k_per_nine":self.zplus_k_per_ninebp,
      "zplus_bb_per_nine":self.zplus_bb_per_ninebp,
      "zplus_k_per_bb":self.zplus_k_per_bbbp,
      "zplus_hr_per_nine":self.zplus_hr_per_ninebp,
      "zplus_avg":self.zplus_avgbp,
      "zplus_whip":self.zplus_whipbp,
      "zplus_babip":self.zplus_babipbp,
      "zplus_lobpercent":self.zplus_lobpercentbp,
      "zplus_kpercent":self.zplus_kpercentbp,
      "zplus_bbpercent":self.zplus_bbpercentbp,
      "zplus_ldpercent":self.zplus_ldpercentbp,
      "zplus_gbpercent":self.zplus_gbpercentbp,
      "zbarrel_percent":self.zbarrel_percentbp,
      "zbrl_per_pa":self.zbrl_per_pabp,
      "zhardhitpercent":self.zhardhitpercentbp,
      "zaverageev":self.zaverageevbp,
      "zaveragela":self.zaveragelabp,
      #fielding
      "zerrors":self.zerrors,
      "zdoubleplays":self.zdoubleplays,
      "zfieldingpercentage":self.zfieldingpercentage,
      "zsbagainst":self.zsbagainst,
      "zcsagainst":self.zcsagainst,
      "zxsbsavedagainst":self.zxsbsavedagainst,
      "zwildpitchespluspassedballs":self.zwildpitchespluspassedballs,
      "zdefensiverunssaved":self.zdefensiverunssaved,
      "zultimatezonerating":self.zultimatezonerating,
      "zdefense":self.zdefense
    }
    return zteam2022dict

  def accesszfielding2022dict(self):
    zfielding2022dict = {
      #fielding
    "zerrors":self.zerrors,
    "zdoubleplays":self.zdoubleplays,
    "zfieldingpercentage":self.zfieldingpercentage,
    "zsbagainst":self.zsbagainst,
    "zcsagainst":self.zcsagainst,
    "zxsbsavedagainst":self.zxsbsavedagainst,
    "zwildpitchespluspassedballs":self.zwildpitchespluspassedballs,
    "zdefensiverunssaved":self.zdefensiverunssaved,
    "zultimatezonerating":self.zultimatezonerating,
    "zdefense":self.zdefense
    }
    return zfielding2022dict

  def accesszbullpen2022dict(self):
    zbullpen2022dict = {
    "zera":self.zerabp,
    "zwinningpercent":self.zwinningpercentbp,
    "zinnings":self.zinningsbp,
    "zbattersfaced":self.zbattersfacedbp,
    "zsaves":self.zsavesbp,
    "zsavepercent":self.zsavepercentbp,
    "zhits":self.zhitsbp,
    "zruns":self.zrunsbp,
    "zrunsaverage":self.zrunsaveragebp,
    "zhitpernine":self.zhitsperninebp,
    "zhomeruns":self.zhomerunsbp,
    "zbbhbp":self.zbbhbpbp,
    "zk":self.zkbp,
    "zkpernine":self.zkperninebp,
    "zbbpernine":self.zbbperninebp,
    "zkperbb":self.zkperbbbp,
    "zhrpernine":self.zhrperninebp,
    "zkpercent":self.zkpercentbp,
    "zbbpercent":self.zbbpercentbp,
    "zkpercentminusbbpercent":self.zkpercentminusbbpercentbp, #NOTE: repetitive
    "zavg":self.zavgbp,
    "zwhip":self.zwhipbp,
    "zbabip":self.zbabipbp,
    "zlobpercent":self.zlobpercentbp,
    "zeraminus":self.zeraminusbp,
    "zfipminus":self.zfipminusbp,
    "zxfipminus":self.zxfipminusbp,
    "zfip":self.zfipbp,
    "zxfip":self.zxfipbp,
    "zsiera":self.zsierabp,
    "zgbperfb":self.zgbperfbbp,
    "zgbpercent":self.zgbpercentbp,
    "zldpercent":self.zldpercentbp,
    "zfbpercent":self.zfbpercentbp,
    "ziffbpercent":self.ziffbpercentbp,
    "zthrownforkpercent":self.zthrownforkpercentbp,
    "zhrperfb":self.zhrperfbbp,
    "zsoftpercent":self.zsoftpercentbp,
    "zmediumpercent":self.zmediumpercentbp,
    "zsoftplusmediumpercent":self.zsoftplusmediumpercentbp,
    "zweakpercent":self.zweakpercentbp,
    "zwpa":self.zwpabp,
    "zretwentyfour":self.zretwentyfourbp,
    "zclutch":self.zclutchbp,
    "zshutdown":self.zshutdownbp,
    "zmeltdown":self.zmeltdownbp,
    "zshutdownpermeltdown":self.zshutdownpermeltdownbp,
    "zoutsidezoneswingpercent":self.zoutsidezoneswingpercentbp,
    "zfirstpitchstrikepercent":self.zfirstpitchstrikepercentbp,
    "zswingingstrikespercent":self.zswingingstrikespercentbp,
    "zcswpercent":self.zcswpercentbp,
    "zwar":self.zwarbp,
    "zrar":self.zrarbp,
    "zplus_k_per_nine":self.zplus_k_per_ninebp,
    "zplus_bb_per_nine":self.zplus_bb_per_ninebp,
    "zplus_k_per_bb":self.zplus_k_per_bbbp,
    "zplus_hr_per_nine":self.zplus_hr_per_ninebp,
    "zplus_avg":self.zplus_avgbp,
    "zplus_whip":self.zplus_whipbp,
    "zplus_babip":self.zplus_babipbp,
    "zplus_lobpercent":self.zplus_lobpercentbp,
    "zplus_kpercent":self.zplus_kpercentbp,
    "zplus_bbpercent":self.zplus_bbpercentbp,
    "zplus_ldpercent":self.zplus_ldpercentbp,
    "zplus_gbpercent":self.zplus_gbpercentbp,
    "zbarrel_percent":self.zbarrel_percentbp,
    "zbrl_per_pa":self.zbrl_per_pabp,
    "zhardhitpercent":self.zhardhitpercentbp,
    "zaverageev":self.zaverageevbp,
    "zaveragela":self.zaveragelabp
    }
    return zbullpen2022dict

  class Admin:
      pass
    

class matchup(models.Model):
  awayteam = models.ForeignKey(team, on_delete = models.CASCADE, related_name = 'awayname', null = True, blank = True)
  hometeam = models.ForeignKey(team, on_delete = models.CASCADE, related_name = 'homename', null = True, blank = True) # this can also provide home park info if you want to include
  gametime = models.CharField(max_length=8, default="0")
  gamedate = models.CharField(max_length=18, default="0")
  doubleheadergameone = models.BooleanField(default=False)
  doubleheadergametwo = models.BooleanField(default=False)
  gametimetemp = models.IntegerField(default="0") # if you care to include
  chanceofrain = models.IntegerField(default="0")
  awaylineupposted = models.BooleanField(default=False) # check if the lineups have been posted when you want to do the math and display results
  homelineupposted = models.BooleanField(default=False)
  awaypitcher = models.ForeignKey(pitcher, on_delete = models.CASCADE, related_name = 'awaypitcher', null = True, blank = True) # starting pitcher
  homepitcher = models.ForeignKey(pitcher, on_delete = models.CASCADE, related_name = 'homepitcher', null = True, blank = True)
  awaypositions = models.CharField(max_length=18, default="0") # keep popping and adding two characters / one for catcher. remember, down the line we do not want to use the DH fielding value when doing the math
  homepositions = models.CharField(max_length=18, default="0") # keep popping and adding two characters / one for catcher
  awaybatterone = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatterone', null = True, blank = True)
  awaybattertwo = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybattertwo', null = True, blank = True)
  awaybatterthree = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatterthree', null = True, blank = True)
  awaybatterfour = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatterfour', null = True, blank = True)
  awaybatterfive = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatterfive', null = True, blank = True)
  awaybattersix = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybattersix', null = True, blank = True)
  awaybatterseven = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatterseven', null = True, blank = True)
  awaybattereight = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybattereight', null = True, blank = True)
  awaybatternine = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'awaybatternine', null = True, blank = True)
  homebatterone = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatterone', null = True, blank = True)
  homebattertwo = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebattertwo', null = True, blank = True)
  homebatterthree = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatterthree', null = True, blank = True)
  homebatterfour = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatterfour', null = True, blank = True)
  homebatterfive = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatterfive', null = True, blank = True)
  homebattersix = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebattersix', null = True, blank = True)
  homebatterseven = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatterseven', null = True, blank = True)
  homebattereight = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebattereight', null = True, blank = True)
  homebatternine = models.ForeignKey(batter, on_delete = models.CASCADE, related_name = 'homebatternine', null = True, blank = True)



  def __str__(self):
    self_title = self.awayteam.name + " at " + self.hometeam.name
    return self_title

  
  # likely needs to be deleted
  def matchupresults(self, customuserweights):
    #customuserweights should be all the weights provided by the user, in a dictionary?
    awaybatterlist = []
    awaybatterlist.append(self.awaybatterone, self.awaybattertwo, self.awaybatterthree, self.awaybatterfour, self.awaybatterfive, self.awaybattersix, self.awaybatterseven, self.awaybattereight, self.awaybatternine)
    #weigh the spot in the order for batting stats?
    for awaybatter in awaybatterlist:
      awaybatteroffensemetrics= []
      awaybatterdefensemetrics = []
      awaybattergeneralmetrics = []
      awaybatteroffensemetrics.append(awaybatter.zpa2022,awaybatter.zavg2022,awaybatter.zplus_avg2022,awaybatter.zobp2022,awaybatter.zplus_obp2022,awaybatter.zslg2022,awaybatter.zplus_slg2022,awaybatter.zops2022,awaybatter.zbb_per_pa2022,awaybatter.zplus_bb_per_pa2022,awaybatter.zk_per_pa2022,awaybatter.zplus_k_per_pa2022,awaybatter.zr_per_pa2022,awaybatter.zrbi_per_pa2022,awaybatter.zgdp_per_pa2022,awaybatter.zxSB_added2022,awaybatter.zxSB_added_percent2022,awaybatter.zwRAA2022,awaybatter.zwOBA2022,awaybatter.zwRC2022,awaybatter.zplus_wRC2022,awaybatter.ziso2022,awaybatter.zplus_iso2022,awaybatter.zbabip2022,awaybatter.zplus_babip2022,awaybatter.zld_per_bip2022,awaybatter.zgb_per_bip2022,awaybatter.zfb_per_bip2022,awaybatter.ziffb_per_bip2022,awaybatter.zhr_per_fb2022,awaybatter.zplus_ld_per_bip2022,awaybatter.zplus_gb_per_bip2022,awaybatter.zplus_fb_per_bip2022,awaybatter.zplus_hr_per_fb2022,awaybatter.zspd2022,awaybatter.zbsr2022,awaybatter.zhardpercent2022,awaybatter.zplus_hardpercent2022,awaybatter.zhardhitpercent2022,awaybatter.zbsr_per_pa2022,awaybatter.zoutsideawaybatter.zoneswingpercent2022,awaybatter.zfirstpitchstrikepercent2022,awaybatter.zswingcontactpercent2022,awaybatter.zswingingstrikespercent2022,awaybatter.zfoff2022, awaybatter.zfoff_per_pa2022, awaybatter.zfbat2022)
      awaybatterdefensemetrics.append(awaybatter.zfdef2022,awaybatter.zfdef_per_pa2022, awaybatter.zffld2022,awaybatter.zffld_per_pa2022)
      awaybattergeneralmetrics.append(awaybatter.zclutch2022,awaybatter.zfwar2022,awaybatter.zfwar_per_pa2022)
      




  class Admin:
      pass

  # https://www.baseball-reference.com/about/war_explained_wraa.shtml
  # a lot of helpful info for the math