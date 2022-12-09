from django.contrib import admin
from .models import Listado


# Registro en el panel de admin

class ListadoAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "created")

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'fructosa',
                'lactosa',
                'sorbitol',
                'manitol',
                'gos',
                'fructano',
                'gr',
                'comment',
                'thumbnail',
                
                'fructosaAmarillo',
                'lactosaAmarillo',
                'sorbitolAmarillo',
                'manitolAmarillo',
                'gosAmarillo',
                'fructanoAmarillo',
                'grAmarillo',
                'commentAmarillo',

                'fructosaRojo',
                'lactosaRojo',
                'sorbitolRojo',
                'manitolRojo',
                'gosRojo',
                'fructanoRojo',
                'grRojo',
                'commentRojo',

                )
        }),
        
    )
    readonly_fields = ("created", "updated")
    

admin.site.register(Listado, ListadoAdmin)
