from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets, renderers
# ####
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    """
    Notice that we've also used the @action decorator to create a custom action, named highlight. 
    This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.

    Custom actions which use the @action decorator will respond to GET requests by default.
    We can use the methods argument if we wanted an action that responded to POST requests.

    The URLs for custom actions by default depend on the method name itself. 
    If you want to change the way url should be constructed, 
    you can include url_path as a decorator keyword argument.
    """
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perfrom_create(self, serializer):
        serializer.save(owner=self.request.user)
    
