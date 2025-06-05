from django.urls import path
from . import views

urlpatterns = [
    path(route = '', view = views.post_list, name = 'post_list'),
    path(route = 'post/<int:pk>/', view = views.post_detail, name = 'post_detail'),
]