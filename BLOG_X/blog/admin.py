from django.contrib import admin
from .models import Post, Comment, Category, Tag, Like, Follow
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','created','updated')
    search_fields = ('title','content','author__username')
    list_filter = ('category','created')
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Follow)
