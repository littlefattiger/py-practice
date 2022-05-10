from django.http import HttpResponse
from django.shortcuts import render
from app01.models import Department

# Create your views here.

def index(request):
    return HttpResponse("加油")


def user_list(request):
    return render(request, "user_list.html")

def orm(request):
    Department.objects.create(title="apple")
    return HttpResponse("成功")