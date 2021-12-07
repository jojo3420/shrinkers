from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member


# Create your views here.
def index(request):
    # return HttpResponse('ok')

    member = Member.objects.get(username='admin')

    return render(request, 'base.html', {
        'welcome_msg': 'welcome',
        'username': member.username
    })


def redirect_index(request):
    return redirect('index')
