from django.db import models
from django.conf import settings
from django.utils.text import slugify
import datetime


def user_path(instance, filename):
    date = str(datetime.date.today())
    return 'images/{0}/{1}/{2}'.format(date, instance.user.username, filename)


class Images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to=user_path)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    def __str__(self):
        return self.title

    # if user did not enter the slug set title as slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
