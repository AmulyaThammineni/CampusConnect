from django.contrib import admin

# Register your models here.
from .models import Branch,Department

class BranchAdmin(admin.ModelAdmin):
    list_display=(
        'department',
        'branch_name',
    )
    search_fields=[
        'department',
        'branch_name',
        
    ]
    list_editable= ['branch_name']
    list_filter=['department']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=[
        'department_name'
    ]
    
    search_fields=[
        'department_name',
        
    ]

admin.site.register(Branch,BranchAdmin)

admin.site.register(Department,DepartmentAdmin)

