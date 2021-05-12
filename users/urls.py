from django.conf.urls import include
from django.urls import path

from .views import Cases_Fought_view, dashboard, register,index, User_Profile, lawyer_Profile

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('oauth/', include('social_django.urls')),
    path('',index,name='index'),
    path('add_lawyer/',lawyer_Profile,name='add_lawyer'),
    path('add_Users/',User_Profile,name='add_Users'),
    path('add_casesFought/',Cases_Fought_view, name='add_CasesFought'),
]