from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']
    list_display = ['author', 'post', 'published_at']


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['tags', 'likes']
    list_display = ['title', 'published_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
