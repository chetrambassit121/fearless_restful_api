from django.contrib.auth.models import User
from items.models import Item
from items.serializers import ItemSerializer
from items.serializers import UserSerializer
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework import status



@api_view(['GET'])
def api_root(request, format=None):
    """
    Creating an endpoint for the root of our API
    Django REST Framework Documentation: https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format)
    })



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Item List DELETE removes all items
    Item Instance DELETE removes that specfic item
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    """
    Defining the query, serializer, and permissions for this ViewSet  
    """


    def delete(self, request, format=None):
        """
        Defining a delete method for client to DELETE all Item objects in the database
        """
        items = Item.objects.all()
        if items:
            items.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
