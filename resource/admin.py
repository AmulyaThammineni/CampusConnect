# Register your models here.
from django.contrib import admin
from .models import Resource
from django.contrib.admin import DateFieldListFilter

from datetime import datetime
from django.utils import timezone
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

# create ResourceAdmin
class ResourceAdmin(admin.ModelAdmin):
    # display these fields in admin panel
    list_display = ('title','user','uploaded_at')
    # add search bar
    search_fields = ('title','user','uploaded_at')
    # add filter
    list_filter = (
        # 'uploaded_at',
        ("uploaded_at", DateRangeQuickSelectListFilterBuilder()), 
        'branch',
        'user',
    )



admin.site.register(Resource, ResourceAdmin)


