from django.db import models

class File(models.Model):
    title = models.CharField(max_length=255)
    id_video = models.CharField(max_length=12, unique=True)
    file = models.FileField(upload_to='mp3/', blank=True)
    is_chart = models.BooleanField(default=False)
    country = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.title
