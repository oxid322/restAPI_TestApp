from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('adds/',
         views.AddListView.as_view(),
         name='add_list'),
    path('adds/<pk>/',
         views.AddDetailView.as_view(),
         name='add_detail')
]