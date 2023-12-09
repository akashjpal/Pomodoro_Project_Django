from django import forms
from .models import PomodoroSession

class PomodoroForm(forms.ModelForm):
    class Meta:
        model = PomodoroSession
        fields = ['is_running', 'duration', 'time_elapsed']
