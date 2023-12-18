from django.contrib.auth.models import Group, User
from rest_framework import serializers

# from .models import Song
# from .models import Show
# from .models import Patron
# from .models import Setlist
from .models import Setlist, Show, Patron, Song, Log

# from quickstart.models import Patron

# from .models.song import Song
# from .models.show import Show
# from .models.patron import Patron
# from .models.setlist import Set


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PatronSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100, required=False)
    address = serializers.CharField(max_length=100, required=False)
    city = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=100, required=False)
    zip_code = serializers.CharField(max_length=100, required=False) 
    country =  serializers.CharField(max_length=100, required=False)
    is_admin = serializers.BooleanField(default=False)
    is_artist = serializers.BooleanField(default=False)
    is_patron = serializers.BooleanField(default=False)
    is_subscribed = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)
    deleted = serializers.BooleanField(required=False)
    one_time_donation = serializers.IntegerField(required=False)
    recurring_donation = serializers.IntegerField(required=False)
    times_at_show = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Patron` instance, given the validated data.
        """
        return Patron.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Patron` instance given the validated data
        """ 
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.country = validated_data.get('country', instance.country)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_artist = validated_data.get('is_artist', instance.is_artist)
        instance.is_patron = validated_data.get('is_patron', instance.is_patron)
        instance.is_subscribed = validated_data.get('is_subscribed', instance.is_subscribed)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.one_time_donation = validated_data.get('one_time_donation', instance.one_time_donation)
        instance.recurring_donation = validated_data.get('recurring_donation', instance.recurring_donation)
        instance.times_at_show = validated_data.get('times_at_show', instance.times_at_show)
        instance.save()
        return instance

class ShowSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()   
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)
    deleted = serializers.BooleanField(required=False)
    venue_name = serializers.CharField(max_length=100)
    venue_address = serializers.CharField(max_length=100)
    venue_city = serializers.CharField(max_length=100)
    venue_state = serializers.CharField(max_length=100)
    venue_zip = serializers.CharField(max_length=100)
    venue_country = serializers.CharField(max_length=100)
    venue_url = serializers.CharField(max_length=100)
    venue_phone = serializers.CharField(max_length=100)
    short_description = serializers.CharField(max_length=100)    
    event_type = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=100, required=False)
    patron_attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Show` instance, given the validated data.
        """
        return Show.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Show` instance given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.venue_name = validated_data.get('venue_name', instance.venue_name)
        instance.venue_address = validated_data.get('venue_address', instance.venue_address)
        instance.venue_city = validated_data.get('venue_city', instance.venue_city)
        instance.venue_state = validated_data.get('venue_state', instance.venue_state)
        instance.venue_zip = validated_data.get('venue_zip', instance.venue_zip)
        instance.venue_country = validated_data.get('venue_country', instance.venue_country)
        instance.venue_url = validated_data.get('venue_url', instance.venue_url)
        instance.venue_phone = validated_data.get('venue_phone', instance.venue_phone)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.patron_attendees = validated_data.get('patron_attendees', instance.patron_attendees)
        instance.save()
        return instance


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    artist = serializers.CharField(max_length=100)
    album = serializers.CharField(max_length=100, required=False)
    genre = serializers.CharField(max_length=100, required=False)
    year = serializers.IntegerField(required=False)
    audio_url = serializers.CharField(max_length=100, required=False)
    image_url = serializers.CharField(max_length=100, required=False)
    times_requested = serializers.IntegerField(default=0)
    lyrics = serializers.CharField(required=False)
    tab = serializers.CharField(required=False)
    video_url = serializers.CharField(max_length=100, required=False)
    duration = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)
    deleted = serializers.BooleanField(required=False)
    sets = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
    requesting_patrons = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Song` instance, given the validated data.
        """
        return Song.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Song` insance, given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.year = validated_data.get('year', instance.year)
        instance.audio_url = validated_data.get('audio_url', instance.audio_url)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.times_requested = validated_data.get('times_requested', instance.times_requested)
        instance.lyrics = validated_data.get('lyrics', instance.lyrics)
        instance.tab = validated_data.get('tab', instance.tab)
        instance.video_url = validated_data.get('video_url', instance.video_url)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.requesting_patrons = validated_data.get('requesting_patrons', instance.requesting_patrons)
        instance.save()
        return instance
    


class SetlistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)
    deleted = serializers.BooleanField(required=False)
    shows = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Setlist` instance, given the validated data.
        """
        return Setlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Setlist` instance given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.show_id = validated_data.get('show_id', instance.show_id)
        instance.songs = validated_data.get('songs', instance.songs)
        instance.save()
        return instance
    
# add serializer for logs
class LogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    log_type = serializers.CharField(max_length=100)
    log_message = serializers.DateTimeField(required=False)
    created_at = serializers.DateTimeField(required=False)
    

    def create(self, validated_data):
        """
        Create and return a new `Log` instance, given the validated data.
        """
        return Log.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Log` instance given the validated data
        """
        
        instance.log_type = validated_data.get('log_type', instance.log_type)
        instance.log_message = validated_data.get('log_message', instance.log_message)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance