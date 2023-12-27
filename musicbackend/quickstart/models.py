from django.db import models

# Create your models here.
class Patron(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True) 
    country =  models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_patron = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    one_time_donation = models.IntegerField(null=True, blank=True)
    recurring_donation = models.IntegerField(null=True, blank=True)
    times_at_show = models.IntegerField(null=True, blank=True)

class Show(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=100)
    venue_city = models.CharField(max_length=100)
    venue_state = models.CharField(max_length=100)
    venue_zip = models.CharField(max_length=100)
    venue_country = models.CharField(max_length=100)
    venue_url = models.CharField(max_length=100)
    venue_phone = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)    
    event_type = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100,null=True, blank=True)
    patron_attendees = models.ManyToManyField('Patron')


class Setlist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    # show_id = models.ForeignKey(
    #     'Show',
    #     on_delete=models.CASCADE,
    # )
    shows = models.ManyToManyField('Show')
    show_order = models.IntegerField()

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    audio_url = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.CharField(max_length=100, null=True, blank=True)
    times_requested = models.IntegerField(default=0)
    lyrics = models.TextField(null=True, blank=True)
    tab = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    sets = models.ManyToManyField('Setlist', null=True, blank=True)
    requesting_patrons = models.ManyToManyField('Patron', null=True, blank=True)
    known = models.BooleanField(default=False)

class SongSetlist(models.Model):
    id = models.AutoField(primary_key=True)
    song_id = models.ForeignKey(
        'Song',
        on_delete=models.CASCADE,
    )
    setlist_id = models.ForeignKey(
        'Setlist',
        on_delete=models.CASCADE,
    )
    order_number = models.IntegerField()

class ShowSetlist(models.Model):
    id = models.AutoField(primary_key=True)
    show_id = models.ForeignKey(
        'Show',
        on_delete=models.CASCADE,
    )
    setlist_id = models.ForeignKey(
        'Setlist',
        on_delete=models.CASCADE,
    )
    order_number = models.IntegerField()

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    log_type = models.CharField(max_length=100)
    log_message = models.TextField()
    log_date = models.DateTimeField(auto_now_add=True)

class SongRequest(models.Model):
    id = models.AutoField(primary_key=True)
    song_id = models.ForeignKey(
        'Song',
    )
    show_id = models.ForeignKey(
        'Show',
    )
    name = models.CharField(max_length=100)
    patron_id = models.ForeignKey(
        'Patron', null=True, blank=True
    )
    