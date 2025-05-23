from django.views.generic.base import ContextMixin
from django.conf import settings
from categories.models import Category, FrendCategory
from main.models import BottomMagicImage


class CategoryListMixin(ContextMixin):

	def get_context_data(self,**kwargs):
		context = super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"] = self.request.path
		context["bottom_magic"] = BottomMagicImage.objects.only("pk").last()
		context["categories"] = Category.objects.only("pk")
		context["frend_categories"] = FrendCategory.objects.only("pk")
		return context
