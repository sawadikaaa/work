from django.conf.urls import url
from django.urls import path
from . import views
app_name='learning_log1s'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]

    