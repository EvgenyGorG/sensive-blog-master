from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']
    list_display = ['author', 'post', 'published_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['tags', 'likes']
    list_display = ['title', 'published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass