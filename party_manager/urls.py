from django.urls import path

from party_manager import views

urlpatterns = [
    path('<str:nom_party>/', views.party, name='party'),
    path('rejoindre_party', views.rejoindre_party, name="rejoindre_party")
]