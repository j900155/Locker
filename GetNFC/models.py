from django.db import models
from django.utils import timezone

# Create your models here.

class NFC(models.Model):
	NFC_PW=models.CharField(max_length=35)
	IO=models.CharField(max_length=5)

class Member(models.Model):
	user=models.CharField(max_length=20)
	def __unicode__(self):
		return self.user
class Box(models.Model):
	Box_id=models.CharField(max_length=3)
	Box_use=models.CharField(max_length=1)
	Box_size=models.CharField(max_length=2)
	def __unicode__(self):
		return self.Box_id
