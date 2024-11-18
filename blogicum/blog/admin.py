from django.contrib import admin

from .models import Post, Location, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
    )
    list_editable = (
        'is_published',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_published',
        'category',
    )
    list_editable = (
        'is_published',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Category, CategoryAdmin)
