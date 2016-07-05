from django.contrib import admin

from .models import Code, Event


class CodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code_type', 'keyb_number', 'card_number', 'valid_from', 'valid_to')


class EventAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'event_type', 'event_begin', 'event_end')

admin.site.register(Code, CodeAdmin)
admin.site.register(Event, EventAdmin)

