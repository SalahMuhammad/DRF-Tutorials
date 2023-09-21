from django.urls import path, include
from api.views import api_root

urlpatterns = [
    path('', api_root),
    path('snippets/', include('snippets.urls')),
    path('users/', include('users.urls')),
]