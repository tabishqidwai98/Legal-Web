from storage.views import CasesListView
from django.conf.urls import include
from django.urls import path

from .views import Cases_Fought_view, dashboard, detail_of_lawyer, register,index, User_Profile, lawyer_Profile, query_Lawyer_Profile, UserProfileListView, query_User_Profile, detail_of_User, CasesFoughtListView, query_Cases_Fought, detail_of_Cases_Fought, lawyerProfileListView

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('oauth/', include('social_django.urls')),
    path('',index,name='index'),
    path('add_lawyer/',lawyer_Profile,name='add_lawyer'),
    path('view_lawyer/', lawyerProfileListView.as_view(), name='view_lawyer'),
    path('profile/<int:pk>', detail_of_lawyer, name='lawyer_profile'),
    path('search_lawyer/', query_Lawyer_Profile,name='search_lawyer'),
    path('add_Users/',User_Profile,name='add_Users'),
    path('view_Users/',UserProfileListView.as_view(), name='view_Users'),
    path('User_profile/<int:pk>', detail_of_User, name='user_profile'),
    path('search_User/', query_User_Profile,name='search_User'),
    path('add_casesFought/',Cases_Fought_view, name='add_CasesFought'),
    path('view_fought/',CasesFoughtListView,name='view_fought'),
    path('fought/<int:pk>',detail_of_Cases_Fought, name='fought'),
    path('search_fought/',query_Cases_Fought,name='search_fought'),
]