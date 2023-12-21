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
def getShow(request, id):

    print(f'trying to get a show {id}')
    show = Show.objects.get(id=id)
    serializer = ShowSerializer(show)
    return Response(serializer.data)

@api_view(['GET'])
def getSongs(request):

    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSongById(request, id):

    song = Song.objects.get(id=id)
    serializer = SongSerializer(song)
    return Response(serializer.data)

@api_view(['GET'])
def getSongByTitle(request, title):

    song = Song.objects.get(title=title)
    serializer = SongSerializer(song)
    return Response(serializer.data)

@api_view(['GET'])
def getPatrons(request):

    patrons = Patron.objects.all()
    serializer = PatronSerializer(patrons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatron(request, id):

    patron = Patron.objects.get(id=id)
    serializer = PatronSerializer(patron)
    return Response(serializer.data)

@api_view(['GET'])
def getSetlists(request):

    setlists = Setlist.objects.all()
    serializer = SetlistSerializer(setlists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSetlist(request, id):

    setlist = Setlist.objects.get(id=id)
    serializer = SetlistSerializer(setlist)
    return Response(serializer.data)

@api_view(['POST'])
def postSong(request):
    '''Create a new song object in the database to be learned'''
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def postSubscriber(request):
    '''Create a new subscriber object in the database'''
    serializer = PatronSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
