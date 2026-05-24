from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=False)
    year = models. IntegerField()
    synopsis = models.TextField()
    picture = models.ImageField(upload_to='movies_images', null=True, blank=True)
    
    def __str__(self):
        return self.title