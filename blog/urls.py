from django.urls import path
from . import views

urlpatterns = [
    path(route = '', view = views.post_list, name = 'post_list'),
    path(route = 'post/<int:pk>/', view = views.post_detail, name = 'post_detail'),
    path(route = 'post/new/', view = views.post_new, name = 'post_new'),
    path(route = 'post/<int:pk>/edit', view = views.post_edit, name = 'post_edit'),
]