from django.contrib import admin
from django.contrib import admin

from .models import Feed, Category

class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'guid', 'pubDate']
    list_filter = ['Category_id']
    search_fields = ['title']
    list_per_page = 15


admin.site.register(Category)
admin.site.register(Feed, FeedAdmin)