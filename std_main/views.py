from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from teach_main.models import Request,Reply,Timing
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from register.models import STUDENT, UserProfile
from django.contrib.auth.decorators import login_required
import json

replying_course_id = -1

@login_required(login_url='../home')
def index(request):
    user = request.user
    print(user)
    try:
        profile = UserProfile.objects.get(user__username=user.get_username())
    except:
        return redirect('../home')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")
    if profile.type != STUDENT:
        return redirect('../prof')
        return HttpResponse("<h1>شما اجازه ی ورود به این صفحه را نداریم</h1>")

    global replying_course_id
    requests = Request.objects.all().order_by('-datetime')
    p = Paginator(requests, 3)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if request.method == 'GET':
        return render(
            request, 'std_main/studentpage.html', 
        {'requests':page , 'std_name': user.first_name + ' ' + user.last_name}
        )

    elif request.method == 'POST':
        if replying_course_id != -1:
            reply_text = request.POST.get('message-text',False)
            related_req = Request.objects.filter(id=int(replying_course_id))[0]
            num_of_times = len(Timing.objects.filter(request=related_req))
            reply_times = []
            for i in range(0, num_of_times):
                new_time = request.POST.get('time'+str(i), False)
                if new_time != False:
                    reply_times.append(str(new_time))

            print(reply_times)
            reply_times_str = ''
            for i in range(0, len(reply_times)):
                reply_times_str += str(reply_times[i])
            
            if (reply_text != False):
                new_reply = Reply(reply_text=reply_text+ ' ' + reply_times_str, replier_fname=user.first_name,
                 replier_lname=user.last_name, replier_id='2', request=related_req)
                new_reply.save()
            
            replying_course_id = -1

    print(reply_text)
    return render(request, 'std_main/studentpage.html', {'requests':page, 'success': True})


@login_required(login_url='../home')
def send_reply(request):
    if request.method == 'GET':
        global replying_course_id
        replying_course_id = request.GET.get('id', False)
        print(replying_course_id)
        if (replying_course_id != -1):
            related_req = Request.objects.filter(id=int(replying_course_id))[0]
            
            related_timings = Timing.objects.filter(request=related_req)
            json_res = {}
            json_res['course_name'] = str(related_req.course_name)+ ' - ' + str(related_req.prof_lname)
            json_res['number_of_timings'] = len(related_timings)
            times = {}
            for i in range(0,len(related_timings)):
                times[str(i)] = str(related_timings[i].day) + ' - ' + str(related_timings[i].start) + str(' تا ') + str(related_timings[i].end)
            json_res['times'] = times
            print(str(related_req.course_name)+ ' - ' + str(related_req.prof_lname))
            
            print(json_res)
            print(JsonResponse(json_res))
            return JsonResponse(json_res)
        else:
            return ' '
        
