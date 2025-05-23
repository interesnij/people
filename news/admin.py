from django.contrib import admin
from news.models import New, NewsBanner

class NewAdmin(admin.ModelAdmin):

    list_display = ['title', 'new_slug', 'posted', 'views']
    list_filter = ['title']
    search_fields = ['title', 'posted']
    class Meta:
            model = New

admin.site.register(New, NewAdmin)
admin.site.register(NewsBanner)
