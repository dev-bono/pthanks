from django.db import models
from django.utils.encoding import force_bytes

# Create your models here.
class Thanks(models.Model):
	user_id = models.IntegerField()
	thanks_to = models.IntegerField()
	memo = models.TextField(max_length=500)
	create_dt = models.DateTimeField()
	heart_count = models.IntegerField()
	thanks_type = models.CharField(max_length=1)

	def __str__(self):
		# Note use of django.utils.encoding.force_bytes() here because
		# first_name and last_name will be unicode strings.
		return '%s' % self.memo
