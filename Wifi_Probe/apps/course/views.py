from django.shortcuts import render, HttpResponse


# Create your views here.
def new_course(req):

    return HttpResponse("OK")


def elect_course(req):
    if req.method == 'POST':
        user_id = req.session.get('user_id')
        course_id = req.POST.get('course_id')
        if user_id and course_id:
            if



    return HttpResponse("OK")
