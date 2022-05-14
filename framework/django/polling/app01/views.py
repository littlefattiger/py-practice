from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
DB = []


# Create your views here.
def home(request):
    return render(request, 'home.html')


def send_msg(request):
    print("接收到客户端请求:", request.GET)
    text = request.GET.get('text')
    print(text)
    DB.append(text)
    return HttpResponse("ok")


def get_msg(request):
    index = int(request.GET.get('index'))
    context = {
        "data":  DB[index:] ,
        "max_index": len(DB)
    }
    return JsonResponse(context)
