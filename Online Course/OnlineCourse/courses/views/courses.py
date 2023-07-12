from django.shortcuts import render,redirect

from courses.models import Course,Video

from django.shortcuts import HttpResponse


def coursePage(request,slug):
    print(request.user)
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    print(serial_number)
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course  = course)
    if(request.user.is_authenticated is False and video.is_preview is False):
        return redirect("login")
    context = {
        'course':course,
        'video': video,

    }
    return render(request,'courses/course_page.html',context)
