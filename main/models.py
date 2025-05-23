from django.db import models


class MainBanner(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to="main/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	description = models.TextField(null=True, blank=True, verbose_name="Краткое содержание")
	def __str__(self):
		return self.description

	class Meta:
		ordering = ["order"]
		verbose_name = "Баннер на главной"
		verbose_name_plural = "Баннеры на главной"


class MediumMagicImage(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to="main/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	def __str__(self):
		return self.order

	class Meta:
		ordering = ["order"]
		verbose_name = "Фото с магией в списке на главной"
		verbose_name_plural = "Фото с магией в списке на главной"

class BottomMagicImage(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to="main/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	def __str__(self):
		return self.order

	class Meta:
		ordering = ["order"]
		verbose_name = "Фото с магией внизу страницы"
		verbose_name_plural = "Фото с магией внизу страницы"
