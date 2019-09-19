from django.db import models

class Url(models.Model):
	original_url = models.CharField("Url", "original_url", max_length=200)
	url_code = models.CharField("Short url", "url_code", max_length=8)

	def __str__(self):
		return self.original_url
