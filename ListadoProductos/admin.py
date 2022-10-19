from django.contrib import admin
from .models import Listado


# Register your models here.

class ListadoAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "created")

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Listado, ListadoAdmin)
