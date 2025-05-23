from django.contrib import admin
from frends.models import Frend


class FrendAdmin(admin.ModelAdmin):

    list_display = ['name', 'frend_slug', 'order', 'views']
    list_filter = ['name']
    search_fields = ['name', 'order']
    class Meta:
            model = Frend

admin.site.register(Frend, FrendAdmin)
