from django.contrib import admin

# Register your models here.
from courses.models import Course, Subject, Reviews

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Subject, SubjectAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "published_date")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Course, CourseAdmin)


admin.site.register(Reviews)