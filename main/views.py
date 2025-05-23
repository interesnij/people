from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from main.models import MediumMagicImage, MainBanner
from news.models import New


class MainPageView(TemplateView, CategoryListMixin):
	template_name = "main/mainpage.html"

	def get(self,request,*args,**kwargs):
		self.news = New.objects.only("pk")[0:6]
		return super(MainPageView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(MainPageView,self).get_context_data(**kwargs)
		context["medium_magic"] = MediumMagicImage.objects.last()
		context["banner"] = MainBanner.objects.last()
		context["news"] = self.news
		return context
