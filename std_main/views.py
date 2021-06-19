from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from teach_main.models import Request,Reply,Timing
from .models import StoredRequests
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
    if profile.type != STUDENT:
        return redirect('../prof')

    global replying_course_id
    requests = Request.objects.all().order_by('-datetime')
    p_request = Paginator(requests, 3)
    page_num = request.GET.get('reqpage', 1)
    try:
        page_request = p_request.page(page_num)
    except EmptyPage:
        page_request = p_request.page(1)

    # Which tab is selected? (Requests/Replies/Bookmars)
    if 'reqpage' in request.GET:
        reply_aria_selected = False
        request_aria_selected = True
        bookmark_aria_selected = False
    elif 'reppage' in request.GET:
        reply_aria_selected = True
        request_aria_selected = False
        bookmark_aria_selected = False
    elif 'bookpage' in request.GET:
        request_aria_selected = False
        reply_aria_selected = False
        bookmark_aria_selected = True
    else:
        request_aria_selected = True
        reply_aria_selected = False
        bookmark_aria_selected = False


    # Get replies for replies page
    replies = Reply.objects.filter(owner=user).order_by('-datetime')
    #parent_request_of_reply = []
    #for rep in replies:
    #    parent_request_of_reply.append(rep.request)
    #print(parent_request_of_reply)
    #print(replies)
    #parent_request_of_reply = QuerySet(parent_request_of_reply)
    #print(parent_request_of_reply)
    p_reply = Paginator(replies, 3)
    page_num = request.GET.get('reppage', 1)
    try:
        page_reply = p_reply.page(page_num)
    except EmptyPage:
        page_reply = p_reply.page(1)

    bookmarks = StoredRequests.objects.filter(owner=user).order_by('-datetime_of_bookmark')
    p_bookmark = Paginator(bookmarks, 3)
    page_num = request.GET.get('bookpage', 1)
    try:
        page_bookmark = p_bookmark.page(page_num)
    except:
        page_bookmark = p_bookmark.page(1)

    if request.method == 'GET':
        return render(
            request, 'std_main/studentpage.html', 
        {'requests':page_request , 'std_name': user.first_name + ' ' + user.last_name, 
        'email': user.email, 'replies':page_reply, 'reply_aria_selected':reply_aria_selected
        ,'request_aria_selected':request_aria_selected, 'bookmark_aria_selected':bookmark_aria_selected
        , 'bookmarks':page_bookmark}
        )

    elif request.method == 'POST':
        if replying_course_id != -1:
            request_aria_selected = True
            reply_aria_selected = False
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
                 replier_lname=user.last_name, owner=user, request=related_req)
                new_reply.save()
            
            replying_course_id = -1
    try:
        print(reply_text)
    except:
        pass
    return render(request, 'std_main/studentpage.html', {'requests':page_request, 'replies': page_reply
    ,'success': True, 'email':user.email, 'std_name': user.first_name + ' ' + user.last_name
    ,'reply_aria_selected':reply_aria_selected,'request_aria_selected':request_aria_selected
    ,'bookmark_aia_selected': bookmark_aria_selected, 'bookmarks':page_bookmark})


@login_required(login_url='../home')
def send_reply(request):
    if request.method == 'GET':
        global replying_course_id
        replying_course_id = request.GET.get('id', False)
        print(replying_course_id)
        if (replying_course_id != -1):
            related_req = Request.objects.filter(id=int(replying_course_id))[0]
            
            related_timings = Timing.objects.filter(request=related_req)

            # Is the request already replied?
            try:
                reply = Reply.objects.filter(request=related_req,owner=request.user)[0]
            except:
                reply = None
            if reply:
                response = {"status": "403"}
                response['reply_text'] = reply.reply_text
                response['course_name'] = str(related_req.course_name)+ ' - ' + str(related_req.prof_lname)
                response['number_of_timings'] = len(related_timings)
                times = {}
                for i in range(0,len(related_timings)):
                    times[str(i)] = str(related_timings[i].day) + ' - ' + str(related_timings[i].start) + str(' تا ') + str(related_timings[i].end)
                response['times'] = times
                print(response)
                return JsonResponse(response)
            
            json_res = {"status": "200"}
            json_res['course_name'] = str(related_req.course_name)+ ' - ' + str(related_req.prof_lname)
            json_res['number_of_timings'] = len(related_timings)
            times = {}
            for i in range(0,len(related_timings)):
                times[str(i)] = str(related_timings[i].day) + ' - ' + str(related_timings[i].start) + str(' تا ') + str(related_timings[i].end)
            json_res['times'] = times
            #print(str(related_req.course_name)+ ' - ' + str(related_req.prof_lname))
            
            #print(json_res)
            #print(JsonResponse(json_res))
            return JsonResponse(json_res)
        else:
            return ' '
        
def bookmark_request(http_request):
    if http_request.method == "POST":
        request_id = http_request.POST.get('id', False)
        # Action can be either 'add' or 'delete'
        action = http_request.POST.get('action', 'add')
        print(request_id)
        ta_request = Request.objects.filter(id=request_id)[0]
        print(ta_request)
        if StoredRequests.objects.filter(owner=http_request.user, request=ta_request).exists():
            if action == "delete":
                print("Already bookmarked! Removing")
                StoredRequests.objects.filter(owner=http_request.user, request=ta_request).delete()
                return JsonResponse({'status':'removed'})
            else:
                print("Already bookmarked!")
                return JsonResponse({'status': 'noaction'}) 
        else:
            print("New bookmark request")
            new_bookmark_neq = StoredRequests(owner=http_request.user,request=ta_request)
            new_bookmark_neq.save()
            return JsonResponse({'status': 'added'})