from django.shortcuts import render, redirect
from .forms import PomodoroForm
from .models import PomodoroSession


def pomodoro_timer(request):
    session = PomodoroSession.objects.first()
    form = PomodoroForm(instance=session)

    if request.method == 'POST':
        form = PomodoroForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('pomodoro_timer')

    return render(request, 'pomodromo_timer.html', {'form': form})
