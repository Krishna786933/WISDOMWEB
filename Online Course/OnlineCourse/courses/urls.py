from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from courses.views import home,coursePage,SignupView,LoginView,signout,checkout

from OnlineCourse.settings import MEDIA_URL, MEDIA_ROOT
urlpatterns = [


    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('logout',signout,name='logout'),

    path('signup',SignupView.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('course/<str:slug>',coursePage,name='coursePage'),
    path('check-out/<str:slug>',checkout,name='checkout'),



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)