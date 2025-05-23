from django.urls import re_path
from news.views import NewsListView, NewsDetailView


urlpatterns = [
    re_path(r'^$', NewsListView.as_view()),
    re_path(r'^(?P<new_slug>[\w\-]+)/$', NewsDetailView.as_view(), name="news_detail"),
]
