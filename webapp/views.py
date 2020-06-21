import time
import sys
sys.path.append('strava-plotter')  # Can't import from from modules with a '-'.. https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it

from collections import Counter

from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from strava_plotter import get_rides_from_strava, parse_rides, cluster_rides, plot_rides


def home(request):
    return render(request, 'home.html')


def loading_activities(request):
    request.session['auth_code'] = request.GET['code']
    return render(request, 'loading_activities.html')


def plotter_settings(request):
    request.session['rides'] = get_rides_from_strava(authorisation_code=request.session['auth_code'])

    types = Counter([ride['type'] for ride in request.session['rides']])
    context = {
        "types": dict(types)
    }

    return render(request, 'settings.html', context=context)


def making_plots(request):
    request.session['params_from_form'] = dict(request.GET)
    return render(request, 'making_plots.html')


def result(request):
    params = {}
    params_from_form = request.session['params_from_form']
    
    # Hardcoded settings
    params["first_cluster_only"] = False
    params["output_format"] = "bytes"
    params["subplots_in_separate_files"] = True

    # Settings from form
    params["clustered"] = params_from_form.pop("clustered", [""])[0] == "on"
    params["margin"] = float(params_from_form.pop("margin")[0])
    params["ids_to_skip"] = [id_to_skip.strip() for id_to_skip in params_from_form.pop("ids_to_skip")[0].split(";") if id_to_skip != '']
    params["alpha"] = float(params_from_form.pop("opacity")[0])/100
    params["activity_types"] = [activity_type for activity_type in params_from_form if params_from_form[activity_type] == ['on']]      

    print(f'Total number of acitivities: {len(request.session["rides"])}')
    print(f'Parameters used: {params}')

    rides = parse_rides(request.session['rides'], params)
    rides = cluster_rides(rides, params)
    images_base64 = plot_rides(rides, params)

    return render(request, 'result.html', {'images': images_base64})
