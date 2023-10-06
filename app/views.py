from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.POST:
        name = request.POST.get('name')
        psw = request.POST.get('password')

        myuser = authenticate(username=name, password=psw)

        if myuser is not None:
            login(request, myuser)
            return userPage(request, myuser)
        else:
            return userNotFound(request)

    return render(request, 'login.html')

def signup(request):
    if request.POST: 
        name = request.POST.get('name')
        email = request.POST.get('email')
        psw = request.POST.get('password')

        myuser = User.objects.create_user(username=name, email=email, password=psw) 
        myuser.save()

        return redirect('login')

    return render(request, 'signup.html')

def userNotFound(request):
    return render(request, 'userNotFound.html')

def userPage(request, user):
    return render(request, 'userPage.html', {'user': user})
