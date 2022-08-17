from django.urls import path


from .views import Homepage, Search, Detalhesalbum, Playlist

app_name= 'musica'

urlpatterns = [
    path('',Homepage.as_view(), name='homepage'),
    path('search/',Search.as_view(), name='search'),
    path('detalhealbum/<int:pk>', Detalhesalbum.as_view(), name='detalhealbum'),
    path('playlist/', Playlist.as_view(), name='playlist'),
]
