from django.urls import re_path
from policy.views import PolicyView


urlpatterns = [
    re_path(r'^$', PolicyView.as_view()),
]
