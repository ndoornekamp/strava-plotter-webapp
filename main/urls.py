"""main URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from webapp.views import home, loading_activities, plotter_settings, making_plots, result

urlpatterns = [
    path('exchange_code', loading_activities),
    path('plotter_settings', plotter_settings, name='plotter_settings'),
    path('making_plots', making_plots, name='making_plots'),
    path('result', result, name='result'),
    path('', home),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
