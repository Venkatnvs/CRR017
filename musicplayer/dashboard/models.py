from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    src = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.name