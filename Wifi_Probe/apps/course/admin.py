from django.contrib import admin
from apps.course import models

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('rno', 'mmac')  # list
    fieldsets = (
        ['Main', {
            'fields': ('rno', 'mmac'),
        }],
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('cname', 'rid', 'sid')  # list
    fieldsets = (
        ['Main', {
            'fields': ('cname', 'rid', 'sid'),
        }],
    )


admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Courseselect)
