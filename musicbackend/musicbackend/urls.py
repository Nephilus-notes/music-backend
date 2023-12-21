"""
URL configuration for musicbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('shows/', views.getShows),
    path('shows/<int:id>', views.getShow),
    path('patrons/', views.getPatrons),
    path('patrons/<int:id>/', views.getPatron),
    path('songs/', views.getSongs),
    path('songs/<int:id>/', views.getSongById),
    path('songs/<str:title>/', views.getSongByTitle),
    path('setlists/', views.getSetlists),
    path('setlists/<int:id>/', views.getSetlist),
    path('subscribe/', views.postSubscriber),
    path('request_song_to_learn/', views.postSong),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
