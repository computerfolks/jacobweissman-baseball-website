from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (TemplateView)
from django.views.generic import (FormView)
from app_bb.models import matchup, pitcher, batter, team
from django import forms
from .forms import GeneralWeightsForm, BattingWeightsForm, PitchingWeightsForm, TeamWeightsForm #, SingleGameForm
import requests
import random
import pickle
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'

class BeginnerView(TemplateView):
  template_name = 'beginner.html'

class AboutView(TemplateView):
  template_name = 'about.html'

class InfoView(TemplateView):
  template_name = 'info.html'


def single_view(request):
  if request.method == "POST":
    h_p1 = pitcher.objects.get(fangraphs_id = request.POST['h_p1'])
    h_p2 = pitcher.objects.get(fangraphs_id = request.POST['h_p2'])
    h_p3 = pitcher.objects.get(fangraphs_id = request.POST['h_p3'])
    h_p4 = pitcher.objects.get(fangraphs_id = request.POST['h_p4'])
    h_p5 = pitcher.objects.get(fangraphs_id = request.POST['h_p5'])
    h_p6 = pitcher.objects.get(fangraphs_id = request.POST['h_p6'])
    h_p7 = pitcher.objects.get(fangraphs_id = request.POST['h_p7'])
    homepitchers = [h_p1, h_p2, h_p3, h_p4, h_p5, h_p6, h_p7]
    print(h_p1)
    print(h_p2)
    print(h_p3)
    print(h_p4)
    print(h_p5)
    print(h_p6)
    print(h_p7)
    h_b1 = batter.objects.get(fangraphs_id = request.POST['h_b1'])
    h_b2 = batter.objects.get(fangraphs_id = request.POST['h_b2'])
    h_b3 = batter.objects.get(fangraphs_id = request.POST['h_b3'])
    h_b4 = batter.objects.get(fangraphs_id = request.POST['h_b4'])
    h_b5 = batter.objects.get(fangraphs_id = request.POST['h_b5'])
    h_b6 = batter.objects.get(fangraphs_id = request.POST['h_b6'])
    h_b7 = batter.objects.get(fangraphs_id = request.POST['h_b7'])
    h_b8 = batter.objects.get(fangraphs_id = request.POST['h_b8'])
    h_b9 = batter.objects.get(fangraphs_id = request.POST['h_b9'])
    homelineup = [h_b1, h_b2, h_b3, h_b4, h_b5, h_b6, h_b7, h_b8, h_b9]
    print(h_b1)
    print(h_b2)
    print(h_b3)
    print(h_b4)
    print(h_b5)
    print(h_b6)
    print(h_b7)
    print(h_b8)
    print(h_b9)
    h_ip1 = request.POST['h_ip1']
    print(h_ip1)
    h_ip2 = request.POST['h_ip2']
    h_ip3 = request.POST['h_ip3']
    h_ip4 = request.POST['h_ip4']
    h_ip5 = request.POST['h_ip5']
    h_ip6 = request.POST['h_ip6']
    h_ip7 = request.POST['h_ip7']
    homeinnings = [h_ip1, h_ip2, h_ip3, h_ip4, h_ip5, h_ip6, h_ip7]
    a_p1 = pitcher.objects.get(fangraphs_id = request.POST['a_p1'])
    a_p2 = pitcher.objects.get(fangraphs_id = request.POST['a_p2'])
    a_p3 = pitcher.objects.get(fangraphs_id = request.POST['a_p3'])
    a_p4 = pitcher.objects.get(fangraphs_id = request.POST['a_p4'])
    a_p5 = pitcher.objects.get(fangraphs_id = request.POST['a_p5'])
    a_p6 = pitcher.objects.get(fangraphs_id = request.POST['a_p6'])
    a_p7 = pitcher.objects.get(fangraphs_id = request.POST['a_p7'])
    awaypitchers = [a_p1, a_p2, a_p3, a_p4, a_p5, a_p6, a_p7]
    print(a_p1)
    print(a_p2)
    print(a_p3)
    print(a_p4)
    print(a_p5)
    print(a_p6)
    print(a_p7)
    a_b1 = batter.objects.get(fangraphs_id = request.POST['a_b1'])
    a_b2 = batter.objects.get(fangraphs_id = request.POST['a_b2'])
    a_b3 = batter.objects.get(fangraphs_id = request.POST['a_b3'])
    a_b4 = batter.objects.get(fangraphs_id = request.POST['a_b4'])
    a_b5 = batter.objects.get(fangraphs_id = request.POST['a_b5'])
    a_b6 = batter.objects.get(fangraphs_id = request.POST['a_b6'])
    a_b7 = batter.objects.get(fangraphs_id = request.POST['a_b7'])
    a_b8 = batter.objects.get(fangraphs_id = request.POST['a_b8'])
    a_b9 = batter.objects.get(fangraphs_id = request.POST['a_b9'])
    awaylineup = [a_b1, a_b2, a_b3, a_b4, a_b5, a_b6, a_b7, a_b8, a_b9]
    print(a_b1)
    print(a_b2)
    print(a_b3)
    print(a_b4)
    print(a_b5)
    print(a_b6)
    print(a_b7)
    print(a_b8)
    print(a_b9)
    a_ip1 = request.POST['a_ip1']
    print(a_ip1)
    a_ip2 = request.POST['a_ip2']
    a_ip3 = request.POST['a_ip3']
    a_ip4 = request.POST['a_ip4']
    a_ip5 = request.POST['a_ip5']
    a_ip6 = request.POST['a_ip6']
    a_ip7 = request.POST['a_ip7']
    awayinnings = [a_ip1, a_ip2, a_ip3, a_ip4, a_ip5, a_ip6, a_ip7]
    hometeam = request.POST['hometeam']
    awayteam = request.POST['awayteam']

    #as a trial, make up positions
    awaypositions = "DHC 1B2B3BSSRFCFLF"
    homepositions = awaypositions
    #all the input has been checked as valid, so call the simulation
    request.session["singlegameresults"] = singlesimulation(awayteam, hometeam, awaylineup, homelineup, awaypitchers, homepitchers, awayinnings, homeinnings, awaypositions, homepositions, pickle.loads(bytes.fromhex(request.session['wbatterdict'])), pickle.loads(bytes.fromhex(request.session['wbaserunningdict'])), pickle.loads(bytes.fromhex(request.session['wfieldingdict'])), pickle.loads(bytes.fromhex(request.session['wpitcherdict'])), pickle.loads(bytes.fromhex(request.session['wteamdict'])), pickle.loads(bytes.fromhex(request.session['wgeneraldict'])))
    # return HttpResponseRedirect('/loading/')
    print(request.session["singlegameresults"])
    # return HttpResponseRedirect('/singleresults/')
    return HttpResponseRedirect('/results/')


    # pitcherform = SingleGameForm(request.POST)
    # if pitcherform.is_valid():
    #   print(pitcherform.cleaned_data['h_p1'])
    #   print(pitcherform.cleaned_data['h_p2'])
    #   print(pitcherform.cleaned_data['h_b1'])
    #   print(pitcherform.cleaned_data['h_b2'])
    #   # print(pitcherform.cleaned_data['h_b3'])
    #   # print(pitcherform.cleaned_data['h_b4'])
    #   # print(pitcherform.cleaned_data['h_b5'])
    #   # print(pitcherform.cleaned_data['h_b6'])
    #   # print(pitcherform.cleaned_data['h_b7'])
    #   # print(pitcherform.cleaned_data['h_b8'])
    #   # print(pitcherform.cleaned_data['h_b9'])
    #   print(pitcherform.cleaned_data['a_p1'])
    #   print(pitcherform.cleaned_data['a_p2'])
    #   print(pitcherform.cleaned_data['a_b1'])
    #   print(pitcherform.cleaned_data['a_b2'])
    #   # print(pitcherform.cleaned_data['a_b3'])
    #   # print(pitcherform.cleaned_data['a_b4'])
    #   # print(pitcherform.cleaned_data['a_b5'])
    #   # print(pitcherform.cleaned_data['a_b6'])
    #   # print(pitcherform.cleaned_data['a_b7'])
    #   # print(pitcherform.cleaned_data['a_b8'])
    #   # print(pitcherform.cleaned_data['a_b9'])
  else:
    # pitcherform = SingleGameForm()
    # I need something here, same strategy as results_view, that redirects if there is no dict (workshop has not been completed)
    pitchers = pitcher.objects.all().order_by('lastname' , 'firstname')
    batters = batter.objects.all().order_by('lastname' , 'firstname')
    innings = [0, 0.1, 0.2, 1, 1.1, 1.2, 2, 2.1, 2.2, 3, 3.1, 3.2, 4, 4.1, 4.2, 5, 5.1, 5.2, 6, 6.1, 6.2, 7, 7.1, 7.2, 8, 8.1, 8.2, 9]
    context = {"pitchers": pitchers, "batters": batters, "innings": innings}
    return render(request, "single.html", context)

# class LoaderView(TemplateView):
#   template_name = 'loaderio-189658c2fc236d9bc89764d0f7b45904.html'

# class WorkshopView(FormView):
#   form_class = WeightsForm
#   template_name = 'workshop.html'

def workshop_view(request):
  if request.method == "POST":
    wgeneraldict = {}
    #handle general
    generalform = GeneralWeightsForm(request.POST)
    if generalform.is_valid():
      #set general values
      #set homefield
      generalform.homefield_auto = generalform.cleaned_data['homefield_auto']
      wgeneraldict['homefield_auto'] = generalform.homefield_auto
      request.session['homefield_auto'] = bool(generalform.homefield_auto)

      generalform.homefield_manual = generalform.cleaned_data['homefield_manual']
      wgeneraldict['homefield_manual'] = generalform.homefield_manual
      request.session['homefield_manual'] = bool(generalform.homefield_manual)

      generalform.homefield_none = generalform.cleaned_data['homefield_none']
      wgeneraldict['homefield_none'] = generalform.homefield_none
      request.session['homefield_none'] =bool(generalform.homefield_none)

      if (generalform.homefield_auto):
        generalform.homefield_weight = 3.5;
      elif(generalform.homefield_manual):
        generalform.homefield_weight = float(generalform.cleaned_data['homefield_weight'])
      else:
        generalform.homefield_weight = 0
      wgeneraldict['homefield_weight'] = generalform.homefield_weight
      request.session['homefield_weight'] = str(generalform.homefield_weight)

      #set seasonweight
      generalform.seasonweights_auto = generalform.cleaned_data['seasonweights_auto']
      wgeneraldict['seasonweights_auto'] = generalform.seasonweights_auto
      request.session['seasonweights_auto'] =bool(generalform.seasonweights_auto)

      generalform.seasonweights_manual = generalform.cleaned_data['seasonweights_manual']
      wgeneraldict['seasonweights_manual'] = generalform.seasonweights_manual
      request.session['seasonweights_manual'] = bool(generalform.seasonweights_manual)

      generalform.seasonweights_current = generalform.cleaned_data['seasonweights_current']
      wgeneraldict['seasonweights_current'] = generalform.seasonweights_current
      request.session['seasonweights_current'] = bool(generalform.seasonweights_current)

      if (generalform.seasonweights_auto):
        generalform.s2022_weight = 60.000
        generalform.s2021_weight = 28.000
        generalform.s2020_weight = 12.000
      elif(generalform.seasonweights_manual):
        generalform.s2022_weight = float(generalform.cleaned_data['s2022_weight'])
        generalform.s2021_weight = float(generalform.cleaned_data['s2021_weight'])
        generalform.s2020_weight = float(generalform.cleaned_data['s2020_weight'])
      else:
        generalform.s2022_weight = 100.000
        generalform.s2021_weight = 0
        generalform.s2020_weight = 0
      wgeneraldict['s2022_weight'] = generalform.s2022_weight
      request.session['s2022_weight'] = str(generalform.s2022_weight)
      wgeneraldict['s2021_weight'] = generalform.s2021_weight
      request.session['s2021_weight'] = str(generalform.s2021_weight)
      wgeneraldict['s2020_weight'] = generalform.s2020_weight
      request.session['s2020_weight'] = str(generalform.s2020_weight)

      #set plus or standard
      generalform.standard_park_adjusted = generalform.cleaned_data['standard_park_adjusted']
      wgeneraldict['standard_park_adjusted'] = generalform.standard_park_adjusted
      request.session['standard_park_adjusted'] = bool(generalform.standard_park_adjusted)

      generalform.plus_park_adjusted = generalform.cleaned_data['plus_park_adjusted']
      wgeneraldict['plus_park_adjusted'] = generalform.plus_park_adjusted
      request.session['plus_park_adjusted'] = bool(generalform.plus_park_adjusted)

      #set baserunning/fielding, as well as other weights
      generalform.bsrfld_auto = generalform.cleaned_data['bsrfld_auto']
      wgeneraldict['bsrfld_auto'] = generalform.bsrfld_auto
      request.session['bsrfld_auto'] = bool(generalform.bsrfld_auto)

      generalform.bsrfld_manual = generalform.cleaned_data['bsrfld_manual']
      wgeneraldict['bsrfld_manual'] = generalform.bsrfld_manual
      request.session['bsrfld_manual'] = bool(generalform.bsrfld_manual)

      if (generalform.bsrfld_manual):
        generalform.batting_weight = generalform.cleaned_data['batting_weight']
        wgeneraldict['batting_weight'] = generalform.batting_weight
        request.session['batting_weight'] = str(generalform.batting_weight)

        generalform.pitching_weight = generalform.cleaned_data['pitching_weight']
        wgeneraldict['pitching_weight'] = generalform.pitching_weight
        request.session['pitching_weight'] = str(generalform.pitching_weight)

        generalform.baserunning_weight = generalform.cleaned_data['baserunning_weight']
        wgeneraldict['baserunning_weight'] = generalform.baserunning_weight
        request.session['baserunning_weight'] = str(generalform.baserunning_weight)

        generalform.fielding_weight = generalform.cleaned_data['fielding_weight']
        wgeneraldict['fielding_weight'] = generalform.fielding_weight
        request.session['fielding_weight'] = str(generalform.fielding_weight)
      else:
        wgeneraldict['baserunning_weight'] = 4 #formerly 7.5
        request.session['baserunning_weight'] = 0

        wgeneraldict['fielding_weight'] = 10 #formerly 12.5
        request.session['fielding_weight'] = 0

        generalform.batting_weight = generalform.cleaned_data['batting_weight']
        wgeneraldict['batting_weight'] = float(generalform.batting_weight) * 0.86
        request.session['batting_weight'] = str(generalform.batting_weight)

        generalform.pitching_weight = generalform.cleaned_data['pitching_weight']
        wgeneraldict['pitching_weight'] = float(generalform.pitching_weight) * 0.86
        request.session['pitching_weight'] = str(generalform.pitching_weight)
      
      # print("bsr weight", wgeneraldict['baserunning_weight'])
      # print("fld weight", wgeneraldict['fielding_weight'])
      # print("pitch weight", wgeneraldict['pitching_weight'])
      # print("bat weight", wgeneraldict['batting_weight'])

      generalform.starterinnings = float(generalform.cleaned_data['starterinnings'])
      wgeneraldict['starterinnings'] = generalform.starterinnings
      request.session['starterinnings'] = str(generalform.starterinnings)

      generalform.variance = float(generalform.cleaned_data['variance'])
      wgeneraldict['variance'] = generalform.variance
      request.session['variance'] = str(generalform.variance)

    battingform = BattingWeightsForm(request.POST)
    if (battingform.is_valid()):
      #this dictionary will match the zbatter2022dict/zbatter2021dict/zbatter2020dict in models.py. they will share key names, and to get results iterate through them and multiply
      #need to work in the 'plus' as well
      wbatterdict = {}

      #avg
      battingform.bavg_weight = battingform.cleaned_data['bavg_weight']
      wbatterdict['zavg'] = battingform.bavg_weight
      request.session['bavg_weight'] = str(battingform.bavg_weight)

      #obp
      battingform.obp_weight = battingform.cleaned_data['obp_weight']
      wbatterdict['zobp'] = battingform.obp_weight
      request.session['obp_weight'] = str(battingform.obp_weight)

      #slg
      battingform.bslg_weight = battingform.cleaned_data['bslg_weight']
      wbatterdict['zslg'] = battingform.bslg_weight
      request.session['bslg_weight'] = str(battingform.bslg_weight)

      #ops
      battingform.ops_weight = battingform.cleaned_data['ops_weight']
      wbatterdict['zops'] = battingform.ops_weight
      request.session['ops_weight'] = str(battingform.ops_weight)

      #rperpa
      battingform.rperpa_weight = battingform.cleaned_data['rperpa_weight']
      wbatterdict['zr_per_pa'] = battingform.rperpa_weight
      request.session['rperpa_weight'] = str(battingform.rperpa_weight)

      #rbiperpa
      battingform.rbiperpa_weight = battingform.cleaned_data['rbiperpa_weight']
      wbatterdict['zrbi_per_pa'] = battingform.rbiperpa_weight
      request.session['rbiperpa_weight'] = str(battingform.rbiperpa_weight)

      #gdpperpa
      # battingform.gdpperpa_weight = battingform.cleaned_data['gdpperpa_weight']
      # wbatterdict['zgdp_per_pa'] = battingform.gdpperpa_weight
      # request.session['gdpperpa_weight'] = str(battingform.gdpperpa_weight)

      #bbperpa
      battingform.bbperpa_weight = battingform.cleaned_data['bbperpa_weight']
      wbatterdict['zbb_per_pa'] = battingform.bbperpa_weight
      request.session['bbperpa_weight'] = str(battingform.bbperpa_weight)

      #kperpa
      battingform.kperpa_weight = battingform.cleaned_data['kperpa_weight']
      wbatterdict['zk_per_pa'] = battingform.kperpa_weight
      request.session['kperpa_weight'] = str(battingform.kperpa_weight)

      #chaserate
      battingform.chaserate_weight = battingform.cleaned_data['chaserate_weight']
      wbatterdict['zoutsidezoneswingpercent'] = battingform.chaserate_weight
      request.session['chaserate_weight'] = str(battingform.chaserate_weight)

      #firstpitchstrike
      battingform.firstpitchstrike_weight = battingform.cleaned_data['firstpitchstrike_weight']
      wbatterdict['zfirstpitchstrikepercent'] = battingform.firstpitchstrike_weight
      request.session['firstpitchstrike_weight'] = str(battingform.firstpitchstrike_weight)

      #swingcontact
      battingform.swingcontact_weight = battingform.cleaned_data['swingcontact_weight']
      wbatterdict['zswingcontactpercent'] = battingform.swingcontact_weight
      request.session['swingcontact_weight'] = str(battingform.swingcontact_weight)

      #swingingstrike
      battingform.swingingstrike_weight = battingform.cleaned_data['swingingstrike_weight']
      wbatterdict['zswingingstrikespercent'] = battingform.swingingstrike_weight
      request.session['swingingstrike_weight'] = str(battingform.swingingstrike_weight)

      # BATTED BALL

      #babip
      battingform.bbabip_weight = battingform.cleaned_data['bbabip_weight']
      wbatterdict['zbabip'] = battingform.bbabip_weight
      request.session['bbabip_weight'] = str(battingform.bbabip_weight)
  
      #ld_per_bip
      battingform.ld_per_bip_weight = battingform.cleaned_data['ld_per_bip_weight']
      wbatterdict['zld_per_bip'] = battingform.ld_per_bip_weight
      request.session['ld_per_bip_weight'] = str(battingform.ld_per_bip_weight)
  
      #gb_per_bip
      battingform.gb_per_bip_weight = battingform.cleaned_data['gb_per_bip_weight']
      wbatterdict['zgb_per_bip'] = battingform.gb_per_bip_weight
      request.session['gb_per_bip_weight'] = str(battingform.gb_per_bip_weight)
  
      #fb_per_bip
      battingform.fb_per_bip_weight = battingform.cleaned_data['fb_per_bip_weight']
      wbatterdict['zfb_per_bip'] = battingform.fb_per_bip_weight
      request.session['fb_per_bip_weight'] = str(battingform.fb_per_bip_weight)
  
      #iffb_per_bip
      battingform.iffb_per_bip_weight = battingform.cleaned_data['iffb_per_bip_weight']
      wbatterdict['ziffb_per_bip'] = battingform.iffb_per_bip_weight
      request.session['iffb_per_bip_weight'] = str(battingform.iffb_per_bip_weight)
  
      #hr_per_fb
      battingform.hr_per_fb_weight = battingform.cleaned_data['hr_per_fb_weight']
      wbatterdict['zhr_per_fb'] = battingform.hr_per_fb_weight
      request.session['hr_per_fb_weight'] = str(battingform.hr_per_fb_weight)
  
      #hardpercent
      # battingform.hardpercent_weight = battingform.cleaned_data['hardpercent_weight']
      # wbatterdict['zhardpercent'] = battingform.hardpercent_weight
      # request.session['hardpercent_weight'] = str(battingform.hardpercent_weight)
  
      #hardhitpercent
      battingform.bhardhitpercent_weight = battingform.cleaned_data['bhardhitpercent_weight']
      wbatterdict['zhardhitpercent'] = battingform.bhardhitpercent_weight
      request.session['bhardhitpercent_weight'] = str(battingform.bhardhitpercent_weight)
  
      #anglesweetspotpercent
      battingform.banglesweetspotpercent_weight = battingform.cleaned_data['banglesweetspotpercent_weight']
      wbatterdict['zanglesweetspotpercent'] = battingform.banglesweetspotpercent_weight
      request.session['banglesweetspotpercent_weight'] = str(battingform.banglesweetspotpercent_weight)
  
      #avg_hit_speed
      battingform.avg_hit_speed_weight = battingform.cleaned_data['avg_hit_speed_weight']
      wbatterdict['zavg_hit_speed'] = battingform.avg_hit_speed_weight
      request.session['avg_hit_speed_weight'] = str(battingform.avg_hit_speed_weight)
  
      #avg_distance
      battingform.avg_distance_weight = battingform.cleaned_data['avg_distance_weight']
      wbatterdict['zavg_distance'] = battingform.avg_distance_weight
      request.session['avg_distance_weight'] = str(battingform.avg_distance_weight)
  
      #ev95percent
      battingform.ev95percent_weight = battingform.cleaned_data['ev95percent_weight']
      wbatterdict['zev95percent'] = battingform.ev95percent_weight
      request.session['ev95percent_weight'] = str(battingform.ev95percent_weight)
  
      #brl_percent
      battingform.brl_percent_weight = battingform.cleaned_data['brl_percent_weight']
      wbatterdict['zbrl_percent'] = battingform.brl_percent_weight
      request.session['brl_percent_weight'] = str(battingform.brl_percent_weight)

      #AGGREGATE
      #wRAA
      battingform.wRAA_weight = battingform.cleaned_data['wRAA_weight']
      wbatterdict['zwRAA'] = battingform.wRAA_weight
      request.session['wRAA_weight'] = str(battingform.wRAA_weight)
  
      #wOBA
      battingform.wOBA_weight = battingform.cleaned_data['wOBA_weight']
      wbatterdict['zwOBA'] = battingform.wOBA_weight
      request.session['wOBA_weight'] = str(battingform.wOBA_weight)
  
      #wRC
      battingform.wRC_weight = battingform.cleaned_data['wRC_weight']
      wbatterdict['zwRC'] = battingform.wRC_weight
      request.session['wRC_weight'] = str(battingform.wRC_weight)
  
      #iso
      battingform.iso_weight = battingform.cleaned_data['iso_weight']
      wbatterdict['ziso'] = battingform.iso_weight
      request.session['iso_weight'] = str(battingform.iso_weight)
  
      #xwoba
      battingform.bxwoba_weight = battingform.cleaned_data['bxwoba_weight']
      wbatterdict['zxwoba'] = battingform.bxwoba_weight
      request.session['bxwoba_weight'] = str(battingform.bxwoba_weight)
  
      #xavg
      battingform.bxavg_weight = battingform.cleaned_data['bxavg_weight']
      wbatterdict['zxavg'] = battingform.bxavg_weight
      request.session['bxavg_weight'] = str(battingform.bxavg_weight)
  
      #xslg
      battingform.bxslg_weight = battingform.cleaned_data['bxslg_weight']
      wbatterdict['zxslg'] = battingform.bxslg_weight
      request.session['bxslg_weight'] = str(battingform.bxslg_weight)
  
      #clutch
      battingform.bclutch_weight = battingform.cleaned_data['bclutch_weight']
      wbatterdict['zclutch'] = battingform.bclutch_weight
      request.session['bclutch_weight'] = str(battingform.bclutch_weight)
  
      #fbat_per_pa
      battingform.fbat_per_pa_weight = battingform.cleaned_data['fbat_per_pa_weight']
      wbatterdict['zfbat_per_pa'] = battingform.fbat_per_pa_weight
      request.session['fbat_per_pa_weight'] = str(battingform.fbat_per_pa_weight)
  
      #bref_batting_runs_per_pa
      battingform.bref_batting_runs_per_pa_weight = battingform.cleaned_data['bref_batting_runs_per_pa_weight']
      wbatterdict['zbref_batting_runs_per_pa'] = battingform.bref_batting_runs_per_pa_weight
      request.session['bref_batting_runs_per_pa_weight'] = str(battingform.bref_batting_runs_per_pa_weight)
  
      #max_distance
      battingform.max_distance_weight = battingform.cleaned_data['max_distance_weight']
      wbatterdict['zmax_distance'] = battingform.max_distance_weight
      request.session['max_distance_weight'] = str(battingform.max_distance_weight)
  
      #max_hit_speed
      battingform.max_hit_speed_weight = battingform.cleaned_data['max_hit_speed_weight']
      wbatterdict['zmax_hit_speed'] = battingform.max_hit_speed_weight
      request.session['max_hit_speed_weight'] = str(battingform.max_hit_speed_weight)
  
      #brl_pa
      # battingform.brl_pa_weight = battingform.cleaned_data['brl_pa_weight']
      # wbatterdict['zbrl_pa'] = battingform.brl_pa_weight
      # request.session['brl_pa_weight'] = str(battingform.brl_pa_weight)

      wbaserunningdict = {}

      #BASERUNNING
      #xSB_added
      # battingform.xSB_added_weight = battingform.cleaned_data['xSB_added_weight']
      # wbaserunningdict['zxSB_added'] = battingform.xSB_added_weight
      # request.session['xSB_added_weight'] = str(battingform.xSB_added_weight)
  
      #xSB_added_percent
      battingform.xSB_added_percent_weight = battingform.cleaned_data['xSB_added_percent_weight']
      wbaserunningdict['zxSB_added_percent'] = battingform.xSB_added_percent_weight
      request.session['xSB_added_percent_weight'] = str(battingform.xSB_added_percent_weight)
  
      #spd
      battingform.spd_weight = battingform.cleaned_data['spd_weight']
      wbaserunningdict['zspd'] = battingform.spd_weight
      request.session['spd_weight'] = str(battingform.spd_weight)
  
      #bsr_per_pa
      battingform.bsr_per_pa_weight = battingform.cleaned_data['bsr_per_pa_weight']
      wbaserunningdict['zbsr_per_pa'] = battingform.bsr_per_pa_weight
      request.session['bsr_per_pa_weight'] = str(battingform.bsr_per_pa_weight)
  
      #bref_bsr_runs_per_pa
      battingform.bref_bsr_runs_per_pa_weight = battingform.cleaned_data['bref_bsr_runs_per_pa_weight']
      wbaserunningdict['zbref_bsr_runs_per_pa'] = battingform.bref_bsr_runs_per_pa_weight
      request.session['bref_bsr_runs_per_pa_weight'] = str(battingform.bref_bsr_runs_per_pa_weight)
  
      #home_to_first
      battingform.home_to_first_weight = battingform.cleaned_data['home_to_first_weight']
      wbaserunningdict['zhome_to_first'] = battingform.home_to_first_weight
      request.session['home_to_first_weight'] = str(battingform.home_to_first_weight)
  
      #sprint_speed
      # battingform.sprint_speed_weight = battingform.cleaned_data['sprint_speed_weight']
      # wbaserunningdict['zsprint_speed'] = battingform.sprint_speed_weight
      # request.session['sprint_speed_weight'] = str(battingform.sprint_speed_weight)

      wfieldingdict = {}

      #fielding
      #outs_above_avg
      battingform.outs_above_avg_weight = battingform.cleaned_data['outs_above_avg_weight']
      wfieldingdict['zouts_above_avg'] = battingform.outs_above_avg_weight
      request.session['outs_above_avg_weight'] = str(battingform.outs_above_avg_weight)
      #fielding_runs_prevented
      battingform.fielding_runs_prevented_weight = battingform.cleaned_data['fielding_runs_prevented_weight']
      wfieldingdict['zfielding_runs_prevented'] = battingform.fielding_runs_prevented_weight
      request.session['fielding_runs_prevented_weight'] = str(battingform.fielding_runs_prevented_weight)
      #ffld_per_pa
      # battingform.ffld_per_pa_weight = battingform.cleaned_data['ffld_per_pa_weight']
      # wfieldingdict['zffld_per_pa'] = battingform.ffld_per_pa_weight
      # request.session['ffld_per_pa_weight'] = str(battingform.ffld_per_pa_weight)
      #fdef_per_pa
      battingform.fdef_per_pa_weight = battingform.cleaned_data['fdef_per_pa_weight']
      wfieldingdict['zfdef_per_pa'] = battingform.fdef_per_pa_weight
      request.session['fdef_per_pa_weight'] = str(battingform.fdef_per_pa_weight)
      #bref_war_def_per_pa
      battingform.bref_war_def_per_pa_weight = battingform.cleaned_data['bref_war_def_per_pa_weight']
      wfieldingdict['zbref_war_def_per_pa'] = battingform.bref_war_def_per_pa_weight
      request.session['bref_war_def_per_pa_weight'] = str(battingform.bref_war_def_per_pa_weight)



    #PITCHING
    pitchingform = PitchingWeightsForm(request.POST)
    if (pitchingform.is_valid()):
      #this dictionary will match the zpitcher2022dict/zpitcher2021dict/zpitcher2020dict in models.py. they will share key names, and to get results iterate through them and multiply
      #need to work in the 'plus' as well
      wpitcherdict = {}
      #winningpercent
      pitchingform.winningpercent_weight = pitchingform.cleaned_data['winningpercent_weight']
      wpitcherdict['zwinningpercent'] = pitchingform.winningpercent_weight
      request.session['winningpercent_weight'] = str(pitchingform.winningpercent_weight)
  
      #shutouts
      # pitchingform.shutouts_weight = pitchingform.cleaned_data['shutouts_weight']
      # wpitcherdict['zshutouts'] = pitchingform.shutouts_weight
      # request.session['shutouts_weight'] = str(pitchingform.shutouts_weight)
  
      #hitpernine
      pitchingform.hitpernine_weight = pitchingform.cleaned_data['hitpernine_weight']
      wpitcherdict['zhitpernine'] = pitchingform.hitpernine_weight
      request.session['hitpernine_weight'] = str(pitchingform.hitpernine_weight)
  
      #bbpernine
      # pitchingform.bbpernine_weight = pitchingform.cleaned_data['bbpernine_weight']
      # wpitcherdict['zbbpernine'] = pitchingform.bbpernine_weight
      # request.session['bbpernine_weight'] = str(pitchingform.bbpernine_weight)
  
      #kpernine
      # pitchingform.kpernine_weight = pitchingform.cleaned_data['kpernine_weight']
      # wpitcherdict['zkpernine'] = pitchingform.kpernine_weight
      # request.session['kpernine_weight'] = str(pitchingform.kpernine_weight)
  
      #hrpernine
      pitchingform.hrpernine_weight = pitchingform.cleaned_data['hrpernine_weight']
      wpitcherdict['zhrpernine'] = pitchingform.hrpernine_weight
      request.session['hrpernine_weight'] = str(pitchingform.hrpernine_weight)
  
      #kperbb
      pitchingform.kperbb_weight = pitchingform.cleaned_data['kperbb_weight']
      wpitcherdict['zkperbb'] = pitchingform.kperbb_weight
      request.session['kperbb_weight'] = str(pitchingform.kperbb_weight)
  
      #avg
      pitchingform.avg_weight = pitchingform.cleaned_data['avg_weight']
      wpitcherdict['zavg'] = pitchingform.avg_weight
      request.session['avg_weight'] = str(pitchingform.avg_weight)
  
      #whip
      pitchingform.whip_weight = pitchingform.cleaned_data['whip_weight']
      wpitcherdict['zwhip'] = pitchingform.whip_weight
      request.session['whip_weight'] = str(pitchingform.whip_weight)
  
      #lobpercent
      pitchingform.lobpercent_weight = pitchingform.cleaned_data['lobpercent_weight']
      wpitcherdict['zlobpercent'] = pitchingform.lobpercent_weight
      request.session['lobpercent_weight'] = str(pitchingform.lobpercent_weight)
  
      #thrownforkpercent
      # pitchingform.thrownforkpercent_weight = pitchingform.cleaned_data['thrownforkpercent_weight']
      # wpitcherdict['zthrownforkpercent'] = pitchingform.thrownforkpercent_weight
      # request.session['thrownforkpercent_weight'] = str(pitchingform.thrownforkpercent_weight)
  
      #cswpercent
      pitchingform.cswpercent_weight = pitchingform.cleaned_data['cswpercent_weight']
      wpitcherdict['zcswpercent'] = pitchingform.cswpercent_weight
      request.session['cswpercent_weight'] = str(pitchingform.cswpercent_weight)
  
      #outsidezoneswingpercent
      pitchingform.outsidezoneswingpercent_weight = pitchingform.cleaned_data['outsidezoneswingpercent_weight']
      wpitcherdict['zoutsidezoneswingpercent'] = pitchingform.outsidezoneswingpercent_weight
      request.session['outsidezoneswingpercent_weight'] = str(pitchingform.outsidezoneswingpercent_weight)
  
      #firstpitchstrikepercent
      pitchingform.firstpitchstrikepercent_weight = pitchingform.cleaned_data['firstpitchstrikepercent_weight']
      wpitcherdict['zfirstpitchstrikepercent'] = pitchingform.firstpitchstrikepercent_weight
      request.session['firstpitchstrikepercent_weight'] = str(pitchingform.firstpitchstrikepercent_weight)
        #swingingstrikespercent
      pitchingform.swingingstrikespercent_weight = pitchingform.cleaned_data['swingingstrikespercent_weight']
      wpitcherdict['zswingingstrikespercent'] = pitchingform.swingingstrikespercent_weight
      request.session['swingingstrikespercent_weight'] = str(pitchingform.swingingstrikespercent_weight)
        #bbpercent
      pitchingform.bbpercent_weight = pitchingform.cleaned_data['bbpercent_weight']
      wpitcherdict['zbbpercent'] = pitchingform.bbpercent_weight
      request.session['bbpercent_weight'] = str(pitchingform.bbpercent_weight)
        #kpercent
      pitchingform.kpercent_weight = pitchingform.cleaned_data['kpercent_weight']
      wpitcherdict['zkpercent'] = pitchingform.kpercent_weight
      request.session['kpercent_weight'] = str(pitchingform.kpercent_weight)
        #slg
      pitchingform.slg_weight = pitchingform.cleaned_data['slg_weight']
      wpitcherdict['zslg'] = pitchingform.slg_weight
      request.session['slg_weight'] = str(pitchingform.slg_weight)

      #BATTED BALLS
        #babip
      pitchingform.babip_weight = pitchingform.cleaned_data['babip_weight']
      wpitcherdict['zbabip'] = pitchingform.babip_weight
      request.session['babip_weight'] = str(pitchingform.babip_weight)
        #gbperfb
      # pitchingform.gbperfb_weight = pitchingform.cleaned_data['gbperfb_weight']
      # wpitcherdict['zgbperfb'] = pitchingform.gbperfb_weight
      # request.session['gbperfb_weight'] = str(pitchingform.gbperfb_weight)
        #hrperfb
      pitchingform.hrperfb_weight = pitchingform.cleaned_data['hrperfb_weight']
      wpitcherdict['zhrperfb'] = pitchingform.hrperfb_weight
      request.session['hrperfb_weight'] = str(pitchingform.hrperfb_weight)
        #gbpercent
      pitchingform.gbpercent_weight = pitchingform.cleaned_data['gbpercent_weight']
      wpitcherdict['zgbpercent'] = pitchingform.gbpercent_weight
      request.session['gbpercent_weight'] = str(pitchingform.gbpercent_weight)
        #iffbpercent
      pitchingform.iffbpercent_weight = pitchingform.cleaned_data['iffbpercent_weight']
      wpitcherdict['ziffbpercent'] = pitchingform.iffbpercent_weight
      request.session['iffbpercent_weight'] = str(pitchingform.iffbpercent_weight)
        #ldpercent
      pitchingform.ldpercent_weight = pitchingform.cleaned_data['ldpercent_weight']
      wpitcherdict['zldpercent'] = pitchingform.ldpercent_weight
      request.session['ldpercent_weight'] = str(pitchingform.ldpercent_weight)
        #fbpercent
      pitchingform.fbpercent_weight = pitchingform.cleaned_data['fbpercent_weight']
      wpitcherdict['zfbpercent'] = pitchingform.fbpercent_weight
      request.session['fbpercent_weight'] = str(pitchingform.fbpercent_weight)
        #softpercent
      pitchingform.softpercent_weight = pitchingform.cleaned_data['softpercent_weight']
      wpitcherdict['zsoftpercent'] = pitchingform.softpercent_weight
      request.session['softpercent_weight'] = str(pitchingform.softpercent_weight)
      #softplusmediumpercent
      pitchingform.softplusmediumpercent_weight = pitchingform.cleaned_data['softplusmediumpercent_weight']
      wpitcherdict['zsoftplusmediumpercent'] = pitchingform.softplusmediumpercent_weight
      request.session['softplusmediumpercent_weight'] = str(pitchingform.softplusmediumpercent_weight)
        #weakpercent
      # pitchingform.weakpercent_weight = pitchingform.cleaned_data['weakpercent_weight']
      # wpitcherdict['zweakpercent'] = pitchingform.weakpercent_weight
      # request.session['weakpercent_weight'] = str(pitchingform.weakpercent_weight)
        #barrel_percent
      pitchingform.barrel_percent_weight = pitchingform.cleaned_data['barrel_percent_weight']
      wpitcherdict['zbarrel_percent'] = pitchingform.barrel_percent_weight
      request.session['barrel_percent_weight'] = str(pitchingform.barrel_percent_weight)
        #hardhitpercent
      pitchingform.hardhitpercent_weight = pitchingform.cleaned_data['hardhitpercent_weight']
      wpitcherdict['zhardhitpercent'] = pitchingform.hardhitpercent_weight
      request.session['hardhitpercent_weight'] = str(pitchingform.hardhitpercent_weight)
        #averageev
      pitchingform.averageev_weight = pitchingform.cleaned_data['averageev_weight']
      wpitcherdict['zaverageev'] = pitchingform.averageev_weight
      request.session['averageev_weight'] = str(pitchingform.averageev_weight)
        #averagela
      # pitchingform.averagela_weight = pitchingform.cleaned_data['averagela_weight']
      # wpitcherdict['zaveragela'] = pitchingform.averagela_weight
      # request.session['averagela_weight'] = str(pitchingform.averagela_weight)
        #anglesweetspotpercent
      pitchingform.anglesweetspotpercent_weight = pitchingform.cleaned_data['anglesweetspotpercent_weight']
      wpitcherdict['zanglesweetspotpercent'] = pitchingform.anglesweetspotpercent_weight
      request.session['anglesweetspotpercent_weight'] = str(pitchingform.anglesweetspotpercent_weight)
        #avgdistance
      pitchingform.avgdistance_weight = pitchingform.cleaned_data['avgdistance_weight']
      wpitcherdict['zavgdistance'] = pitchingform.avgdistance_weight
      request.session['avgdistance_weight'] = str(pitchingform.avgdistance_weight)
        #ev95pluspercent
      pitchingform.ev95pluspercent_weight = pitchingform.cleaned_data['ev95pluspercent_weight']
      wpitcherdict['zev95pluspercent'] = pitchingform.ev95pluspercent_weight
      request.session['ev95pluspercent_weight'] = str(pitchingform.ev95pluspercent_weight)
        #brlperpa
      # pitchingform.brlperpa_weight = pitchingform.cleaned_data['brlperpa_weight']
      # wpitcherdict['zbrlperpa'] = pitchingform.brlperpa_weight
      # request.session['brlperpa_weight'] = str(pitchingform.brlperpa_weight)

      #AGGREGATE
        #era
      pitchingform.era_weight = pitchingform.cleaned_data['era_weight']
      wpitcherdict['zera'] = pitchingform.era_weight
      request.session['era_weight'] = str(pitchingform.era_weight)
        #xera
      pitchingform.xera_weight = pitchingform.cleaned_data['xera_weight']
      wpitcherdict['zxera'] = pitchingform.xera_weight
      request.session['xera_weight'] = str(pitchingform.xera_weight)
        #runsaverage
      pitchingform.runsaverage_weight = pitchingform.cleaned_data['runsaverage_weight']
      wpitcherdict['zrunsaverage'] = pitchingform.runsaverage_weight
      request.session['runsaverage_weight'] = str(pitchingform.runsaverage_weight)

             #war
      pitchingform.war_weight = pitchingform.cleaned_data['war_weight']
      wpitcherdict['zwar'] = pitchingform.war_weight
      request.session['war_weight'] = str(pitchingform.war_weight)
        #fip
      pitchingform.fip_weight = pitchingform.cleaned_data['fip_weight']
      wpitcherdict['zfip'] = pitchingform.fip_weight
      request.session['fip_weight'] = str(pitchingform.fip_weight)
        #xfip
      pitchingform.xfip_weight = pitchingform.cleaned_data['xfip_weight']
      wpitcherdict['zxfip'] = pitchingform.xfip_weight
      request.session['xfip_weight'] = str(pitchingform.xfip_weight)
        #siera
      pitchingform.siera_weight = pitchingform.cleaned_data['siera_weight']
      wpitcherdict['zsiera'] = pitchingform.siera_weight
      request.session['siera_weight'] = str(pitchingform.siera_weight)
      #rar
      pitchingform.rar_weight = pitchingform.cleaned_data['rar_weight']
      wpitcherdict['zrar'] = pitchingform.rar_weight
      request.session['rar_weight'] = str(pitchingform.rar_weight)
        #tera
      pitchingform.tera_weight = pitchingform.cleaned_data['tera_weight']
      wpitcherdict['ztera'] = pitchingform.tera_weight
      request.session['tera_weight'] = str(pitchingform.tera_weight)
        #wpa
      pitchingform.wpa_weight = pitchingform.cleaned_data['wpa_weight']
      wpitcherdict['zwpa'] = pitchingform.wpa_weight
      request.session['wpa_weight'] = str(pitchingform.wpa_weight)
        #retwentyfour
      pitchingform.retwentyfour_weight = pitchingform.cleaned_data['retwentyfour_weight']
      wpitcherdict['zretwentyfour'] = pitchingform.retwentyfour_weight
      request.session['retwentyfour_weight'] = str(pitchingform.retwentyfour_weight)
        #clutch
      pitchingform.clutch_weight = pitchingform.cleaned_data['clutch_weight']
      wpitcherdict['zclutch'] = pitchingform.clutch_weight
      request.session['clutch_weight'] = str(pitchingform.clutch_weight)
        #kwera
      pitchingform.kwera_weight = pitchingform.cleaned_data['kwera_weight']
      wpitcherdict['zkwera'] = pitchingform.kwera_weight
      request.session['kwera_weight'] = str(pitchingform.kwera_weight)
        #woba
      pitchingform.woba_weight = pitchingform.cleaned_data['woba_weight']
      wpitcherdict['zwoba'] = pitchingform.woba_weight
      request.session['woba_weight'] = str(pitchingform.woba_weight)
        #xavg
      pitchingform.xavg_weight = pitchingform.cleaned_data['xavg_weight']
      wpitcherdict['zxavg'] = pitchingform.xavg_weight
      request.session['xavg_weight'] = str(pitchingform.xavg_weight)
        #xslg
      pitchingform.xslg_weight = pitchingform.cleaned_data['xslg_weight']
      wpitcherdict['zxslg'] = pitchingform.xslg_weight
      request.session['xslg_weight'] = str(pitchingform.xslg_weight)
        #xwoba
      pitchingform.xwoba_weight = pitchingform.cleaned_data['xwoba_weight']
      wpitcherdict['zxwoba'] = pitchingform.xwoba_weight
      request.session['xwoba_weight'] = str(pitchingform.xwoba_weight)


    #FIELDING
    teamform = TeamWeightsForm(request.POST)
    if (teamform.is_valid()):
      wteamdict = {}
      #errors
      teamform.errors_weight = teamform.cleaned_data['errors_weight']
      wteamdict['zerrors'] = teamform.errors_weight
      request.session['errors_weight'] = str(teamform.errors_weight)
        #doubleplays
      teamform.doubleplays_weight = teamform.cleaned_data['doubleplays_weight']
      wteamdict['zdoubleplays'] = teamform.doubleplays_weight
      request.session['doubleplays_weight'] = str(teamform.doubleplays_weight)
        #fieldingpercentage
      teamform.fieldingpercentage_weight = teamform.cleaned_data['fieldingpercentage_weight']
      wteamdict['zfieldingpercentage'] = teamform.fieldingpercentage_weight
      request.session['fieldingpercentage_weight'] = str(teamform.fieldingpercentage_weight)
        #xsbsavedagainst
      teamform.xsbsavedagainst_weight = teamform.cleaned_data['xsbsavedagainst_weight']
      wteamdict['zxsbsavedagainst'] = teamform.xsbsavedagainst_weight
      request.session['xsbsavedagainst_weight'] = str(teamform.xsbsavedagainst_weight)
        #wildpitchespluspassedballs
      teamform.wildpitchespluspassedballs_weight = teamform.cleaned_data['wildpitchespluspassedballs_weight']
      wteamdict['zwildpitchespluspassedballs'] = teamform.wildpitchespluspassedballs_weight
      request.session['wildpitchespluspassedballs_weight'] = str(teamform.wildpitchespluspassedballs_weight)
        #defensiverunssaved
      teamform.defensiverunssaved_weight = teamform.cleaned_data['defensiverunssaved_weight']
      wteamdict['zdefensiverunssaved'] = teamform.defensiverunssaved_weight
      request.session['defensiverunssaved_weight'] = str(teamform.defensiverunssaved_weight)
        #ultimatezonerating
      teamform.ultimatezonerating_weight = teamform.cleaned_data['ultimatezonerating_weight']
      wteamdict['zultimatezonerating'] = teamform.ultimatezonerating_weight
      request.session['ultimatezonerating_weight'] = str(teamform.ultimatezonerating_weight)
        #defense
      teamform.defense_weight = teamform.cleaned_data['defense_weight']
      wteamdict['zdefense'] = teamform.defense_weight
      request.session['defense_weight'] = str(teamform.defense_weight)



      request.session.modified = True

      #only one of the below error messages will appear at a time. Is that a big deal? I don't think so. Someone will fix one problem, and then be instructed to fix another problem. doesn't seem too annoying

      #validate the input for season weight
      seasonweightsum = generalform.s2022_weight + generalform.s2021_weight + generalform.s2020_weight
      if seasonweightsum == 100:
        pass
      else:
        featureerror = "ERROR: The season weight values entered must sum to 100!"
        featureerrordetails = "The % season values did not sum to 100. The sum is " + str(seasonweightsum) + ". Please ensure the values entered in Season % Weight sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input for category weight
      if generalform.bsrfld_auto == True:
        categoryweightsum = generalform.batting_weight + generalform.pitching_weight
      else:
        categoryweightsum = generalform.batting_weight + generalform.pitching_weight + generalform.baserunning_weight + generalform.fielding_weight
      if categoryweightsum == 100:
        pass
      else:
        featureerror = "ERROR: The batting/pitching/baserunning/fielding weight values must sum to 100!"
        featureerrordetails = "The % values entered do not sum to 100. The sum is " + str(categoryweightsum) + ". Please ensure the values entered in Category % Weights sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input of starting pitcher IP
      if generalform.starterinnings % 1 > 0.29 and generalform.starterinnings % 1 < 0.99:
        featureerror = "ERROR: The Starting Pitcher IP value must be a whole number, end in 0.1, or end in 0.2!"
        featureerrordetails = "The value entered is not a valid IP value. The value is " + str(generalform.starterinnings) + ". Please ensure the value entered in Starting Pitcher IP is valid."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input for batting
      battingsum = input_valid(wbatterdict)
      if battingsum == 100:
        pass
      else:
        featureerror = "ERROR: The Batting values must sum to 100!"
        featureerrordetails = "The % batting values entered do not sum to 100. The sum is " + str(battingsum) + ". Please ensure the values entered in Batting % Weight sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input for baserunning
      baserunningsum = input_valid(wbaserunningdict)
      if baserunningsum == 100:
        pass
      else:
        featureerror = "ERROR: The Baserunning values must sum to 100!"
        featureerrordetails = "The % baserunning values entered do not sum to 100. The sum is " + str(baserunningsum) + ". Please ensure the values entered in Baserunning % Weight sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input for pitching
      pitchingsum = input_valid(wpitcherdict)
      if pitchingsum == 100:
        pass
      else:
        featureerror = "ERROR: The Pitching values must sum to 100!"
        featureerrordetails = "The % pitching values entered do not sum to 100. The sum is " + str(pitchingsum) + ". Please ensure the values entered in Pitching % Weight sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)

      #validate the input for fielding, first must combine individual and team fielding metrics
      wcheckfieldingdict = {}
      wcheckfieldingdict.update(wfieldingdict)
      wcheckfieldingdict.update(wteamdict)
      fieldingsum = input_valid(wcheckfieldingdict)
      if fieldingsum == 100:
        #all the input has been checked as valid, so call the simulation
        request.session["gameresults"] = todaysimulation(wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict)
        # return HttpResponseRedirect('/loading/')
        #load all dictionaries into request.session (for other purposes, such as single-game simulation)
        request.session['wbatterdict'] = pickle.dumps(wbatterdict).hex()
        # print(wbatterdict)
        # print(pickle.loads(bytes.fromhex(request.session['wbatterdict'])))
        # print(request.session['wbatterdict'])
        request.session['wbaserunningdict'] = pickle.dumps(wbaserunningdict).hex()
        request.session['wfieldingdict'] = pickle.dumps(wfieldingdict).hex()
        request.session['wpitcherdict'] = pickle.dumps(wpitcherdict).hex()
        request.session['wteamdict'] = pickle.dumps(wteamdict).hex()
        request.session['wgeneraldict'] = pickle.dumps(wgeneraldict).hex()
        return HttpResponseRedirect('/results/')
      else:
        featureerror = "ERROR: The Fielding values must sum to 100!"
        featureerrordetails = "The % fielding values entered do not sum to 100. The sum is " + str(fieldingsum) + ". Please ensure the values entered in Fielding % Weight sum to 100."
        context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform, 'featureerror':featureerror, 'featureerrordetails':featureerrordetails}
        return render(request, 'workshop.html', context)
        
      
  #otherwise, it's a get request
  else:
    #check if request session exists using any variable
    if 'homefield_auto' in request.session:
      generalform = GeneralWeightsForm(initial={
        'homefield_auto':request.session['homefield_auto'],
        'homefield_manual':request.session['homefield_manual'],
        'homefield_none':request.session['homefield_none'],
        'homefield_weight':request.session['homefield_weight'],
        'seasonweights_auto':request.session['seasonweights_auto'],
        'seasonweights_manual':request.session['seasonweights_manual'],
        'seasonweights_current':request.session['seasonweights_current'],
        's2022_weight':request.session['s2022_weight'],
        's2021_weight':request.session['s2021_weight'],
        's2020_weight':request.session['s2020_weight'],
        'standard_park_adjusted':request.session['standard_park_adjusted'],
        'plus_park_adjusted':request.session['plus_park_adjusted'],
        'bsrfld_auto':request.session['bsrfld_auto'],
        'bsrfld_manual':request.session['bsrfld_manual'],
        'batting_weight':request.session['batting_weight'],
        'pitching_weight':request.session['pitching_weight'],
        'baserunning_weight':request.session['baserunning_weight'],
        'fielding_weight':request.session['fielding_weight'],
        'starterinnings':request.session['starterinnings'],
        'variance':request.session['variance']
      })
    else: generalform = GeneralWeightsForm()

    if 'bavg_weight' in request.session:
      battingform = BattingWeightsForm(initial={
        'bavg_weight':request.session['bavg_weight'], 
        'obp_weight':request.session['obp_weight'], 
        'bslg_weight':request.session['bslg_weight'], 
        'ops_weight':request.session['ops_weight'], 
        'rperpa_weight':request.session['rperpa_weight'], 
        'rbiperpa_weight':request.session['rbiperpa_weight'], 
        # 'gdpperpa_weight':request.session['gdpperpa_weight'], 
        'bbperpa_weight':request.session['bbperpa_weight'], 
        'kperpa_weight':request.session['kperpa_weight'], 
        'chaserate_weight':request.session['chaserate_weight'], 
        'firstpitchstrike_weight':request.session['firstpitchstrike_weight'], 
        'swingcontact_weight':request.session['swingcontact_weight'], 
        'swingingstrike_weight':request.session['swingingstrike_weight'],
        'bbabip_weight':request.session['bbabip_weight'],
        'ld_per_bip_weight':request.session['ld_per_bip_weight'],
        'gb_per_bip_weight':request.session['gb_per_bip_weight'],
        'fb_per_bip_weight':request.session['fb_per_bip_weight'],
        'iffb_per_bip_weight':request.session['iffb_per_bip_weight'],
        'hr_per_fb_weight':request.session['hr_per_fb_weight'],
        # 'hardpercent_weight':request.session['hardpercent_weight'],
        'bhardhitpercent_weight':request.session['bhardhitpercent_weight'],
        'banglesweetspotpercent_weight':request.session['banglesweetspotpercent_weight'],
        'avg_hit_speed_weight':request.session['avg_hit_speed_weight'],
        'avg_distance_weight':request.session['avg_distance_weight'],
        'ev95percent_weight':request.session['ev95percent_weight'],
        'brl_percent_weight':request.session['brl_percent_weight'],
        'wRAA_weight':request.session['wRAA_weight'],
        'wOBA_weight':request.session['wOBA_weight'],
        'wRC_weight':request.session['wRC_weight'],
        'iso_weight':request.session['iso_weight'],
        'bxwoba_weight':request.session['bxwoba_weight'],
        'bxavg_weight':request.session['bxavg_weight'],
        'bxslg_weight':request.session['bxslg_weight'],
        'bclutch_weight':request.session['bclutch_weight'],
        'fbat_per_pa_weight':request.session['fbat_per_pa_weight'],
        'bref_batting_runs_per_pa_weight':request.session['bref_batting_runs_per_pa_weight'],
        'max_distance_weight':request.session['max_distance_weight'],
        'max_hit_speed_weight':request.session['max_hit_speed_weight'],
        # 'brl_pa_weight':request.session['brl_pa_weight'],
        # 'xSB_added_weight':request.session['xSB_added_weight'],
        'xSB_added_percent_weight':request.session['xSB_added_percent_weight'],
        'spd_weight':request.session['spd_weight'],
        'bsr_per_pa_weight':request.session['bsr_per_pa_weight'],
        'bref_bsr_runs_per_pa_weight':request.session['bref_bsr_runs_per_pa_weight'],
        'home_to_first_weight':request.session['home_to_first_weight'],
        # 'sprint_speed_weight':request.session['sprint_speed_weight'],
        'outs_above_avg_weight':request.session['outs_above_avg_weight'],     
        'fielding_runs_prevented_weight':request.session['fielding_runs_prevented_weight'],
        # 'ffld_per_pa_weight':request.session['ffld_per_pa_weight'],
        'fdef_per_pa_weight':request.session['fdef_per_pa_weight'],
        'bref_war_def_per_pa_weight':request.session['bref_war_def_per_pa_weight'],
        })
    else:
      battingform = BattingWeightsForm()

    if 'winningpercent_weight' in request.session:
      pitchingform = PitchingWeightsForm(initial={
        'winningpercent_weight':request.session['winningpercent_weight'],
        # 'shutouts_weight':request.session['shutouts_weight'],
        'hitpernine_weight':request.session['hitpernine_weight'],
        # 'bbpernine_weight':request.session['bbpernine_weight'],
        # 'kpernine_weight':request.session['kpernine_weight'],
        'hrpernine_weight':request.session['hrpernine_weight'],
        'kperbb_weight':request.session['kperbb_weight'],
        'avg_weight':request.session['avg_weight'],
        'whip_weight':request.session['whip_weight'],
        'lobpercent_weight':request.session['lobpercent_weight'],
        # 'thrownforkpercent_weight':request.session['thrownforkpercent_weight'],
        'cswpercent_weight':request.session['cswpercent_weight'],
        'outsidezoneswingpercent_weight':request.session['outsidezoneswingpercent_weight'],
        'firstpitchstrikepercent_weight':request.session['firstpitchstrikepercent_weight'],
        'swingingstrikespercent_weight':request.session['swingingstrikespercent_weight'],
        'bbpercent_weight':request.session['bbpercent_weight'],
        'kpercent_weight':request.session['kpercent_weight'],
        'slg_weight':request.session['slg_weight'],
        'babip_weight':request.session['babip_weight'],
        # 'gbperfb_weight':request.session['gbperfb_weight'],
        'hrperfb_weight':request.session['hrperfb_weight'],
        'gbpercent_weight':request.session['gbpercent_weight'],
        'iffbpercent_weight':request.session['iffbpercent_weight'],
        'ldpercent_weight':request.session['ldpercent_weight'],
        'fbpercent_weight':request.session['fbpercent_weight'],
        'softpercent_weight':request.session['softpercent_weight'],
        'softplusmediumpercent_weight':request.session['softplusmediumpercent_weight'],
        # 'weakpercent_weight':request.session['weakpercent_weight'],
        'barrel_percent_weight':request.session['barrel_percent_weight'],
        'hardhitpercent_weight':request.session['hardhitpercent_weight'],
        'averageev_weight':request.session['averageev_weight'],
        # 'averagela_weight':request.session['averagela_weight'],
        'anglesweetspotpercent_weight':request.session['anglesweetspotpercent_weight'],
        'avgdistance_weight':request.session['avgdistance_weight'],
        'ev95pluspercent_weight':request.session['ev95pluspercent_weight'],
        # 'brlperpa_weight':request.session['brlperpa_weight'],
        'era_weight':request.session['era_weight'],
        'xera_weight':request.session['xera_weight'],
        'runsaverage_weight':request.session['runsaverage_weight'],
        'war_weight':request.session['war_weight'],
        'fip_weight':request.session['fip_weight'],
        'xfip_weight':request.session['xfip_weight'],
        'siera_weight':request.session['siera_weight'],
        'rar_weight':request.session['rar_weight'],
        'tera_weight':request.session['tera_weight'],
        'wpa_weight':request.session['wpa_weight'],
        'retwentyfour_weight':request.session['retwentyfour_weight'],
        'clutch_weight':request.session['clutch_weight'],
        'kwera_weight':request.session['kwera_weight'],
        'woba_weight':request.session['woba_weight'],
        'xavg_weight':request.session['xavg_weight'],
        'xslg_weight':request.session['xslg_weight'],
        'xwoba_weight':request.session['xwoba_weight'],
        })
    else:
      pitchingform = PitchingWeightsForm()

    if 'errors_weight' in request.session:
     teamform = TeamWeightsForm(initial={
       'errors_weight':request.session['errors_weight'],
       'doubleplays_weight':request.session['doubleplays_weight'],
       'fieldingpercentage_weight':request.session['fieldingpercentage_weight'],
       'xsbsavedagainst_weight':request.session['xsbsavedagainst_weight'],
       'wildpitchespluspassedballs_weight':request.session['wildpitchespluspassedballs_weight'],
       'defensiverunssaved_weight':request.session['defensiverunssaved_weight'],
       'ultimatezonerating_weight':request.session['ultimatezonerating_weight'],
       'defense_weight':request.session['defense_weight']
      })
    else:
     teamform = TeamWeightsForm()

  context = {'generalform': generalform, 'battingform' : battingform, 'pitchingform' : pitchingform, 'teamform' : teamform}
  return render(request, 'workshop.html', context)

# def loading_view(request):
#   render (request, 'home.html')
#   return HttpResponseRedirect('/results/')

def results_view(request):
  #I think the only choice is get
  if request.method == "GET":
    #access the results using request.session
    try:
      gameresults = request.session["gameresults"]
      # print(gameresults)

      return render(request, 'results.html', {'gameresults' : gameresults})
    except:
      return HttpResponseRedirect('/workshop/')
  else:
    return HttpResponseRedirect('/results/')

def input_valid(data):
  sum = 0
  for x in data:
    if data[x] is not None:
      sum = sum + data[x]
  return sum

def zmatchup(currentmatchup, wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict):
  #collect teams
  currentawayteam = currentmatchup.awayteam
  currenthometeam = currentmatchup.hometeam

  #collect starting pitchers
  currentawaypitcher = currentmatchup.awaypitcher
  currenthomepitcher = currentmatchup.homepitcher

  #collect lineups
  currentawaylineup = [currentmatchup.awaybatterone, currentmatchup.awaybattertwo, currentmatchup.awaybatterthree, currentmatchup.awaybatterfour, currentmatchup.awaybatterfive, currentmatchup.awaybattersix, currentmatchup.awaybatterseven, currentmatchup.awaybattereight, currentmatchup.awaybatternine]
  currenthomelineup = [currentmatchup.homebatterone, currentmatchup.homebattertwo, currentmatchup.homebatterthree, currentmatchup.homebatterfour, currentmatchup.homebatterfive, currentmatchup.homebattersix, currentmatchup.homebatterseven, currentmatchup.homebattereight, currentmatchup.homebatternine]

  #collect positions for dh purposes
  currentawaypositions = currentmatchup.awaypositions
  currenthomepositions = currentmatchup.homepositions

  plus_park_adjusted = wgeneraldict['plus_park_adjusted']

  awaybattingzsum = findbattingzsum(plus_park_adjusted, wbatterdict, currentawaylineup)
  homebattingzsum = findbattingzsum(plus_park_adjusted, wbatterdict, currenthomelineup)
  awayindivfieldingzsum = findindivfieldingzsum(wfieldingdict, currentawaylineup, currentawaypositions)
  homeindivfieldingzsum = findindivfieldingzsum(wfieldingdict, currenthomelineup, currenthomepositions)
  awaybaserunningzsum = findbaserunningzsum(wbaserunningdict, currentawaylineup)
  homebaserunningzsum = findbaserunningzsum(wbaserunningdict, currenthomelineup)
  awaypitchingzsum = findpitchingzsum(currentawayteam, currentawaypitcher, wpitcherdict, plus_park_adjusted)
  homepitchingzsum = findpitchingzsum(currenthometeam, currenthomepitcher, wpitcherdict, plus_park_adjusted)
  awayteamfieldingzsum = findteamfieldingzsum(currentawayteam, wteamdict)
  hometeamfieldingzsum = findteamfieldingzsum(currenthometeam, wteamdict)
  awayzsum = totalzsum(awaybattingzsum, awayindivfieldingzsum, awaybaserunningzsum, awaypitchingzsum, awayteamfieldingzsum, wgeneraldict)
  homezsum = totalzsum(homebattingzsum, homeindivfieldingzsum, homebaserunningzsum, homepitchingzsum, hometeamfieldingzsum, wgeneraldict)

  return {'away' : awayzsum, 'home' : homezsum}

def homefield(hometeamwinpercent, homefieldboost):
  #HOME-FIELD
  hometeamwinpercent = round(hometeamwinpercent + homefieldboost, 2)
  if hometeamwinpercent > 100:
    hometeamwinpercent = 100
  if hometeamwinpercent < 0:
    hometeamwinpercent = 0
  return hometeamwinpercent

def gameodds(hometeamwinpercent, awayteamwinpercent):
  if hometeamwinpercent >= 50 and awayteamwinpercent != 0 and hometeamwinpercent != 0:
    homeamericanodds = str(round((100 * hometeamwinpercent) / (100 - hometeamwinpercent)))
    homeamericanodds = '-' + homeamericanodds
    awayamericanodds = str(round((10000/awayteamwinpercent) - 100))
    awayamericanodds = '+' + awayamericanodds
  elif awayteamwinpercent != 0 and hometeamwinpercent != 0:
    awayamericanodds = str(round((100 * awayteamwinpercent) / (100 - awayteamwinpercent)))
    awayamericanodds = '-' + awayamericanodds
    homeamericanodds = str(round((10000/hometeamwinpercent) - 100))
    homeamericanodds = '+' + homeamericanodds
  else:
    awayamericanodds = 'ERR'
    homeamericanodds = 'ERR'
  return {'home' : homeamericanodds, 'away' : awayamericanodds}

def teamfieldingweighttotal(wteamdict):
  #does not matter what team is used
  # team = team.objects.all().get(name = 'nyy')
  # teamdict = team.accesszfielding2022dict()
  totalfieldingweights = 0
  #loop through the team fielding keys of the zdict/wdict
  for teamfieldingkey in wteamdict.keys():
    if wteamdict[teamfieldingkey] is not None:
      totalfieldingweights += wteamdict[teamfieldingkey] / 100


def singlesimulation(awayteam, hometeam, awaylineup, homelineup, awaypitchers, homepitchers, awayinnings, homeinnings, awaypositions, homepositions, wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict):
  plus_park_adjusted = wgeneraldict['plus_park_adjusted']
  awaybattingzsum = findbattingzsum(plus_park_adjusted, wbatterdict, awaylineup)
  homebattingzsum = findbattingzsum(plus_park_adjusted, wbatterdict, homelineup)

  awayindivfieldingzsum = findindivfieldingzsum(wfieldingdict, awaylineup, awaypositions)
  print(awayindivfieldingzsum)
  homeindivfieldingzsum = findindivfieldingzsum(wfieldingdict, homelineup, homepositions)
  print(homeindivfieldingzsum)
  #this stat needs to be scaled to 100 because there is no team, so however much weight the user cumulatively dedicated to team-fielding stats needs to go to individual
  teamfieldingweights = teamfieldingweighttotal(wteamdict)
  if teamfieldingweights is not None and teamfieldingweights != 1:
    awayindivfieldingzsum *= (1 / (1 - teamfieldingweights))
    homeindivfieldingzsum *= (1 / (1 - teamfieldingweights))
  #check that the above, along with the function it calls, works

  awaybaserunningzsum = findbaserunningzsum(wbaserunningdict, awaylineup)
  homebaserunningzsum = findbaserunningzsum(wbaserunningdict, homelineup)

  #new pitching simulations are needed
  awaypitchingzsum = findsinglegamepitchingzsum(awaypitchers, awayinnings, wpitcherdict, plus_park_adjusted)
  homepitchingzsum = findsinglegamepitchingzsum(homepitchers, homeinnings, wpitcherdict, plus_park_adjusted)
  print("pitching")
  print(awaypitchingzsum)
  print(homepitchingzsum)

  # a new total zsum is needed
  awayzsum = singletotalzsum(awaybattingzsum, awayindivfieldingzsum, awaybaserunningzsum, awaypitchingzsum, wgeneraldict)
  homezsum = singletotalzsum(homebattingzsum, homeindivfieldingzsum, homebaserunningzsum, homepitchingzsum, wgeneraldict)
  
  #POWER SCORE: independent of opponent and home-field, where 100 is league-average
  homepowerscore = round(homezsum['zsum'] * 40 + 100, 2)
  awaypowerscore = round(awayzsum['zsum'] * 40 + 100, 2)

  #POWER SCORE for individual categories
  homebattingpowerscore = round(homezsum['battingzsum'] * 40 + 100, 2)
  awaybattingpowerscore = round(awayzsum['battingzsum'] * 40 + 100, 2)
  homefieldingpowerscore = round(homezsum['fieldingzsum'] * 40 + 100, 2)
  awayfieldingpowerscore = round(awayzsum['fieldingzsum'] * 40 + 100, 2)
  print(round(homezsum['baserunningzsum'] * 40 + 100, 2))
  homebaserunningpowerscore = float(round(homezsum['baserunningzsum'] * 40 + 100, 2))
  awaybaserunningpowerscore = float(round(awayzsum['baserunningzsum'] * 40 + 100, 2))
  homepitchingpowerscore = round(homezsum['pitchingzsum'] * 40 + 100, 2)
  awaypitchingpowerscore = round(awayzsum['pitchingzsum'] * 40 + 100, 2)

  variance = wgeneraldict['variance']

  #perform the math function, which should return home team and away team chances of winning
  hometeamwinpercent = mathsimulation(homezsum['zsum'], awayzsum['zsum'], variance)
  homefieldboost = wgeneraldict['homefield_weight']

  #apply homefield advantage
  hometeamwinpercent = round(homefield(hometeamwinpercent, homefieldboost), 2)
  awayteamwinpercent = round(100 - hometeamwinpercent, 2)


  #run function to calculate american odds
  teamodds = gameodds(hometeamwinpercent, awayteamwinpercent)
  homeamericanodds = teamodds['home']
  awayamericanodds = teamodds['away']
  #the big question is what to return here. if you want to build a powerful page that shows every player's contribution, you are gonna need to build something powerful here, and possibly even adjust the functions and what they return to be more detailed
  #what if I start with the basics of returning batting/pitching/baserunning/fielding, plus win percent and odds and power score
  return {'hometeam' : hometeam.upper(), 'homewinpercent' : hometeamwinpercent, 'homeamericanodds' : homeamericanodds, 'homepowerscore' : homepowerscore, 'homebattingpowerscore': homebattingpowerscore, 'homefieldingpowerscore': homefieldingpowerscore, 'homepitchingpowerscore': homepitchingpowerscore, 'homebaserunningpowerscore': homebaserunningpowerscore, 'awayteam': awayteam.upper(), 'awaywinpercent' : awayteamwinpercent, 'awayamericanodds': awayamericanodds, 'awaypowerscore' : awaypowerscore, 'awaybattingpowerscore': awaybattingpowerscore, 'awayfieldingpowerscore': awayfieldingpowerscore, 'awaypitchingpowerscore': awaypitchingpowerscore, 'awaybaserunningpowerscore': awaybaserunningpowerscore}

def findsinglegamepitchingzsum(pitchers, innings, wpitcherdict, plus_park_adjusted):
  #generate plus dictionaries which will be used if user has selected plus stats
  pitchingplusdict = {'zkpernine':'zplus_k_per_nine', 'zbbpernine':'zplus_bb_per_nine', 'zkperbb':'zplus_k_per_bb', 'zhitpernine':'zplus_h_per_nine', 'zhrpernine':'zplus_hr_per_nine', 'zavg':'zplus_avg', 'zwhip':'zplus_whip', 'zbabip':'zplus_babip', 'zlobpercent':'zplus_lobpercent', 'zkpercent':'zplus_kpercent', 'zbbpercent':'zplus_bbpercent', 'zldpercent':'zplus_ldpercent', 'zgbpercent':'zplus_gbpercent', 'zhrperfb':'zplus_hrperfb', 'zsoftpercent':'zplus_softpercent', 'zmediumpercent':'zplus_mediumpercent'}
  #starting pitching
  pitching2022zsum = 0
  pitching2021zsum = 0
  pitching2020zsum = 0
  for x in range(len(pitchers)):
    indivpitching2022zsum = 0
    indivpitching2021zsum = 0
    indivpitching2020zsum = 0
    pitcher2022dict = pitchers[x].accesszpitcher2022dict()
    pitcher2021dict = pitchers[x].accesszpitcher2021dict()
    pitcher2020dict = pitchers[x].accesszpitcher2020dict()
    #loop through the keys of the zdict/wdict
    for pitchingkey in wpitcherdict.keys():
      if wpitcherdict[pitchingkey] is not None:
        #check if plus stats being used and this qualifies as a stat for which plus data is available
        if plus_park_adjusted:
          if pitchingkey in pitchingplusdict:
            pluspitchingkey = pitchingplusdict[pitchingkey]
          else:
            pluspitchingkey = pitchingkey
        else:
          pluspitchingkey = pitchingkey

        #starting pitcher value
        # 2022
        indivpitching2022zsum += (wpitcherdict[pitchingkey] * pitcher2022dict[pluspitchingkey]) / 100
        indivpitching2021zsum += (wpitcherdict[pitchingkey] * pitcher2021dict[pluspitchingkey]) / 100
        indivpitching2020zsum += (wpitcherdict[pitchingkey] * pitcher2020dict[pluspitchingkey]) / 100
    indivinnings = findindivinnings(float(innings[x]))
    pitching2022zsum += float(indivpitching2022zsum) * indivinnings
    pitching2021zsum += float(indivpitching2021zsum) * indivinnings
    pitching2020zsum += float(indivpitching2020zsum) * indivinnings
  pitching2022zsum /= 9
  pitching2021zsum /= 9
  pitching2020zsum /= 9
  return {'2022': pitching2022zsum, '2021': pitching2021zsum, '2020': pitching2020zsum}
  



def simulation(currentmatchup, wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict):
  teamzsum = zmatchup(currentmatchup, wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict)
  awayzsum = teamzsum['away']
  homezsum = teamzsum['home']
  #POWER SCORE: independent of opponent and home-field, where 100 is league-average
  homepowerscore = round(homezsum * 40 + 100, 2)
  awaypowerscore = round(awayzsum * 40 + 100, 2)

  variance = wgeneraldict['variance']

  #perform the math function, which should return home team and away team chances of winning
  hometeamwinpercent = mathsimulation(homezsum, awayzsum, variance)
  homefieldboost = wgeneraldict['homefield_weight']

  #apply homefield advantage
  hometeamwinpercent = round(homefield(hometeamwinpercent, homefieldboost), 2)
  awayteamwinpercent = round(100 - hometeamwinpercent, 2)


  #run function to calculate american odds
  teamodds = gameodds(hometeamwinpercent, awayteamwinpercent)
  homeamericanodds = teamodds['home']
  awayamericanodds = teamodds['away']

  #store each matchup as a list item in a larger list (list of lists)
  #note: team being passed by name object could easily be accessed by unique name, pitcher fangraphs_id to access info
  #formulate pitcher to be passed, adjust if pitcher is dummy dummy because he did not qualify
  homepitcher = currentmatchup.homepitcher.firstname + ' ' + currentmatchup.homepitcher.lastname
  awaypitcher = currentmatchup.awaypitcher.firstname + ' ' + currentmatchup.awaypitcher.lastname
  if currentmatchup.homepitcher.firstname == 'dummy':
    homepitcher = 'DNQ (not enough IP) - replacement level stats used instead'
  if currentmatchup.awaypitcher.firstname == 'dummy':
    awaypitcher = 'DNQ (not enough IP) - replacement level stats used instead'

  #if game is doubleheader, make note
  if currentmatchup.doubleheadergameone:
    gamedate = currentmatchup.gamedate + ' G1'
  elif currentmatchup.doubleheadergametwo:
    gamedate = currentmatchup.gamedate + ' G2'
  else:
    gamedate = currentmatchup.gamedate
  return {'gametime' : currentmatchup.gametime, 'gamedate' : gamedate, 'homelogopath' : currentmatchup.hometeam.logopath, 'homecity': currentmatchup.hometeam.city, 'hometeam' : currentmatchup.hometeam.name.upper(), 'homepitcher' : homepitcher, 'homepitcherid' : currentmatchup.homepitcher.fangraphs_id, 'homewinpercent' : hometeamwinpercent, 'homeamericanodds' : homeamericanodds, 'homepowerscore' : homepowerscore, 'awaylogopath' : currentmatchup.awayteam.logopath, 'awaycity': currentmatchup.awayteam.city, 'awayteam' : currentmatchup.awayteam.name.upper(), 'awaypitcher' : awaypitcher, 'awaypitcherid' : currentmatchup.awaypitcher.fangraphs_id, 'awaywinpercent' : awayteamwinpercent, 'awayamericanodds': awayamericanodds, 'awaypowerscore' : awaypowerscore}

def todaysimulation(wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict):
  gameresults = []

  # first, iterate through each matchup where both lineups are loaded using a big for loop
  # order_by should ensure games are always posted in chronological order, except that it has 12 lose to 1
  # for currentmatchup in matchup.objects.filter(awaylineupposted = True, homelineupposted = True).order_by('gametime'):
  qmatchup = []
  # first check for 12, then just check 1 through 11 by incrementing
  for currentmatchup in matchup.objects.filter(awaylineupposted = True, homelineupposted = True).order_by('gametime'):
    if (currentmatchup.gametime.startswith('12')):
      qmatchup.append(currentmatchup)
  for x in range(11):
    for currentmatchup in matchup.objects.filter(awaylineupposted = True, homelineupposted = True).order_by('gametime'):
      if (currentmatchup.gametime.startswith(str(x))):
        if (x == 1 and (currentmatchup.gametime.startswith('12') or currentmatchup.gametime.startswith('11') or currentmatchup.gametime.startswith('10'))):
          pass
        else:
          qmatchup.append(currentmatchup)
      #for speed purposes
      elif (currentmatchup.gametime.startswith(str(x + 1)) and x != 9):
        break
  qmatchup.reverse()
  while(len(qmatchup) > 0):
    currentmatchup = qmatchup.pop()
    gameresult = simulation(currentmatchup, wbatterdict, wbaserunningdict, wfieldingdict, wpitcherdict, wteamdict, wgeneraldict)    
    gameresults.append(gameresult)
  # print(gameresults)


  #load games without lineups currently posted
  fmatchup = []
  # first check for 12, then just check 1 through 11 by incrementing
  for currentmatchup in matchup.objects.filter(awaylineupposted = False) | matchup.objects.filter(homelineupposted = False).order_by('gametime'):
    if (currentmatchup.gametime.startswith('12')):
      fmatchup.append(currentmatchup)
  for x in range(11):
    for currentmatchup in matchup.objects.filter(awaylineupposted = False) | matchup.objects.filter(homelineupposted = False).order_by('gametime'):
      if (currentmatchup.gametime.startswith(str(x))):
        if (x == 1 and (currentmatchup.gametime.startswith('12') or currentmatchup.gametime.startswith('11') or currentmatchup.gametime.startswith('10'))):
          pass
        else:
          fmatchup.append(currentmatchup)
      #for speed purposes
      elif (currentmatchup.gametime.startswith(str(x + 1)) and x != 9):
        break
  fmatchup.reverse()
  while(len(fmatchup) > 0):
    freshmatchup = fmatchup.pop()
  # for freshmatchup in matchup.objects.filter(awaylineupposted = False) | matchup.objects.filter(homelineupposted = False):
    #collect teams
    freshawayteam = freshmatchup.awayteam
    freshhometeam = freshmatchup.hometeam
    #if game is doubleheader, make note
    if freshmatchup.doubleheadergameone:
      gamedate = freshmatchup.gamedate + ' G1'
    elif freshmatchup.doubleheadergametwo:
      gamedate = freshmatchup.gamedate + ' G2'
    else:
      gamedate = freshmatchup.gamedate
    gameresults.append({'gametime' : freshmatchup.gametime, 'gamedate' : gamedate, 'homelogopath' : freshhometeam.logopath, 'hometeam' : freshhometeam.name.upper(), 'homecity' : freshhometeam.city, 'homepitcher' : 'CHECK BACK SOON', 'homepitcherid' : '', 'homewinpercent' : 'NA', 'homeamericanodds' : 'NA', 'homepowerscore' : 'NA', 'awaylogopath' : freshawayteam.logopath, 'awayteam' : freshawayteam.name.upper(), 'awaycity' : freshawayteam.city, 'awaypitcher' : 'LINEUPS NOT POSTED', 'awaypitcherid' : '', 'awaywinpercent' : 'NA', 'awayamericanodds': 'NA', 'awaypowerscore' : 'NA'})
  return gameresults


def mathsimulation(netzteamone, netzteamtwo, standarddev):
  teamonewins = 0
  teamtwowins = 0
  for x in range(100000):
    teamonezrand = random.gauss(netzteamone, standarddev)
    teamtwozrand = random.gauss(netzteamtwo, standarddev)
    if (teamonezrand > teamtwozrand):
      teamonewins += 1
    else:
      teamtwowins += 1
  teamonewinpercent = float(teamonewins) * 100 / float(teamonewins + teamtwowins)
  teamtwowinpercent = float(teamtwowins) * 100 / float(teamtwowins + teamonewins)
  # print(teamonewinpercent)
  # print(teamtwowinpercent)
  #only need to return one of the values, the other can be derived
  return teamonewinpercent

def findbattingzsum(plus_park_adjusted, wbatterdict, lineup):
  #generate plus dictionaries which will be used if user has selected plus stats
  battingplusdict = {'zavg':'zplus_avg', 'zobp':'zplus_obp', 'zslg':'zplus_slg', 'zbb_per_pa':'zplus_bb_per_pa', 'zk_per_pa':'zplus_k_per_pa', 'zwRC':'zplus_wRC', 'ziso':'zplus_iso', 'zbabip':'zplus_babip', 'zld_per_bip':'zplus_ld_per_bip', 'zgb_per_bip':'zplus_gb_per_bip', 'zfb_per_bip':'zplus_fb_per_bip', 'zhr_per_fb':'zplus_hr_per_fb', 'zhardpercent':'zplus_hardpercent', 'zops': 'zplus_ops'}
  batting2022zsum = 0
  batting2021zsum = 0
  batting2020zsum = 0
  for currentbatter in lineup:
    #NOTE: change to exclusively batting dictionary
    currentbatter2022dict = currentbatter.accesszbatter2022dict()
    currentbatter2021dict = currentbatter.accesszbatter2021dict()
    currentbatter2020dict = currentbatter.accesszbatter2020dict()
    #loop through the keys of the zdict/wdict. use the wdict keys to loop because it has batting separate from baserunning/fielding
    #batting
    for battingkey in wbatterdict.keys():
      if wbatterdict[battingkey] is not None:
        #check if plus stats being used and this qualifies as a stat for which plus data is available
        if plus_park_adjusted:
          if battingkey in battingplusdict:
            plusbattingkey = battingplusdict[battingkey]
          else:
            plusbattingkey = battingkey
        else:
          plusbattingkey = battingkey
          
        # 2022
        #divide by 100 because the weight still hasn't been divided by 100 to keep the page rendering properly back to the user
        batting2022zsum += (wbatterdict[battingkey] * currentbatter2022dict[plusbattingkey]) / 100
        # 2021
        batting2021zsum += (wbatterdict[battingkey] * currentbatter2021dict[plusbattingkey]) / 100
        # 2020
        batting2020zsum += (wbatterdict[battingkey] * currentbatter2020dict[plusbattingkey]) / 100
  return {'2022': batting2022zsum, '2021': batting2021zsum, '2020': batting2020zsum}

def findindivfieldingzsum(wfieldingdict, lineup, positions):
  #This should not include any dh and will need to be used again later when the teams are iterated through, only individual fielding is being collected now
  indivfielding2022zsum = 0 
  indivfielding2021zsum = 0
  indivfielding2020zsum = 0
  for currentfielder in lineup:
    currentfielder2022dict = currentfielder.accesszfielder2022dict()
    currentfielder2021dict = currentfielder.accesszfielder2021dict()
    currentfielder2020dict = currentfielder.accesszfielder2020dict()
    #get position of current batter to avoid using the dh for fielding stats
    currentfielderposition = positions[:2]
    #adjust the positions to pop off the current value
    positions = positions[2:]
    #fielding
    if currentfielderposition.lower() != 'dh':
      for fieldingkey in wfieldingdict.keys():
        if wfieldingdict[fieldingkey] is not None:
          #divide by 100 because the weight still hasn't been divided by 100 to keep the page rendering properly back to the user
          indivfielding2022zsum += (wfieldingdict[fieldingkey] * currentfielder2022dict[fieldingkey]) / 100
          indivfielding2021zsum += (wfieldingdict[fieldingkey] * currentfielder2021dict[fieldingkey]) / 100
          indivfielding2020zsum += (wfieldingdict[fieldingkey] * currentfielder2020dict[fieldingkey]) / 100
  return {'2022': indivfielding2022zsum, '2021': indivfielding2021zsum, '2020': indivfielding2020zsum}

def findbaserunningzsum(wbaserunningdict, lineup):
  baserunning2022zsum = 0
  # baserunning2021zsum = 0
  # baserunning2020zsum = 0
  #baserunning
  for currentbsr in lineup:
    # print(currentbsr)
    currentbsr2022dict = currentbsr.accesszbaserunner2022dict()
    # currentbatter2021dict = currentbatter.accesszbatter2021dict()
    # currentbatter2020dict = currentbatter.accesszbatter2020dict()
    for baserunningkey in wbaserunningdict.keys():
      if wbaserunningdict[baserunningkey] is not None:
        #divide by 100 because the weight still hasn't been divided by 100 to keep the page rendering properly back to the user
        baserunning2022zsum += (wbaserunningdict[baserunningkey] * currentbsr2022dict[baserunningkey]) / 100
        # baserunning2021zsum += (wbaserunningdict[baserunningkey] * currentbatter2021dict[baserunningkey]) / 100
        # baserunning2020zsum += (wbaserunningdict[baserunningkey] * currentbatter2020dict[baserunningkey]) / 100
    # print(baserunning2022zsum)
  return {'2022': baserunning2022zsum}
  # return {'2022': baserunning2022zsum, '2021': baserunning2021zsum, '2020': baserunning2020zsum}

def findpitchingzsum(team, pitcher, wpitcherdict, plus_park_adjusted):
  #NOTE: this should change to just a function which returns the pitching / bullpen stuff
  #load the team dict
  teamdict = team.accesszbullpen2022dict()

  #generate plus dictionaries which will be used if user has selected plus stats
  pitchingplusdict = {'zkpernine':'zplus_k_per_nine', 'zbbpernine':'zplus_bb_per_nine', 'zkperbb':'zplus_k_per_bb', 'zhitpernine':'zplus_h_per_nine', 'zhrpernine':'zplus_hr_per_nine', 'zavg':'zplus_avg', 'zwhip':'zplus_whip', 'zbabip':'zplus_babip', 'zlobpercent':'zplus_lobpercent', 'zkpercent':'zplus_kpercent', 'zbbpercent':'zplus_bbpercent', 'zldpercent':'zplus_ldpercent', 'zgbpercent':'zplus_gbpercent', 'zhrperfb':'zplus_hrperfb', 'zsoftpercent':'zplus_softpercent', 'zmediumpercent':'zplus_mediumpercent'}
  #starting pitching
  pitching2022zsum = 0
  pitching2021zsum = 0
  pitching2020zsum = 0
  #bullpen pitching
  bullpenpitchingzsum = 0
  #for categories that are missing, subtract from this total
  bullpenmultiplyfactor = 100

  pitcher2022dict = pitcher.accesszpitcher2022dict()
  pitcher2021dict = pitcher.accesszpitcher2021dict()
  pitcher2020dict = pitcher.accesszpitcher2020dict()
  #loop through the keys of the zdict/wdict
  for pitchingkey in wpitcherdict.keys():
    if wpitcherdict[pitchingkey] is not None:
      #check if plus stats being used and this qualifies as a stat for which plus data is available
      if plus_park_adjusted:
        if pitchingkey in pitchingplusdict:
          pluspitchingkey = pitchingplusdict[pitchingkey]
        else:
          pluspitchingkey = pitchingkey
      else:
        pluspitchingkey = pitchingkey

      #starting pitcher value
      # 2022
      pitching2022zsum += (wpitcherdict[pitchingkey] * pitcher2022dict[pluspitchingkey]) / 100
      pitching2021zsum += (wpitcherdict[pitchingkey] * pitcher2021dict[pluspitchingkey]) / 100
      pitching2020zsum += (wpitcherdict[pitchingkey] * pitcher2020dict[pluspitchingkey]) / 100
      #bullpen pitching, many of the keys will not work because bullpen data is more limited, so use try/except
      try:
        bullpentemp = (wpitcherdict[pitchingkey] * teamdict[pluspitchingkey]) / 100
        bullpenpitchingzsum += bullpentemp
      except:
        #it still might exist, just not as a plus stat
        try:
          bullpentemp = (wpitcherdict[pitchingkey] * teamdict[pitchingkey]) / 100
          bullpenpitchingzsum += bullpentemp
        except: 
          #if it does not work at all, we should keep track of the fact that we are at less than 100% sum for bullpen and overcompensate with a multiplicative factor for all other bullpen categories
          bullpenmultiplyfactor = bullpenmultiplyfactor - wpitcherdict[pitchingkey]
        #if the key is not found because the stat is not available for bullpens, but let's double check (shutouts, slugging, anglesweetspot, avgdistance, ev95pluspercent, barrel per pa, xera, tera, kwera, woba, xavg, xwoba, xslg)
        #print (pitchingkey)
        pass

  #print(pitchingzsum)
  #adjust bullpenzsum by multiply factor
  if (bullpenmultiplyfactor != 0):
    bullpenpitchingzsum = float(bullpenpitchingzsum) * float(100/bullpenmultiplyfactor)
  return {'bullpen': bullpenpitchingzsum, '2022': pitching2022zsum, '2021': pitching2021zsum, '2020': pitching2020zsum}

def findteamfieldingzsum(team, wteamdict):
  #NOTE: switch to just team fielding stats
  teamdict = team.accesszfielding2022dict()
  teamfieldingzsum = 0
  #loop through the team fielding keys of the zdict/wdict
  for teamfieldingkey in wteamdict.keys():
    if wteamdict[teamfieldingkey] is not None:
      teamfieldingzsum += (wteamdict[teamfieldingkey] * teamdict[teamfieldingkey]) / 100
  return teamfieldingzsum

def singletotalzsum(batting, fielding, baserunning, pitching, wgeneraldict):
  #multiply the final zsums by the season weights
  #divide by 100 because weights are out of 100
  battingzsum = (float(batting['2022']) * float(wgeneraldict['s2022_weight']) + float(batting['2021']) * float(wgeneraldict['s2021_weight']) + float(batting['2020']) * float(wgeneraldict['s2020_weight'])) / 900
  fieldingzsum = (float(fielding['2022']) * float(wgeneraldict['s2022_weight']) + float(fielding['2021']) * float(wgeneraldict['s2021_weight']) + float(fielding['2020']) * float(wgeneraldict['s2020_weight'])) / 800
  # divide by 9 rather than 900 because only looking at one season
  baserunningzsum = (baserunning['2022']) / 9
  pitchingzsum = (float(pitching['2022']) * float(wgeneraldict['s2022_weight']) + float(pitching['2021']) * float(wgeneraldict['s2021_weight']) + float(pitching['2020']) * float(wgeneraldict['s2020_weight'])) / 100
  #multiply the categories by the category weights
  zsum = (float(battingzsum) * float(wgeneraldict['batting_weight']) + float(fieldingzsum) * float(wgeneraldict['fielding_weight']) + float(baserunningzsum) * float(wgeneraldict['baserunning_weight']) + float(pitchingzsum) * float(wgeneraldict['pitching_weight'])) / 100
  return {'zsum': zsum, 'battingzsum': battingzsum, 'fieldingzsum': fieldingzsum, 'baserunningzsum': baserunningzsum, 'pitchingzsum': pitchingzsum}

def totalzsum(batting, indivfielding, baserunning, pitching, teamfielding, wgeneraldict):
  rawinnings = wgeneraldict['starterinnings']
  starterinnings = findindivinnings(rawinnings)
  starterpercent = starterinnings / 9
  bullpenpercent = 1 - starterpercent
  #multiply the final zsums for batting and starting pitching (ONLY, not bullpen) by the season weights
  #divide by 100 because weights are out of 100
  battingzsum = (float(batting['2022']) * float(wgeneraldict['s2022_weight']) + float(batting['2021']) * float(wgeneraldict['s2021_weight']) + float(batting['2020']) * float(wgeneraldict['s2020_weight'])) / 900
  indivfieldingzsum = (float(indivfielding['2022']) * float(wgeneraldict['s2022_weight']) + float(indivfielding['2021']) * float(wgeneraldict['s2021_weight']) + float(indivfielding['2020']) * float(wgeneraldict['s2020_weight'])) / 800
  fieldingzsum = float(indivfieldingzsum) + float(teamfielding)
  # divide by 9 rather than 900 because only looking at one season
  baserunningzsum = (baserunning['2022']) / 9
  indivpitchingzsum = (float(pitching['2022']) * float(wgeneraldict['s2022_weight']) + float(pitching['2021']) * float(wgeneraldict['s2021_weight']) + float(pitching['2020']) * float(wgeneraldict['s2020_weight'])) / 100
  pitchingzsum = float(indivpitchingzsum) * float(starterpercent) + float(pitching['bullpen']) * float(bullpenpercent)
  #multiply the pitchingzsums and bullpenzsums by the percent
  #multiply the categories by the category weights
  zsum = (float(battingzsum) * float(wgeneraldict['batting_weight']) + float(fieldingzsum) * float(wgeneraldict['fielding_weight']) + float(baserunningzsum) * float(wgeneraldict['baserunning_weight']) + float(pitchingzsum) * float(wgeneraldict['pitching_weight'])) / 100
  return zsum

# def findstarterinnings(wgeneraldict):
#   if (wgeneraldict['starterinnings'] % 1 > 0.09 and wgeneraldict['starterinnings'] % 1 < 0.11):
#     starterinnings = wgeneraldict['starterinnings'] - wgeneraldict['starterinnings'] % 1 + 0.33
#   elif (wgeneraldict['starterinnings'] % 1 > 0.19 and wgeneraldict['starterinnings'] % 1 < 0.21):
#     starterinnings = wgeneraldict['starterinnings'] - wgeneraldict['starterinnings'] % 1 + 0.67
#   else:
#     #round to whole number
#     starterinnings = float(round(wgeneraldict['starterinnings']))
#   return starterinnings

def findindivinnings(innings):
  if (innings % 1 > 0.09 and innings % 1 < 0.11):
    starterinnings = innings - innings % 1 + 0.33
  elif (innings % 1 > 0.19 and innings % 1 < 0.21):
    starterinnings = innings - innings % 1 + 0.67
  else:
    #round to whole number
    starterinnings = float(round(innings))
  return starterinnings


    

      


#THE SIMULATION
#Plan: run this function and redirect to results when the function is done (maybe an in-between loading page)
# I have to decide how much fielding/baserunning should be weighed, I will do so by finding the fangraphs stddev for each of batting, baserunning, pitching, fielding and then assign % accordingly with pitching/batting being adjusted to an even split
# get the final team z-sums, send it to another function which takes the z-sums and variance, and gives back % to win
# once all of this works, you can move to rendering the matchup results page