from django.shortcuts import render

from courses.models import Course

from django.shortcuts import HttpResponse


def home(request):
    courses = Course.objects.all()
    print(courses)
    context = {'course':courses}
    return render(request,'courses/home.html',context )
