from django.contrib import admin
from .models import Categoria, Post, Comment


# Registrar en el panel de administración
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'categorias',
                'tiempo',
                'calorias',
                'proteinas',
                'grasas',
                'azucares',
                'sal',

                'contenido', 
                'ingredientes',
                'autor',
                "likes",
                'thumbnail'
                )
        }),
        
    )
    readonly_fields = ("created", "updated")
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


