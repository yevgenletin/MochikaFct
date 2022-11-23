
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        contenido = models.TextField(max_length=4000)
        thumbnail = models.ImageField(upload_to='media/thumbnail/%Y/%m/%d/', null=True, blank=True)
        ingredientes = models.TextField(max_length=4000)

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

        autor = models.ForeignKey(User,on_delete=models.CASCADE)
        categorias = models.ManyToManyField(Categoria)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name = 'post'
            verbose_name_plural = 'posts'

        def __str__(self):
            return self.name



