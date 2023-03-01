from django import forms
from django.forms import ModelForm
from app_bb.models import batter, pitcher

# 3.5 in homefieldradio will be changed to actual auto value


class GeneralWeightsForm(forms.Form):
  #plan: keep the radios as-is for general, manually save when the form is posted
  #home-field
  homefield_auto = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input homefieldradio','id':'homefieldauto','checked':'checked','name':'homefieldauto','value':'homefieldauto'}), required = False)
  homefield_manual = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input homefieldradio','id':'homefieldmanual','name':'homefieldmanual','value':'homefieldmanual'}), required = False)
  homefield_none = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input homefieldradio','id':'homefieldnone','name':'homefieldnone','value':'homefieldnone'}), required = False)
  homefield_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control halfbox', 'id':'homefieldweightinput', 'name':'homefieldadvantageweight','step':'0.01','min':'0','max':'50','value':'3.500'}
      ), max_value=50,min_value=0, decimal_places=3, required = False)
  #three-year weighted
  seasonweights_auto = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input seasonweightsradio','id':'seasonweightsauto','checked':'checked','name':'seasonweightsradio','value':'seasonweightsauto'}), required = False)
  seasonweights_manual = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input seasonweightsradio','id':'seasonweightsmanual','name':'seasonweightsradio','value':'seasonweightsmanual'}), required = False)
  seasonweights_current = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input seasonweightsradio','id':'seasonweightscurrent','name':'seasonweightsradio','value':'seasonweightscurrent'}), required = False)
  s2022_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control seasonweightsinput', 'name':'s2022_weight','step':'0.01','min':'0','max':'100','value':'60.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  s2021_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control seasonweightsinput', 'name':'s2021_weight','step':'0.01','min':'0','max':'100','value':'28.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  s2020_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control seasonweightsinput', 'name':'s2020_weight','step':'0.01','min':'0','max':'100','value':'12.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  #standard or plus
  standard_park_adjusted = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input plusradio','id':'plusstandard','checked':'checked','name':'plusradio','value':'plusstandard'}), required = False)
  plus_park_adjusted = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input plusradio','id':'plusplus','name':'plusradio','value':'plusplus'}), required = False)
  #batting/pitching/baserunning/fielding
  bsrfld_auto = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input bsrfldradio','id':'bsrfldauto','checked':'checked','name':'bsrfldradio','value':'bsrfldauto'}), required = False)
  bsrfld_manual = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input bsrfldradio','id':'bsrfldmanual','name':'bsrfldradio','value':'bsrfldmanual'}), required = False)
  batting_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control categoryinput', 'name':'batting_weight','step':'0.01','min':'0','max':'100','value':'50.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  pitching_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control categoryinput', 'name':'pitching_weight','step':'0.01','min':'0','max':'100','value':'50.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  baserunning_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control categoryinput', 'name':'baserunning_weight','step':'0.01','min':'0','max':'100','value':'0.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  fielding_weight = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control categoryinput', 'name':'fielding_weight','step':'0.01','min':'0','max':'100','value':'0.00'}
      ), max_value=100,min_value=0, decimal_places=3, required = False)
  #starterinnings
  starterinnings = forms.DecimalField(widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control halfbox ', 'id':'inningsinput','name':'starterinnings','step':'0.1','min':'1','max':'9','value':'5.0'}
      ), max_value=9,min_value=1, decimal_places=1, required = False)
  #variance
  variance = forms.DecimalField(widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control halfbox', 'id':'varianceinput','name':'variance','step':'0.01','min':'0','max':'8','value':'1.2'}
    ), max_value=8,min_value=0, decimal_places=2, required = True)


#anything in the batter model will be included in this form. that includes baserunning and player-based fielding
class BattingWeightsForm(forms.Form):
  #box-score

  #NOTE: for the categories avg, slugging, hardhit%, sweetspot %, babip, xavg, xslg, xwoba, fclutch the variable names are same for pitching and batting. to remedy, I will add a b to batter for all of those
  bavg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bavg_weight', 'id':'bavginput','step':'0.01','min':'0','max':'100','placeholder':'batting average','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  obp_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'obp_weight', 'id':'obpinput','step':'0.01','min':'0','max':'100','placeholder':'on-base %','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  bslg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bslg_weight', 'id':'bslginput','step':'0.01','min':'0','max':'100','placeholder':'slugging %','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  ops_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'ops_weight', 'id':'opsinput','step':'0.01','min':'0','max':'100','placeholder':'on-base + slugging %','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  rperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'rperpa_weight', 'id':'rperpainput','step':'0.01','min':'0','max':'100','placeholder':'runs scored / plate appearance','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  rbiperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'rbiperpa_weight', 'id':'rbiperpainput','step':'0.01','min':'0','max':'100','placeholder':'runs batted in / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  gdpperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'gdpperpa_weight', 'id':'gdpperpainput','step':'0.01','min':'0','max':'100','placeholder':'grounded into double play / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  bbperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bbperpa_weight', 'id':'bbperpainput','step':'0.01','min':'0','max':'100','placeholder':'walks / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  kperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'kperpa_weight', 'id':'kperpainput','step':'0.01','min':'0','max':'100','placeholder':'strikeouts / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  chaserate_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'chaserate_weight', 'id':'chaserateinput','step':'0.01','min':'0','max':'100','placeholder':'% outside zone swings','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  firstpitchstrike_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'firstpitchstrike_weight', 'id':'firstpitchstrikeinput','step':'0.01','min':'0','max':'100','placeholder':'% of pa with 0-1 counts','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  swingcontact_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'swingcontact_weight', 'id':'swingcontactinput','step':'0.01','min':'0','max':'100','placeholder':'% of swings which make contact','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  swingingstrike_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'swingingstrike_weight', 'id':'swingingstrikeinput','step':'0.01','min':'0','max':'100','placeholder':'% of pitches swung and missed','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  #batted-ball
  bbabip_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control battinginput', 'name':'bbabip_weight', 'id':'bbabipinput','step':'0.01','min':'0','max':'100','placeholder':'hits / bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  ld_per_bip_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'ld_per_bip_weight', 'id':'ld_per_bipinput','step':'0.01','min':'0','max':'100','placeholder':'line drives / bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  gb_per_bip_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'gb_per_bip_weight', 'id':'gb_per_bipinput','step':'0.01','min':'0','max':'100','placeholder':'ground balls / bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  fb_per_bip_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'fb_per_bip_weight', 'id':'fb_per_bipinput','step':'0.01','min':'0','max':'100','placeholder':'fly balls / bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  iffb_per_bip_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'iffb_per_bip_weight', 'id':'iffb_per_bipinput','step':'0.01','min':'0','max':'100','placeholder':'in-field fb / bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  hr_per_fb_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'hr_per_fb_weight', 'id':'hr_per_fbinput','step':'0.01','min':'0','max':'100','placeholder':'homeruns / fb','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  hardpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'hardpercent_weight', 'id':'hardpercentinput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs hard contact %','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bhardhitpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bhardhitpercent_weight', 'id':'bhardhitpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of balls hit hard','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  banglesweetspotpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'banglesweetspotpercent_weight', 'id':'banglesweetspotpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with launch angle 8 to 32','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  avg_hit_speed_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'avg_hit_speed_weight', 'id':'avg_hit_speedinput','step':'0.01','min':'0','max':'100','placeholder':'avg exit velocity on bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  avg_distance_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'avg_distance_weight', 'id':'avg_distanceinput','step':'0.01','min':'0','max':'100','placeholder':'avg distance of bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  ev95percent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'ev95percent_weight', 'id':'ev95percentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with exit velo 95+mph','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  brl_percent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'brl_percent_weight', 'id':'brl_percentinput','step':'0.01','min':'0','max':'100','placeholder':'% of abs which end in a "barrel"','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  #AGGREGATE
  wRAA_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control battinginput', 'name':'wRAA_weight', 'id':'wRAAinput','step':'0.01','min':'0','max':'100','placeholder':'weighted runs above average','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  wOBA_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'wOBA_weight', 'id':'wOBAinput','step':'0.01','min':'0','max':'100','placeholder':'weighted on-base average','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  wRC_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'wRC_weight', 'id':'wRCinput','step':'0.01','min':'0','max':'100','placeholder':'weighted runs created','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  iso_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'iso_weight', 'id':'isoinput','step':'0.01','min':'0','max':'100','placeholder':'extra base hits / ab','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bxwoba_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bxwoba_weight', 'id':'bxwobainput','step':'0.01','min':'0','max':'100','placeholder':'expected wOBA','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bxavg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bxavg_weight', 'id':'bxavginput','step':'0.01','min':'0','max':'100','placeholder':'expected batting average','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bxslg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bxslg_weight', 'id':'bxslginput','step':'0.01','min':'0','max':'100','placeholder':'expected slugging','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bclutch_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bclutch_weight', 'id':'bclutchinput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs clutch rating','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  fbat_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'fbat_per_pa_weight', 'id':'fbat_per_painput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs batting value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bref_batting_runs_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'bref_batting_runs_per_pa_weight', 'id':'bref_batting_runs_per_painput','step':'0.01','min':'0','max':'100','placeholder':'baseball reference batting value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  max_distance_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'max_distance_weight', 'id':'max_distanceinput','step':'0.01','min':'0','max':'100','placeholder':'maximum batted ball distance','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  max_hit_speed_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'max_hit_speed_weight', 'id':'max_hit_speedinput','step':'0.01','min':'0','max':'100','placeholder':'maximum batted ball exit velocity','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  brl_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control battinginput', 'name':'brl_pa_weight', 'id':'brl_painput','step':'0.01','min':'0','max':'100','placeholder':'barrels / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)




  #BASERUNNING
  xSB_added_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'xSB_added_weight', 'id':'xSB_addedinput','step':'0.01','min':'0','max':'100','placeholder':'sb - (2 * cs)','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  xSB_added_percent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'xSB_added_percent_weight', 'id':'xSB_added_percentinput','step':'0.01','min':'0','max':'100','placeholder':'(sb - (2 * cs)) / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  spd_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'spd_weight', 'id':'spdinput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs speed metric','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bsr_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'bsr_per_pa_weight', 'id':'bsr_per_painput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs baserunning value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  bref_bsr_runs_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'bref_bsr_runs_per_pa_weight', 'id':'bref_bsr_runs_per_painput','step':'0.01','min':'0','max':'100','placeholder':'bref baserunning value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  home_to_first_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'home_to_first_weight', 'id':'home_to_firstinput','step':'0.01','min':'0','max':'100','placeholder':'seconds from home to first','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  
  sprint_speed_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control baserunninginput', 'name':'sprint_speed_weight', 'id':'sprint_speedinput','step':'0.01','min':'0','max':'100','placeholder':'max running speed','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

   #fielding
  outs_above_avg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'outs_above_avg_weight', 'id':'outs_above_avginput','step':'0.01','min':'0','max':'100','placeholder':'outs above average','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  fielding_runs_prevented_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'fielding_runs_prevented_weight', 'id':'fielding_runs_preventedinput','step':'0.01','min':'0','max':'100','placeholder':'fielding runs prevented','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  ffld_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'ffld_per_pa_weight', 'id':'ffld_per_painput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs fielding value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  fdef_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'fdef_per_pa_weight', 'id':'fdef_per_painput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs defense value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  bref_war_def_per_pa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'bref_war_def_per_pa_weight', 'id':'bref_war_def_per_painput','step':'0.01','min':'0','max':'100','placeholder':'bref defense value','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)












#PITCHING

class PitchingWeightsForm(forms.Form):
 #box-score
  winningpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'winningpercent_weight', 'id':'winningpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of decisions which are wins','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  shutouts_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'shutouts_weight', 'id':'shutoutsinput','step':'0.01','min':'0','max':'100','placeholder':'complete-game shutouts','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  hitpernine_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'hitpernine_weight', 'id':'hitpernineinput','step':'0.01','min':'0','max':'100','placeholder':'hits against / 9IP','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  bbpernine_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'bbpernine_weight', 'id':'bbpernineinput','step':'0.01','min':'0','max':'100','placeholder':'walks / 9','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  kpernine_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'kpernine_weight', 'id':'kpernineinput','step':'0.01','min':'0','max':'100','placeholder':'strikeouts / 9','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  hrpernine_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'hrpernine_weight', 'id':'hrpernineinput','step':'0.01','min':'0','max':'100','placeholder':'homeruns / 9','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  kperbb_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'kperbb_weight', 'id':'kperbbinput','step':'0.01','min':'0','max':'100','placeholder':'strikeouts / walk','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  avg_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'avg_weight', 'id':'avginput','step':'0.01','min':'0','max':'100','placeholder':'batting avg against','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  whip_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'whip_weight', 'id':'whipinput','step':'0.01','min':'0','max':'100','placeholder':'whip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  lobpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'lobpercent_weight', 'id':'lobpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of baserunners stranded','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  thrownforkpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'thrownforkpercent_weight', 'id':'thrownforkpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of strike-pitches','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  cswpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'cswpercent_weight', 'id':'cswpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of non-foulball strike-pitches','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  outsidezoneswingpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'outsidezoneswingpercent_weight', 'id':'outsidezoneswingpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% outside zone swings','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)

  firstpitchstrikepercent_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'firstpitchstrikepercent_weight', 'id':'firstpitchstrikepercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of counts starting 0-1','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  swingingstrikespercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'swingingstrikespercent_weight', 'id':'swingingstrikespercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of pitches swung and missed','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  bbpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'bbpercent_weight', 'id':'bbpercentinput','step':'0.01','min':'0','max':'100','placeholder':'walks / pa','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  kpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'kpercent_weight', 'id':'kpercentinput','step':'0.01','min':'0','max':'100','placeholder':'strikeouts / pa','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  slg_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'slg_weight', 'id':'slginput','step':'0.01','min':'0','max':'100','placeholder':'slugging against','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)



  #BATTED BALL
  babip_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'babip_weight', 'id':'babipinput','step':'0.01','min':'0','max':'100','placeholder':'batting average on bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  gbperfb_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'gbperfb_weight', 'id':'gbperfbinput','step':'0.01','min':'0','max':'100','placeholder':'groundballs / flyball','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  hrperfb_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'hrperfb_weight', 'id':'hrperfbinput','step':'0.01','min':'0','max':'100','placeholder':'homeruns / flyball','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  gbpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'gbpercent_weight', 'id':'gbpercentinput','step':'0.01','min':'0','max':'100','placeholder':'groundballs / bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  iffbpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'iffbpercent_weight', 'id':'iffbpercentinput','step':'0.01','min':'0','max':'100','placeholder':'in-field fb / bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  ldpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'ldpercent_weight', 'id':'ldpercentinput','step':'0.01','min':'0','max':'100','placeholder':'linedrives / bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  fbpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'fbpercent_weight', 'id':'fbpercentinput','step':'0.01','min':'0','max':'100','placeholder':'flyballs / bip','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
  softpercent_weight = forms.DecimalField(
   widget=forms.NumberInput(
     attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'softpercent_weight', 'id':'softpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with soft contact','maxlength':'5'}
     ),
   max_value=100,min_value=0, decimal_places=3, required = False)
 
  softplusmediumpercent_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'softplusmediumpercent_weight', 'id':'softplusmediumpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with soft/medium contact','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  weakpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'weakpercent_weight', 'id':'weakpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with weak contact','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  barrel_percent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'barrel_percent_weight', 'id':'barrel_percentinput','step':'0.01','min':'0','max':'100','placeholder':'% of abs which end in a "barrel"','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  hardhitpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'hardhitpercent_weight', 'id':'hardhitpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip hit hard','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  averageev_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'averageev_weight', 'id':'averageevinput','step':'0.01','min':'0','max':'100','placeholder':'avg exit velocity on bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  averagela_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'averagela_weight', 'id':'averagelainput','step':'0.01','min':'0','max':'100','placeholder':'avg launch angle on bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  anglesweetspotpercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'anglesweetspotpercent_weight', 'id':'anglesweetspotpercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with la 8-32 degrees','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  avgdistance_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'avgdistance_weight', 'id':'avgdistanceinput','step':'0.01','min':'0','max':'100','placeholder':'avg distance of bip','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  ev95pluspercent_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'ev95pluspercent_weight', 'id':'ev95pluspercentinput','step':'0.01','min':'0','max':'100','placeholder':'% of bip with exit velo 95+mph','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  brlperpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'brlperpa_weight', 'id':'brlperpainput','step':'0.01','min':'0','max':'100','placeholder':'barrels / pa','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)


  #AGGREGATE  
  era_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'era_weight', 'id':'erainput','step':'0.01','min':'0','max':'100','placeholder':'earned runs / 9','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  xera_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'xera_weight', 'id':'xerainput','step':'0.01','min':'0','max':'100','placeholder':'expected era','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  runsaverage_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'runsaverage_weight', 'id':'runsaverageinput','step':'0.01','min':'0','max':'100','placeholder':'runs / 9','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

  war_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'war_weight', 'id':'warinput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs wins above replacement','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  fip_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'fip_weight', 'id':'fipinput','step':'0.01','min':'0','max':'100','placeholder':'fielding-independent pitching','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  xfip_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'xfip_weight', 'id':'xfipinput','step':'0.01','min':'0','max':'100','placeholder':'xFIP','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  siera_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'siera_weight', 'id':'sierainput','step':'0.01','min':'0','max':'100','placeholder':'SIERA','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  rar_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'rar_weight', 'id':'rarinput','step':'0.01','min':'0','max':'100','placeholder':'runs above replacement','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  tera_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'tera_weight', 'id':'terainput','step':'0.01','min':'0','max':'100','placeholder':'true runs allowed','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  wpa_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'wpa_weight', 'id':'wpainput','step':'0.01','min':'0','max':'100','placeholder':'win probability added','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  retwentyfour_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'retwentyfour_weight', 'id':'retwentyfourinput','step':'0.01','min':'0','max':'100','placeholder':'twenty-four state run contribution','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  clutch_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'clutch_weight', 'id':'clutchinput','step':'0.01','min':'0','max':'100','placeholder':'fangraphs clutch rating','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  kwera_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'kwera_weight', 'id':'kwerainput','step':'0.01','min':'0','max':'100','placeholder':'strikeout-walk era','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  woba_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'woba_weight', 'id':'wobainput','step':'0.01','min':'0','max':'100','placeholder':'weighted on-base average against','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  xavg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'xavg_weight', 'id':'xavginput','step':'0.01','min':'0','max':'100','placeholder':'expected avg against','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  xslg_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'xslg_weight', 'id':'xslginput','step':'0.01','min':'0','max':'100','placeholder':'expected slugging against','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  xwoba_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control pitchinginput', 'name':'xwoba_weight', 'id':'xwobainput','step':'0.01','min':'0','max':'100','placeholder':'expected woba against','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)




# TEAM BASED FIELDING
class TeamWeightsForm(forms.Form):
  errors_weight = forms.DecimalField(
  widget=forms.NumberInput(
    attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'errors_weight', 'id':'errorsinput','step':'0.01','min':'0','max':'100','placeholder':'total team errors','maxlength':'5'}
    ),
  max_value=100,min_value=0, decimal_places=3, required = False)
  doubleplays_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'doubleplays_weight', 'id':'doubleplaysinput','step':'0.01','min':'0','max':'100','placeholder':'total double-plays turned','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  fieldingpercentage_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'fieldingpercentage_weight', 'id':'fieldingpercentageinput','step':'0.01','min':'0','max':'100','placeholder':'fielding %','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  xsbsavedagainst_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'xsbsavedagainst_weight', 'id':'xsbsavedagainstinput','step':'0.01','min':'0','max':'100','placeholder':'xsb above average','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  wildpitchespluspassedballs_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'wildpitchespluspassedballs_weight', 'id':'wildpitchespluspassedballsinput','step':'0.01','min':'0','max':'100','placeholder':'wild pitches + passed balls','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  defensiverunssaved_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'defensiverunssaved_weight', 'id':'defensiverunssavedinput','step':'0.01','min':'0','max':'100','placeholder':'defensive runs saved','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  ultimatezonerating_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'ultimatezonerating_weight', 'id':'ultimatezoneratinginput','step':'0.01','min':'0','max':'100','placeholder':'ultimate zone rating','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)
  defense_weight = forms.DecimalField(
    widget=forms.NumberInput(
      attrs={'type':'number', 'class':'form-control fieldinginput', 'name':'defense_weight', 'id':'defenseinput','step':'0.01','min':'0','max':'100','placeholder':'team defense rating','maxlength':'5'}
      ),
    max_value=100,min_value=0, decimal_places=3, required = False)

# class SingleGameForm(forms.Form):
#   orderedpitchers = pitcher.objects.all().order_by('lastname' , 'firstname')
#   h_p1 = forms.ModelChoiceField(orderedpitchers)
#   h_p2 = forms.ModelChoiceField(orderedpitchers)
#   a_p1 = forms.ModelChoiceField(orderedpitchers)
#   a_p2 = forms.ModelChoiceField(orderedpitchers)
#   orderedbatters = batter.objects.all().order_by('lastname' , 'firstname')
#   h_b1 = forms.ModelChoiceField(orderedbatters)
#   h_b2 = forms.ModelChoiceField(orderedbatters)
#   a_b1 = forms.ModelChoiceField(orderedbatters)
#   a_b2 = forms.ModelChoiceField(orderedbatters)
  # h_b5 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # h_b6 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # h_b7 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # h_b8 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # h_b9 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b1 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b2 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b3 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b4 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b5 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b6 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b7 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b8 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
  # a_b9 = forms.ModelChoiceField(queryset=batter.objects.all().order_by('lastname' , 'firstname'))
