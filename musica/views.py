from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Album
# Create your views here.

class Homepage(ListView):
    template_name = 'homepage.html'
    model = Album

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['romance'] = self.model.objects.filter(categoria=self.get_object().categoria)
    #     return context


class Detalhesalbum(DetailView):
    template_name = 'detalhealbum.html'
    model = Album




class Search(ListView):
    template_name = 'search.html'
    model = Album

class Playlist(ListView):
    template_name = 'playlist.html'
    model = Album