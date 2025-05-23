from django.db import models


class AboutBanner(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to="main/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	description = models.TextField(null=True, blank=True, verbose_name="Краткое содержание")
	def __str__(self):
		return self.description

	class Meta:
		ordering = ["order"]
		verbose_name = "Баннер в разделе о нас"
		verbose_name_plural = "Баннеры в разделе о нас"
