from django.contrib import admin
from .models import Book, User, Loan

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_year', 'is_available')
    search_fields = ('title', 'author', 'publisher')
    list_filter = ('publication_year', 'is_available')

admin.site.register(Book, BookAdmin)
admin.site.register(User)
admin.site.register(Loan)