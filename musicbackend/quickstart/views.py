from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework_swagger.views import get_swagger_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Setlist, Show, Patron, Song
from .serializers import SetlistSerializer, ShowSerializer, PatronSerializer, SongSerializer

# from django.conf.urls import url



# Create your views here.

from quickstart.serializers import GroupSerializer, UserSerializer

# schema_view = get_swagger_view(title='Music API')

# urlpatterns = [
#     url(r'^$', schema_view),
# ]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def getShows(request):

    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSongs(request):

    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatrons(request):

    patrons = Patron.objects.all()
    serializer = PatronSerializer(patrons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSetlists(request):

    setlists = Setlist.objects.all()
    serializer = SetlistSerializer(setlists, many=True)
    return Response(serializer.data)
