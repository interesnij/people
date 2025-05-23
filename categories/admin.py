from django.contrib import admin
from categories.models import Category, FrendCategory

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['order', 'slug', 'image', 'name']
    list_filter = ['name']
    search_fields = ['name', 'posted']
    class Meta:
            model = Category


class FrendCategoryAdmin(admin.ModelAdmin):

    list_display = ['order', 'slug', 'image', 'name']
    list_filter = ['name']
    search_fields = ['name', 'posted']
    class Meta:
            model = FrendCategory


admin.site.register(Category, CategoryAdmin)
admin.site.register(FrendCategory, FrendCategoryAdmin)
