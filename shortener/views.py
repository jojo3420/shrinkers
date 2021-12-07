from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Member


# Create your views here.
def index(request):
    # return HttpResponse('ok')
    try:
        member = Member.objects.get(username='admin_')
        username = member.username
    except Exception:
        username = 'Anonymous User'

    return render(request, 'base.html', {
        'welcome_msg': 'welcome',
        'username': username
    })


@csrf_exempt
def get_user(request, member_id: int):
    member = Member.objects.filter(pk=member_id).first()
    if request.method == 'GET':
        name = request.GET.get('name')
        age = request.GET.get('age')
        data = {'name': name, 'age': age}
        if member:
            data['member'] = member
        return render(request, 'base.html', data)
    elif request.method == 'POST':
        return JsonResponse(status=201, data={'msg': 'hello world'})
