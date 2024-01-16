from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip, Note
# Create your views here.
class HomeView(TemplateView):
    template_name = 'trips/index.html'
    
    
def trips_list(request):
    trips = Trip.objects.all()
    notes = Note.objects.all()
    context = {
        'trips': trips,
        'notes': notes
    }
    return render(request, 'trips/trip_list.html', context)