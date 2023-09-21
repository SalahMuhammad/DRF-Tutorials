from rest_framework import viewsets
from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve' actions.

    Here we've used the 'ReadOnlyModelViewSet' class to automatically provide the default 'read-only' operations. 
    We're still setting the 'queryset' and 'serializer_class' attributes exactly as we did when we were using regular views, 
    but we no longer need to provide the same information to two separate classes.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer