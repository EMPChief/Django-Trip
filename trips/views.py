from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Trip, Note
from django.contrib.auth.mixins import LoginRequiredMixin

# HomeView: Display the homepage
class HomeView(TemplateView):
    template_name = 'trips/index.html'

# trips_list: List all trips for the logged-in user
def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    return render(request, 'trips/trip_list.html', {'trips': trips})


# TripCreateView: Create a new trip
class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    success_url = reverse_lazy('trips-list')

    # Set the trip owner to the current user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# TripDetailView: Show details of a specific trip
class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip

    # Include related notes in the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.object.notes.all()
        return context

# TripUpdateView: Update an existing trip
class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    success_url = reverse_lazy('trips-list')

# TripDeleteView: Delete a trip
class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy('trips-list')

# NoteListView: List all notes for the logged-in user
class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    # Filter notes by the current user's trips
    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)

# NoteCreateView: Create a new note
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['trip', 'note', 'name', 'type', 'img', 'rating']
    success_url = reverse_lazy('note-list')

    # Limit the trip choices to those owned by the current user
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form

# NoteDetailView: Show details of a specific note
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

# NoteUpdateView: Update an existing note
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['trip', 'note', 'name', 'type', 'img', 'rating']
    success_url = reverse_lazy('note-list')

    # Limit the trip choices to those owned by the current user
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form

# NoteDeleteView: Delete a note
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
