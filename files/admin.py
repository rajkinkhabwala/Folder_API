from django.contrib import admin

from files.models import Upload

# Register your models here.
@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    pass