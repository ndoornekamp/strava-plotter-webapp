import time
import sys
sys.path.append('strava-plotter')  # Can't import from from modules with a '-'.. https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it

from collections import Counter
from PIL import Image

from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from strava_plotter import get_rides_from_strava, parse_rides, cluster_rides, plot_rides


def home(request):
    return render(request, 'home.html')


def plotter_settings(request):
    request.session['rides'] = get_rides_from_strava(authorisation_code=request.GET['code'])

    print(request.session['rides'])
    print(len(request.session['rides']))

    types = Counter([ride['type'] for ride in request.session['rides']])

    context = {
        "nof_activities": len(request.session['rides']),
        "types": dict(types)
    }

    return render(request, 'settings.html', context=context)


def result(request):
    return FileResponse(open('media/output.png', 'rb'))