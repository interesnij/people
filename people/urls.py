from django.urls import re_path, include
from django.contrib import admin


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', include ('main.urls')),
    re_path(r'^categories/', include('categories.urls')),
    re_path(r'^people/', include('peoples.urls')),
    re_path(r'^frends/', include('frends.urls')),
    re_path(r'^about/', include('about.urls')),
    re_path(r'^policy/', include('policy.urls')),
    re_path(r'^news/', include('news.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
