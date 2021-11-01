from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:id>/', views.SongList.get_single),
]