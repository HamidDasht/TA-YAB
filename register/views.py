from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import STUDENT, TEACHER, UserProfile, TYPE_CHOICES, DEPT_CHOICES

from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../home')
def home(request):
    user = request.user
    print(user)
    try:
        profile = UserProfile.objects.get(user__username=user.get_username())
    except:
        return redirect('../home')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    if profile.type == STUDENT:
        return redirect('../std')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    elif profile.type == TEACHER:
        return redirect('../prof')
    return redirect('home/')

def loginPage(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        try:
            profile = UserProfile.objects.get(user__username=user.get_username())
        except:
            return redirect('../home')
            return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
        if profile.type == STUDENT:
            return redirect('../std')
            return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
        elif profile.type == TEACHER:
            return redirect('../prof')
            #return render(request, 'registration/logout.html', {})
    
    next = request.GET.get('next')
    form = UserLoginForm( request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate( username=username, password=password )
        
        login(request, user)
        profile = UserProfile.objects.get(user__username=user.get_username())
        
        if profile.type == TEACHER :
            return redirect('../prof')
        elif profile.type == STUDENT:
            return redirect('../std')
        #return render(request, 'registration/logout.html', {})

    context = {
        'form':form,
    }
    return render(request, 'registration/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')