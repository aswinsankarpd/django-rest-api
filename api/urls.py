from .views import *
from django.urls import path,include

urlpatterns = [
    path('',apiOverview,name="api-overview"),
    path('tasklist/',taskList,name="tasklist"),
    path('taskdetail/<int:pk>',taskdetail,name="taskdetail"),
    path('taskcreate/',taskcreate,name="taskcreate"),
    path('taskupdate/<int:pk>',taskupdate,name="taskupdate"),
    path('taskdelete/<int:pk>',taskdelete,name="taskdelete")
]