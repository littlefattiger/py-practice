import queue
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse

USER_QUEUE = {}


# Create your views here.
def home(request):
    uid = request.GET.get('uid')
    USER_QUEUE[uid] = queue.Queue()
    return render(request, 'home.html', {"uid": uid})


def send_msg(request):
    print("接收到客户端请求:", request.GET)
    text = request.GET.get('text')
    for uid, q in USER_QUEUE.items():
        q.put(text)

    return HttpResponse("ok")


def get_msg(request):
    uid = request.GET.get('uid')
    q = USER_QUEUE[uid]
    result = {'status':True, 'data':None}
    try:
        data = q.get(timeout=10)
        result['data'] = data
    except queue.Empty as e:
        result['status'] = False
    return JsonResponse(result)
