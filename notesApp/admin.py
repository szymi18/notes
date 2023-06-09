from django.contrib import admin

from notesApp.models import Note
# Register your models here.

@admin.register(Note)
class adminNote(admin.ModelAdmin):
    list_display = ('title', 'content', 'creation_date', 'author')