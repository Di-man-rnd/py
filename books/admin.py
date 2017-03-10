from django.contrib import admin

from .models import Autor, Publisher, Book


class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')                        # выводимые поля
    search_fields = ('first_name', 'last_name')                                # поиск по полям


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'publisher')
    list_filter = ('publisher', 'autor', 'publication_date')                   # фильтр
    date_hierarchy = 'publication_date'                                        # фильтр для дат
    ordering = ['title']                                                       # упорядочили записи для админки


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)