from django.conf.urls import url
from . import views

urlpatterns = [
            url('posts_horse', views.post_list_hamster, name='post_list'),
]
