from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:id>/', views.SongDetail.as_view()),
]

    # path('music/<int:id>/', views.SongDetail.put),
    # path('music/<int:id>/', views.SongDetail.get),
    # path('music/<int:id>/', views.SongDetail.delete)