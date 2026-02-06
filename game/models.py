from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Studio(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    country = models.CharField(max_length=200)
    bio = models.TextField()
    logo=models.ImageField(upload_to='studio_logos/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Platform(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Game(models.Model):
    
     title = models.CharField(max_length=200)
     categories = models.ManyToManyField(Categories, blank=True)
     studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
     platform = models.ManyToManyField(Platform, blank=True)
     release_date = models.DateField()
     description = models.TextField()
     cover_image = models.ImageField(upload_to='game_covers/')
     metacritic_score = models.IntegerField(null=True, blank=True)
     metacritic_url = models.URLField(null=True, blank=True)
     STAR_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
     ]
     user_rating = models.IntegerField(choices=STAR_CHOICES, null=True, blank=True)
     
     def __str__(self):
         return self.title
       
# Create your models here.
