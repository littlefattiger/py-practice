from django.shortcuts import render

# Create your views here.
from app01 import models


def home(request):
    user = request.GET.get('user')

    data_list = models.AuditTask.objects.filter(user=user, status=2).select_related("task")

    return render(request, 'home.html', {"data_list": data_list, "user": user})


def audit(request):
    user = request.GET.get('user')
    task_id = request.GET.get('tid')
    task_object = models.Task.objects.filter(id=task_id).first()
    print(task_object)
    return render(request, 'audit.html', {'user': user, 'task_id': task_id, "task_object": task_object})
