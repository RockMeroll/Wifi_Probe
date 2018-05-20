from django.shortcuts import render, HttpResponse
from apps.course.models import *

# Create your views here.
def new_course(req):

    return HttpResponse("OK")


def elect_course(req):
    if req.method == 'POST':
        user_id = req.session.get('user_id')
        course_id = req.POST.get('course_id')

        try:
            if user_id and course_id and \
                    Courseselect.objects.filter(cid=course_id, sid=user_id).count() == 0:
                Courseselect.objects.create(cid=course_id, sid=user_id)
                return HttpResponse("Success")
        except ValueError as ve:
            return HttpResponse(str(ve))

    return HttpResponse("OK")
