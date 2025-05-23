from django.urls import re_path
from peoples.views import PeopleListView, PeopleDetailView


urlpatterns = [
    re_path(r'^(?P<slug>[\w\-]+)/$', PeopleListView.as_view()),
    re_path(r'^(?P<people_slug>[\w\-]+)/detail/$', PeopleDetailView.as_view(), name="people_detail"),
]
