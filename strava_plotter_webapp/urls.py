"""strava_plotter_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from webapp.views import home, loading_activities, plotter_settings, making_plots, result

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url('exchange_code', loading_activities),
    url('plotter_settings', plotter_settings, name='plotter_settings'),
    url('making_plots', making_plots, name='making_plots'),
    url('result', result, name='result'),
    url('', home),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
