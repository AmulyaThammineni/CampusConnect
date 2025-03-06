
from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib import admin
from .models import *


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'query', 'response']
    search_fields = ['name', 'email', 'query']
    list_filter = ['sent_on']
    list_editable=['response']
    readonly_fields = ('name', 'email', 'query', 'sent_on')

    
# Register the ContactUs model with the custom admin class
admin.site.register(ContactUs, ContactUsAdmin)
