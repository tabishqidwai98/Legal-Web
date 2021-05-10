from django.conf.urls import include
from django.urls import path
from .views import AiModelListView
from .views import upload_form,detail_of_ai_model,query_ai_models

urlpatterns = [
    path('', AiModelListView.as_view(), name='view_model'),
    path('model/<int:pk>', detail_of_ai_model, name='detail_model'),
    path('upload/', upload_form, name='upload_ai_model'),
    path('search/', query_ai_models, name='search_ai_model'),
]