from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class New(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    new_slug = models.CharField(max_length=100,verbose_name="Для ссылки")
    description = models.TextField(verbose_name="Краткое содержание")
    content = RichTextUploadingField(blank=True, default='', external_plugin_resources=[('youtube','/static/ckeditor_plugins/youtube/youtube/','plugin.js',)])
    posted = models.DateTimeField(default=timezone.now,verbose_name="Опубликовано")
    views = models.IntegerField(default=0,verbose_name="Просмотры")
    image1 = models.ImageField(upload_to="blog/list",verbose_name="Картинка в индес")
    image2 = models.ImageField(blank=True,upload_to="blog/list",verbose_name="главная картинка в деталях")

    def get_absolute_url(self):
        return reverse('news_detail',kwargs={"new_slug":self.new_slug})

    class Meta:
        ordering = ["-posted"]
        verbose_name = "новость"
        verbose_name_plural = "новости"

    def __str__(self):
        return self.title


class NewsBanner(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to="main/list")
	order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
	description = models.TextField(null=True, blank=True, verbose_name="Краткое содержание")
	def __str__(self):
		return self.description

	class Meta:
		ordering = ["order"]
		verbose_name = "Баннер в разделе новости"
		verbose_name_plural = "Баннеры в разделе новости"
