from django.shortcuts import render,redirect
from time import time
from courses.models import Course,Video,Payment
from OnlineCourse.settings import *
from django.shortcuts import HttpResponse
import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def checkout(request,slug):
    course = Course.objects.get(slug = slug)
    user = None
    if(request.user.is_authenticated is False):
        return redirect("login")
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    if action == 'create_payment':
        amount = int((course.price - (course.price * course.discount * 0.01))*100)
        currency = "INR"
        notes = {
            "email":user.email,
            "name":f'{user.first_name}{user.last_name}',}
        reciept = f"codewithkrishna-{int(time())}"
        order = client.order.create({"notes" : notes,"amount" : amount,"currency" : currency})

        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()



        
        

        
    context = {
        'course':course,
        'order':order,
        "payment":payment

    }
    return render(request,'courses/check_out.html',context)
