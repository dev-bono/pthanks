from django.db import models

# Create your models here.
class User(models.Model):
	nickname = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=20)
	remain_heart = models.IntegerField()
	create_dt = models.DateTimeField()

	def __str__(self):
		return self.nickname