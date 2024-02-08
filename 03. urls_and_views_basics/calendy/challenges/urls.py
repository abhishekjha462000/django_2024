from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('<int:value>', views.monthly_challenge_by_integer),
    path('<month>', views.monthly_challenge, name = 'monthly-challenge'),
]