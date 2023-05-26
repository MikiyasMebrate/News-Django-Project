from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.NewsCategory)
admin.site.register(models.News)
admin.site.register(models.About)
admin.site.register(models.Team)
admin.site.register(models.Contact)
admin.site.register(models.SocialMedia)