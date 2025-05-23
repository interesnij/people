from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class CategoriesView(TemplateView, CategoryListMixin):
    template_name = "categories.html"
