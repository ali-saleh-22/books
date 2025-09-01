from django.contrib import admin
from appbooks.models import Book, Category


# Register your models here.
class C(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class B(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, B)
admin.site.register(Category, C)
