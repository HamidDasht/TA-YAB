from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Request, Timing
from django.http import HttpResponseRedirect
from register.models import TEACHER, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../home')
def index(request):
    user = request.user
    print(user)
    try:
        profile = UserProfile.objects.get(user__username=user.get_username())
    except:
        return redirect('../home')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    if profile.type != TEACHER:
        return redirect('../std')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    return render(request, 'teach_main/profpage.html',  {'teacher_name': user.first_name + ' ' + user.last_name,
    'email': user.email})


start_times = []
finish_times = []
days = []

schedule_strings = []

@login_required(login_url='../home')
def addreq(request):
    user = request.user
    print(user)
    try:
        profile = UserProfile.objects.get(user__username=user.get_username())
    except:
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    if profile.type != TEACHER:
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    
    if request.method == 'GET':
        return render(request, 'teach_main/addreq.html', {'success': False})
    elif request.method == 'POST':
        course_name = request.POST.get('CourseName',False)
        description = request.POST.get('validationTextarea',False)

        if request.POST.get('customControlAutosizing','k') == 'on':
            masters = True
        else:
            masters = False

        if request.POST.get('customControlAutosizing1','k') == 'on':
            bachelor = True
        else:
            bachelor = False
    
    if (course_name != False):
        new_req = Request(course_name = course_name, description=description, masters=masters, bachelor=bachelor,
        prof_fname=user.first_name, prof_lname=user.last_name, prof_id='123')
        new_req.save()
        while len(schedule_strings) != 0:
            new_time = Timing(day=days.pop(), start=start_times.pop(), end=finish_times.pop(), request=new_req)
            new_time.save()
            schedule_strings.pop()


    print(course_name)
    print(description)
    print(masters)
    print(bachelor)
    return render(request, 'teach_main/addreq.html', {'success': 'True'})

    #return HttpResponse(request.POST.get('CourseName',False))

@login_required(login_url='../home')
def add_time(request):
    if request.method == 'POST':
        time_start = request.POST.get('Time1',False)
        time_end = request.POST.get('Time2',False)
        day = request.POST.get('Day', False)

        schedule_string = str(time_start) + str(time_end) + str(day)
        if schedule_string not in schedule_strings:
            print(time_start)
            print(time_end)
            print(day)
            schedule_strings.append(schedule_string)
            start_times.append(time_start)
            finish_times.append(time_end)
            if day == 'sat':
                str_day = 'شنبه'
            elif day == 'sun':
                str_day = 'یک شنبه'
            elif day == 'mon':
                str_day = 'دو شنبه'
            elif day == 'tu':
                str_day = 'سه شنبه'
            elif day == 'wed':
                str_day = 'چهارشنبه'
            days.append(str_day)
        return HttpResponse('')