from django.urls import re_path
from frends.views import FrendListView, FrendDetailView


urlpatterns = [
    re_path(r'^(?P<slug>[\w\-]+)/$', FrendListView.as_view()),
    re_path(r'^(?P<frend_slug>[\w\-]+)/detail/$', FrendDetailView.as_view(), name="frend_detail"),
]
