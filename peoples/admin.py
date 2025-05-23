from django.contrib import admin
from peoples.models import People

class PeopleAdmin(admin.ModelAdmin):

    list_display = ['name', 'people_slug', 'order', 'views']
    list_filter = ['name']
    search_fields = ['name', 'order']
    class Meta:
            model = People

admin.site.register(People, PeopleAdmin)
