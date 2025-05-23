from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название")
	slug = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название для url")
	image = models.ImageField(null=True, blank=True, upload_to="categories/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	description = models.TextField(null=True, blank=True, verbose_name="Краткое содержание")

	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория людей"
		verbose_name_plural = "категории людей"

	def __str__(self):
		return self.name


class FrendCategory(models.Model):
	name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название")
	slug = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название для url")
	image = models.ImageField(null=True, blank=True, upload_to="categories/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	description = models.TextField(null=True, blank=True, verbose_name="Краткое содержание")

	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория друзей"
		verbose_name_plural = "категории друзей"

	def __str__(self):
		return self.name
