#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
#def my_Equiride(request):
#   return HttpResponse("Hello, Booking System!")

#def homepage(request):
#   return render(request, 'homepage.html')

class Index(TemplateView):
    template_name = "Equiride/index.html"