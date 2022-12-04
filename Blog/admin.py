from django.contrib import admin
from .models import Categoria, Post, Comment


# Register your models here.

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
                "valor",
                'thumbnail'
                )
        }),
        
    )
    readonly_fields = ("created", "updated")
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


