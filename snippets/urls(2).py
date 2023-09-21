from django.urls import path
from snippets.views import SnippetViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = format_suffix_patterns([
    path('', snippet_list, name='snippet-list'),
    path('<int:pk>/', snippet_detail, name='snippet-detail'),
    path('<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
])