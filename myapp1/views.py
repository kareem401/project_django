from django.views.generic import ListView, TemplateView
from .models import post 

class HomePageView(ListView):
	model = post
	template_name = "home.html"

class AboutPageView(TemplateView):
	template_name = "about.html"