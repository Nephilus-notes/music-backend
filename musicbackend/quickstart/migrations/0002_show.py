# Generated by Django 5.0 on 2023-12-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('venue_name', models.CharField(max_length=100)),
                ('venue_address', models.CharField(max_length=100)),
                ('venue_city', models.CharField(max_length=100)),
                ('venue_state', models.CharField(max_length=100)),
                ('venue_zip', models.CharField(max_length=100)),
                ('venue_country', models.CharField(max_length=100)),
                ('venue_url', models.CharField(max_length=100)),
                ('venue_phone', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('image_url', models.CharField(blank=True, max_length=100, null=True)),
                ('patron_attendees', models.ManyToManyField(to='quickstart.patron')),
            ],
        ),
    ]