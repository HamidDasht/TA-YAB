from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from .models import Request, StoredReplies, Timing, Reply
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
    if profile.type != TEACHER:
        return redirect('../std')

    
    requests = Request.objects.filter(owner=user).order_by('-datetime')
    p = Paginator(requests, 3)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(
        request, 'teach_main/profpage.html', 
    {'requests':page , 'teacher_name': user.first_name + ' ' + user.last_name,
    'email': user.email}
    )
    

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
    
    recent_requests = Request.objects.filter(owner=user).order_by('-datetime')[:2]

    if request.method == 'GET':
        return render(request, 'teach_main/addreq.html', {'success': False, 'recent_requests':recent_requests})
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
        new_req = Request(owner=user, course_name = course_name, description=description, masters=masters, bachelor=bachelor,
        prof_fname=user.first_name, prof_lname=user.last_name)
        new_req.save()
        while len(schedule_strings) != 0:
            new_time = Timing(day=days.pop(), start=start_times.pop(), end=finish_times.pop(), request=new_req)
            new_time.save()
            schedule_strings.pop()


    print(course_name)
    print(description)
    print(masters)
    print(bachelor)
    return render(request, 'teach_main/addreq.html', {'success': 'True', 'recent_requests':recent_requests})

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


@login_required(login_url='../../home')
def replies(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        user = request.user
        try:
            profile = UserProfile.objects.get(user__username=user.get_username())
        except: 
            return redirect('../home')
        if profile.type != TEACHER:
            return redirect('../prof')
        try:
            ta_request = Request.objects.filter(id=cid)[0]
        except:
            return redirect('../prof')
        if ta_request.owner != request.user:
            return redirect('../prof')
        
        if 'reppage' in request.GET:
            reply_aria_selected = True
            bookmark_aria_selected = False
        elif 'bookpage' in request.GET:
            reply_aria_selected = False
            bookmark_aria_selected = True
        else:
            reply_aria_selected = True
            bookmark_aria_selected = False

        # Retrieve all replies to the specified request
        replies = Reply.objects.filter(request=ta_request).order_by('datetime')
        # Retreive all bookmarked replies to the specified request
        bookmarks = StoredReplies.objects.filter(owner=user,reply__request__id=cid).order_by('-datetime_of_bookmark')

        bookmarked_ids = []
        for book in bookmarks:
            bookmarked_ids.append(book.reply.id)

        p = Paginator(replies, 3)
        page_num = request.GET.get('reppage', 1)
        try:
            reply_page = p.page(page_num)
        except EmptyPage:
            reply_page = p.page(1)

        p = Paginator(bookmarks, 3)
        page_num = request.GET.get('bookpage',1)
        try:
            bookmark_page = p.page(page_num)
        except:
            bookmark_page = p.page(1)

        return render(request, 'teach_main/replies.html',{ 
        'request':ta_request, 'replies':reply_page, 'bookmarks':bookmark_page, 'teacher_name': user.first_name + ' ' + user.last_name,
        'email': user.email, 'bookmark_aria_selected':bookmark_aria_selected, 'reply_aria_selected':reply_aria_selected,
        'bookmarked_ids':bookmarked_ids})

def accept_reply(request):
    if request.method == 'GET':
        reply_id = request.GET.get('id', False)
        if (reply_id != -1):
            related_reply = Reply.objects.filter(id=int(reply_id))[0]
            related_reply.is_accepted = True
            related_reply.save(update_fields=['is_accepted'])
            return JsonResponse({'status':'success', 'reply_id':reply_id})

def reject_reply(request):
    if request.method == 'GET':
        reply_id = request.GET.get('id', False)
        if (reply_id != -1):
            related_reply = Reply.objects.filter(id=int(reply_id))[0]
            related_reply.is_rejected = True
            related_reply.save(update_fields=['is_rejected'])
            return JsonResponse({'status':'success', 'reply_id':reply_id})

def bookmark_reply(http_request):
    if http_request.method == "POST":
        reply_id = http_request.POST.get('id', False)
        # Action can be either 'add' or 'delete'
        action = http_request.POST.get('action', 'add')
        print(reply_id)
        student_reply = Reply.objects.filter(id=reply_id)[0]
        print(student_reply)
        if StoredReplies.objects.filter(owner=http_request.user, reply=student_reply).exists():
            if action == "delete":
                print("Already bookmarked! Removing")
                StoredReplies.objects.filter(owner=http_request.user, reply=student_reply).delete()
                return JsonResponse({'status':'removed'})
            else:
                print("Already bookmarked!")
                return JsonResponse({'status': 'noaction'})
        else:
            print("New bookmark reply")
            new_bookmark_rep = StoredReplies(owner=http_request.user, reply=student_reply)
            new_bookmark_rep.save()
            return JsonResponse({'status': 'added'})

def delete_request(http_request):
    if http_request.method == "POST":
        request_id = http_request.POST.get('id', False)
        print(request_id)
        Request.objects.filter(id=request_id).delete()
        return JsonResponse({})
        return redirect('../home')
        """student_reply = Reply.objects.filter(id=reply_id)[0]
        print(student_reply)
        if StoredReplies.objects.filter(owner=http_request.user, reply=student_reply).exists():
            print("Already bookmarked!")
        else:
            print("New bookmark reply")
            new_bookmark_rep = StoredReplies(owner=http_request.user, reply=student_reply)
            new_bookmark_rep.save()
        return JsonResponse({})"""