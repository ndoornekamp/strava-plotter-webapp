import time
import sys
sys.path.append('strava-plotter')  # Can't import from from modules with a '-'.. https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it

from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from strava_plotter import strava_plotter


def home(request):
    return render(request, 'home.html')


def result(request):
    strava_plotter(authorisation_code=request.GET['code'])

    return FileResponse(open("media/output.png","rb"))