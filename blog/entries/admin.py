from django.contrib import admin
from .models import Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_title','entry_text','entry_date','entry_author')

admin.site.register(Entry,EntryAdmin)