from django.contrib import admin
from django.urls import path, include

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
    path('', include('api.urls'))
]
