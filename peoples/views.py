from peoples.models import People
from django.views.generic.list import ListView
from django.http import HttpResponse
from categories.models import Category
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class PeopleListView(ListView, CategoryListMixin):
	model = People
	template_name = "people_index.html"
	paginate_by = 9

	def get(self,request,*args,**kwargs):
		self.cat = Category.objects.get(slug=self.kwargs["slug"])
		return super(PeopleListView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(PeopleListView,self).get_context_data(**kwargs)
		context["category"] = self.cat
		return context

	def get_queryset(self):
		people_list = People.objects.filter(category=self.cat).order_by("order")
		return people_list


class PeopleDetailView(TemplateView, CategoryListMixin):
	template_name = "people.html"

	def get(self,request,*args,**kwargs):
		self.people = People.objects.get(people_slug=self.kwargs["people_slug"])
		self.people.views += 1
		self.people.save()
		self.peoples = People.objects.filter(category=self.people.category)[0:6]
		return super(PeopleDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(PeopleDetailView,self).get_context_data(**kwargs)
		context["peoples"] = self.peoples
		context["object"] = self.people
		return context
