from django.contrib.auth import views as auth_views
from .views import about, contact, lawyerProfileListView, CasesFoughtListView, UserProfileListView
from django.conf.urls import include
from django.urls import path
from . import views

from .views import Cases_Fought_view, dashboard,Rating,detail_of_lawyer, register,index, User_Profile_view, your_User_Profile, lawyer_Profile_views, query_Lawyer_Profile, query_User_Profile, detail_of_User, CasesFoughtListView, query_Cases_Fought, detail_of_Cases_Fought, ClientSignUpView, LawyerSignUpView

urlpatterns = [
    path('',index,name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('register/', register, name='register'),
    path('accounts/signup', register, name='register'),
    path('accounts/signup/client', ClientSignUpView.as_view(), name='client_register'),
    path('accounts/signup/lawyer', LawyerSignUpView.as_view(), name='lawyer_register'),
    path('oauth/', include('social_django.urls')),
    path('lawyer_profile/',views.lawyer_Profile,name='lawyer_profile'),
    path('client_profile/',views.client_Profile,name='client_profile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('rating/<int:pk>',views.rating,name='rating'),       
    


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