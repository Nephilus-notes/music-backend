from django.db import models

class Setlist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    show_id = models.ForeignKey(
        'Show',
        on_delete=models.CASCADE,
    )
    show_order = models.IntegerField()
