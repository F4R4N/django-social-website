from django.db import models
from django.conf import settings
import datetime
def user_path(instance, filename):
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    return 'user/{0}-{1}-{2}/{3}/{4}'.format(year, month, day, instance.user.username, filename)


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)

	photo = models.ImageField(upload_to=user_path, blank=True)



	def __str__(self):
		return f'Profile for user {self.user.username}'
