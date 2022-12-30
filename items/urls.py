from django.urls import path, include
from rest_framework.routers import DefaultRouter
from items import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet,basename="item")
router.register(r'users', views.UserViewSet,basename="user")
"""
Create a router and register our viewsets with it.
Django REST Framework Documentation: https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
"""

urlpatterns = [
    path('', include(router.urls)),
]
"""
The API URLs are now determined automatically by the router.
"""