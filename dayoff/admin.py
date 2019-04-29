from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

from dayoff.models import DayOff

admin.site.register(Permission)

class DayOffAdmin(admin.ModelAdmin):
    list_display = ['create_by', 'reason', 'date_start', 'date_end', 'approve_status']

    list_filter = ['create_by', 'date_start', 'date_end', 'type', 'approve_status']
    search_fields = ['create_by', 'date_start', 'date_end', 'type', 'approve_status']

    fieldsets = [  # แบ่งกลุ่มหน้า UI
        ("ข้อมูลการลา", {'fields': ['create_by', 'reason', 'date_start', 'date_end']}),
        ("การอนุมัติ", {'fields': ['approve_status']})
    ]
    readonly_fields = ['reason','create_by', 'date_start', 'date_end', 'type']
admin.site.register(DayOff, DayOffAdmin)