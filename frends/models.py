from django.db import models
from categories.models import FrendCategory
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Frend(models.Model):
    PERSON = 'P'
    COMPANY = 'C'
    ORG = 'O'
    COMMUNITY = 'CY'
    TYPE = (
        (PERSON, 'Персона'),
        (COMPANY, 'Компания'),
        (ORG, 'Организация'),
        (COMMUNITY, 'Сообщество'),
    )

    name = models.CharField(max_length=100,verbose_name="ФИО")
    frend_slug = models.CharField(max_length=100,verbose_name="Для ссылки")
    category = models.ForeignKey(FrendCategory,on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Краткое содержание")
    content = RichTextUploadingField(blank=True, default='', external_plugin_resources=[('youtube','/static/ckeditor_plugins/youtube/youtube/','plugin.js',)])
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")
    views = models.IntegerField(default=0,verbose_name="Просмотры")
    index_image = models.ImageField(upload_to="frends/list",verbose_name="Картинка в индекс")
    image = models.ImageField(blank=True,upload_to="frends/list",verbose_name="Главная картинка")
    type = models.CharField(blank=False, null=False, choices=TYPE, default=COMPANY, max_length=2, verbose_name="Тип друга")

    class Meta:
        verbose_name = "друг"
        verbose_name_plural = "друзья"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frend_detail',kwargs={"frend_slug":self.frend_slug})
