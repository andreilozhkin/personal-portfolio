from django.contrib import admin
from .models import Job, Education, Project, Tag

# Register your models here.
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Tag)

class TagInline(admin.TabularInline):
    model = Tag.projects.through
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        TagInline,
    )

admin.site.register(Project, ProjectAdmin)
