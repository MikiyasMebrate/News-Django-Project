from django.db import models
from fontawesome_5.fields import IconField

# Create your models here.
class NewsCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    writer = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='news')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self) -> str:
        return self.title\
        
class About(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    detail_description = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self) -> str:
        return self.title

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='members')

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Contact(models.Model):
    po_box = models.CharField(max_length=10)
    address_one = models.CharField(max_length=40)
    address_two = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.po_box + " " + self.phone

class SocialMedia(models.Model):
    name = models.CharField(max_length=20)
    icon = IconField()
    link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

