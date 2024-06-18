from django.contrib import admin
from .models import Author, Post, Tag


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "author", "date",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
