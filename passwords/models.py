from django.db import models

# Create your models here.
class Password(models.Model):
	"""docstring for Password"models.Modelf __init__(self, arg):
		super(Password,models.Model.__init__()
		self.arg = arg

		"""
	ref = models.CharField(max_length=60)