from django.db import models
from categories.models import Category
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class People(models.Model):
    name = models.CharField(max_length=100,verbose_name="ФИО")
    people_slug = models.CharField(max_length=100,verbose_name="Для ссылки")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Краткое содержание")
    content = RichTextUploadingField(blank=True, default='', external_plugin_resources=[('youtube','/static/ckeditor_plugins/youtube/youtube/','plugin.js',)])
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
    views = models.IntegerField(default=0,verbose_name="Просмотры")
    index_image = models.ImageField(upload_to="peoples/list",verbose_name="Картинка в индекс")
    image = models.ImageField(blank=True,upload_to="peoples/list",verbose_name="Главная картинка")

    class Meta:
        verbose_name = "человек"
        verbose_name_plural = "люди"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people_detail',kwargs={"people_slug":self.people_slug})
