from django.urls import path
from . import views
from .views import HomePageView, AboutPageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   	path('', HomePageView.as_view(), name="home"),
   	path('about/', AboutPageView.as_view(), name="about"),
   	
]

urlpatterns += staticfiles_urlpatterns()