from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import PunchOutForm
from datetime import timedelta

def punch_in(request):
    if request.method == 'POST':
        task_description = request.POST.get('task_description')
        print(timezone.now())
        Task.objects.create(description=task_description, punch_in_time=timezone.now())
        return redirect('punch_out')
    return render(request, 'punch_in.html')

def punch_out(request):
    tasks = Task.objects.filter(punch_out_time__isnull=True)

    if request.method == 'POST':
        form = PunchOutForm(request.POST)

        # Check if 'status' is present in the form data
        if 'status' in request.POST:
            status = request.POST['status']

            for task in tasks:
                task.punch_out_time = timezone.now()
                task.status = status
                task.save()

            return redirect('work_summary')
    else:
        form = PunchOutForm()

    return render(request, 'punch_out.html', {'form': form})

def work_summary(request):
    tasks_completed = Task.objects.filter(punch_out_time__isnull=False)
    tasks_pending = Task.objects.filter(punch_out_time__isnull=True)
    total_seconds = sum([(task.punch_out_time - task.punch_in_time).total_seconds() for task in tasks_completed], 0)
    total_work_time = str(timedelta(seconds=total_seconds))
    context = {
        'tasks_completed': tasks_completed,
        'tasks_pending': tasks_pending,
        'total_work_time': total_work_time,
    }

    return render(request, 'work_summary.html', context)