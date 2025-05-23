from django.shortcuts import render
from django.views.generic.base import ContextMixin
from news.models import New, NewsBanner
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class NewsListView(ListView, CategoryListMixin):
	model = New
	template_name = "news_index.html"
	paginate_by = 9

	def get(self,request,*args,**kwargs):
		return super(NewsListView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(NewsListView,self).get_context_data(**kwargs)
		context["banner"] = NewsBanner.objects.last()
		return context

	def get_queryset(self):
		news_list = New.objects.only("pk").order_by("-posted")
		return news_list


class NewsDetailView(TemplateView, CategoryListMixin):
	model = New
	template_name = "new.html"
	news = New.objects.all()[0:4]

	def get(self,request,*args,**kwargs):
		self.new = New.objects.get(new_slug=self.kwargs["new_slug"])
		self.new.views += 1
		self.new.save()
		return super(NewsDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(NewsDetailView,self).get_context_data(**kwargs)
		context["news"] = self.news
		context["object"] = self.new
		return context
