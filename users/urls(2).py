from django.urls import path
from users.views import UserViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

user_list = UserViewSet.as_view({
    'get': 'list',
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', user_list, name='user-list'),
    path('<int:pk>/', user_detail, name='user-detail'),
])