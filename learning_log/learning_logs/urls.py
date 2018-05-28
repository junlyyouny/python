"""定义learning_logs的URL模式"""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('set_topic_public/<int:topic_id>', views.set_topic_public, name='set_topic_public'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]