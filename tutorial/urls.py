from django.contrib import admin
from django.urls import path, include
# 
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename="snippet")
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
]

# old
# urlpatterns += [
#     path('snippets/', include('snippets.urls')),
#     path('users/', include('users.urls')),
# ]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

# api root
urlpatterns += [
    path('', include(router.urls))
]
