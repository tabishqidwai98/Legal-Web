from django.conf.urls import include
from django.urls import path
from .views import CasesListView
from .views import upload_form,detail_of_Cases,query_Cases

urlpatterns = [
    path('', CasesListView.as_view(), name='view_model'),
    path('model/<int:pk>', detail_of_Cases, name='detail_model'),
    path('upload/', upload_form, name='upload_ai_model'),
    path('search/', query_Cases, name='search_ai_model'),
]