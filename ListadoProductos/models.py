
from django.db import models
from multiselectfield import MultiSelectField


class Listado(models.Model):

    ELEMENT = (('verde', 'verde',),
              ('amarillo', 'amarillo'),
              ('rojo', 'rojo'),)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    fructosa =MultiSelectField(max_length= 50, choices = ELEMENT)
    lactosa = MultiSelectField(max_length= 50, choices = ELEMENT)
    sorbitol = MultiSelectField(max_length= 50, choices = ELEMENT)
    manitol = MultiSelectField(max_length= 50, choices = ELEMENT)
    gos = MultiSelectField(max_length= 50, choices = ELEMENT)
    fructano = MultiSelectField(max_length= 50, choices = ELEMENT)
    gr = models.CharField(max_length= 50)
    comment = models.TextField(max_length= 5000)
    thumbnail = models.ImageField(upload_to='media/thumbnail/%Y/%m/%d/', null=True, blank=True)
  
    fructosaAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    lactosaAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    sorbitolAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    manitolAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    gosAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    fructanoAmarillo = MultiSelectField(max_length= 50, choices = ELEMENT)
    grAmarillo = models.CharField(max_length= 50)
    commentAmarillo = models.TextField(max_length= 5000)
    
    fructosaRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    lactosaRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    sorbitolRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    manitolRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    gosRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    fructanoRojo = MultiSelectField(max_length= 50, choices = ELEMENT)
    grRojo = models.CharField(max_length= 50)
    commentRojo = models.TextField(max_length= 5000)
    
    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                       '300x300',
                                       upscale=False,
                                       crop=False,
                                       quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'

        
    def __str__(self):
        return str(self.id) + " " + str(self.name)




