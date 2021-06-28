from django.conf.urls import include
from django.urls import path
from .views import upload_form,detail_of_Cases,query_Cases,delete_case,edit_Case,case_view

urlpatterns = [
    path('cases', case_view , name='view_cases'),
    path('cases/<int:pk>', detail_of_Cases, name='detail_cases'),
    path('upload/', upload_form, name='upload_cases'),
    path('search/', query_Cases, name='search_cases'),
    path('deletecase/<int:pk>', delete_case, name='delete_case'),
    path('editcase/<int:pk>', edit_Case, name='edit_case'),
]