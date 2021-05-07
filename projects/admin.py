from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Project)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'tags', 'featured')
    prepopulated_fields = {'slug': ('title',),}

admin.site.register(models.Category)