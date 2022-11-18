from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name = 'home'),
    path('about/', views.about,  name = 'about'),
    path('cars/', views.cars_index,  name = 'index'),
    path('cars/<int:car_id>/', views.cars_detail, name = 'detail'),
    path('cars/create/', views.CarCreate.as_view(), name = 'cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name = 'cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name = 'cars_delete'),
    path('cars/<int:car_id>/add_mod/', views.add_mod, name = 'add_mod'),
    path('cars/<int:car_id>/assoc_track/<int:track_id>/', views.assoc_track, name = 'assoc_track'),
    path('cars/<int:car_id>/unassoc_track/<int:track_id>/', views.unassoc_track, name = 'unassoc_track'),
    path('tracks/', views.TrackList.as_view(), name='tracks_index'),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name='tracks_detail'),
    path('tracks/create/', views.TrackCreate.as_view(), name='tracks_create'),
    path('tracks/<int:pk>/update/', views.TrackUpdate.as_view(), name='tracks_update'),
    path('tracks/<int:pk>/delete/', views.TrackDelete.as_view(), name='tracks_delete'),
]