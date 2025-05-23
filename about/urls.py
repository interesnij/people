from django.urls import re_path
from about.views import AboutView


urlpatterns = [
    re_path(r'^$', AboutView.as_view()),
]
