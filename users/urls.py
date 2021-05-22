from storage.views import CasesListView
from .views import lawyerProfileListView, CasesFoughtListView, UserProfileListView
from django.conf.urls import include
from django.urls import path
from users import views

from .views import Cases_Fought_view, dashboard, detail_of_lawyer, register,index, User_Profile_view, lawyer_Profile_views, query_Lawyer_Profile, UserProfileListView, query_User_Profile, detail_of_User, CasesFoughtListView, query_Cases_Fought, detail_of_Cases_Fought, lawyerProfileListView, your_User_Profile

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('oauth/', include('social_django.urls')),
    path('',index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('add_lawyer/',lawyer_Profile_views,name='add_lawyer'),
    path('view_lawyer/', lawyerProfileListView.as_view(), name='view_lawyer'),
    path('detail_lawyer/<int:pk>', detail_of_lawyer, name='lawyer_profile'),
    path('search_lawyer/', query_Lawyer_Profile,name='search_lawyer'),

    path('add_User/',User_Profile_view,name='add_Users'),
    path('view_User/',UserProfileListView.as_view(), name='view_Users'),
    path('detail_User/<int:pk>', detail_of_User, name='user_profile'),
    path('Search_User/', query_User_Profile,name='search_User'),
    path('your_profile_user/<int:pk>',your_User_Profile,name='your_profile_user'),

    path('add_casesFought/',Cases_Fought_view, name='add_CasesFought'),
    path('view_casesFought/',CasesFoughtListView.as_view(),name='view_fought'),
    path('detail_casesFought/<int:pk>',detail_of_Cases_Fought, name='fought'),
    path('search_casesFought/',query_Cases_Fought,name='search_fought'),
]