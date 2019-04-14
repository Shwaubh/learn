from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

from sharetext.models import Data


def home(request):
    if request.user.is_authenticated:
        data = User.objects.exclude(is_superuser = 1).exclude(pk = request.user.pk)
        senddata = dict()
        senddata['loggedin'] = request.user
        senddata['data'] = data
        return render(request, 'sharetext/index.html', senddata)
    return render(request, 'sharetext/base.html', None)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username = username, password = password)
            return HttpResponse('User created successfully')
        except IntegrityError as e:
            return HttpResponse("User already exists")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('../')
        else:
            return HttpResponse("Error in username or password")


def logoutUser(request):
    logout(request)
    return redirect('../')


def sendmessage(request):
    if request.user.is_authenticated:
        receiver = User.objects.get(pk = request.POST['user'])
        if request.FILES['file']:
            print('file')
            data = Data(sender = request.user, receiver = receiver, msg = request.POST['msg'], file=request.FILES['file'])
        else:
            print('msg')
            data = Data(sender = request.user, receiver = receiver, msg = request.POST['msg'])
        data.save()
        return HttpResponse("message send successfully to "+receiver.username)


def sent(request, user):
    if request.user.is_authenticated and request.user.pk == user:
        data = Data.objects.filter(sender__pk = user)
        return render(request, 'sharetext/sent.html', {'sentdata' : data, 'loggedin' : request.user})
    else:
        return HttpResponse(request.user.is_authenticated)


def received(request, user):
    if request.user.is_authenticated and request.user.pk == user:
        data = Data.objects.filter(receiver__pk = user)
        return render(request, 'sharetext/received.html', {'receiveddata' : data, 'loggedin' : request.user})
    else:
        return HttpResponse(request.user.is_authenticated)


def handler404(request):
    print('hello')
    return render(request, 'sharetext/404.html', status=404)


def handler500(request):
    print('hello2')
    return render(request, 'sharetext/500.html', status=500)
