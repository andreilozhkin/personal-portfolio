from django.contrib import admin
from .models import Job, Education, Project, Tag, Profile


# Register your models here.

class TagInline(admin.TabularInline):
    model = Tag.projects.through
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (TagInline,)


admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
