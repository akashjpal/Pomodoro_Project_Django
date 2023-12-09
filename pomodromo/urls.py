from django.urls import path
from .views import pomodoro_timer

urlpatterns = [
    path('', pomodoro_timer, name='pomodoro_timer'),
]
