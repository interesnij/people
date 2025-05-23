from django.urls import re_path
from categories.views import CategoriesView


urlpatterns = [
    re_path(r'^$', CategoriesView.as_view()),
]
