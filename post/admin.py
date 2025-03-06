from django.contrib import admin
from .models import *

# Register your models here.
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

# create PostAdmin
class PostAdmin(admin.ModelAdmin):
    # display these fields in admin panel
    list_display = ('title','user','created_at')
    # add search bar
    search_fields = ('title','author','created_at')
    # add filter
    list_filter = (
        ('created_at', DateRangeQuickSelectListFilterBuilder()), 
        'branch','user')


# create PostComment
class PostCommentAdmin(admin.ModelAdmin):
    # display these fields in admin panel
    list_display = ('user','post','comment','created_at')
    # add search bar
    search_fields = ('user','post','comment')
    # add filter
    list_filter = (
        ('created_at', DateRangeQuickSelectListFilterBuilder()), 
        )

admin.site.register(Post,PostAdmin)
admin.site.register(PostComment,PostCommentAdmin)