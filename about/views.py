from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from about.models import AboutBanner


class AboutView(TemplateView, CategoryListMixin):
    template_name="about.html"

    def get_context_data(self,**kwargs):
        context = super(AboutView,self).get_context_data(**kwargs)
        context["banner"] = AboutBanner.objects.last()
        return context
