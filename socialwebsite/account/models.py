from django.db import models
from django.conf import settings
import datetime
def user_path(instance, filename):
    date = str(datetime.date.today())
    return 'user/{0}/{1}/{2}'.format(date, instance.user.username, filename)


class Profile(models.Model):
	# settings.AUTH_USER_MODEL use to make a custom user authentication
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)

	photo = models.ImageField(upload_to=user_path, blank=True)



	def __str__(self):
		return f'Profile for user {self.user.username}'
