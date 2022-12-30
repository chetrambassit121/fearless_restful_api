from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
]
"""
Pattern for admin and the urls in the items app
"""


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
"""
Pattern to include the login and logout views for the browsable API
Django REST Framework Documentation: https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-login-to-the-browsable-api
"""
