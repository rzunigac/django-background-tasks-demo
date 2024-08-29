from django.shortcuts import render, redirect
from .tasks import send_email_task
from background_task.models import Task


def trigger_email(request):
    if request.method == 'POST':
        send_email_task()
        return redirect('success')
    return render(request, 'email_sender/trigger_email.html')


def success(request):
    scheduled_tasks = Task.objects.all()
    return render(request, 'email_sender/success.html', {'scheduled_tasks': scheduled_tasks})
