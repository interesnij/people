from frends.models import Frend
from django.views.generic.list import ListView
from django.http import HttpResponse
from categories.models import FrendCategory
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class FrendListView(ListView, CategoryListMixin):
	model = Frend
	template_name = "frend_index.html"
	paginate_by = 9

	def get(self,request,*args,**kwargs):
		self.cat = FrendCategory.objects.get(slug=self.kwargs["slug"])
		return super(FrendListView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(FrendListView,self).get_context_data(**kwargs)
		context["category"] = self.cat
		return context

	def get_queryset(self):
		frend_list = Frend.objects.filter(category=self.cat).order_by("order")
		return frend_list


class FrendDetailView(TemplateView, CategoryListMixin):
	template_name = "frend.html"

	def get(self,request,*args,**kwargs):
		self.frend = Frend.objects.get(frend_slug=self.kwargs["frend_slug"])
		self.frend.views += 1
		self.frend.save()
		self.frends = Frend.objects.filter(category=self.frend.category)[0:6]
		return super(FrendDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(FrendDetailView,self).get_context_data(**kwargs)
		context["frends"] = self.frends
		context["object"] = self.frend
		return context
