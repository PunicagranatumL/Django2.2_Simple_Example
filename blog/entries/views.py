from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry

# Create your views here.

#def index(request):
    #return render(request,'entries/index.html')

class HomeView(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blogentries"
    ordering = ['-entry_date']
    paginate_by = 2

class EntryView(LoginRequiredMixin,DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title','entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)