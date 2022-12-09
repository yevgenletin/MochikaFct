
from django.db import models
from django.contrib.auth.models import User

#Modelo categoria
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

#Modelo de la receta
class Post(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        tiempo = models.CharField(max_length=10)
        calorias = models.IntegerField()
        proteinas = models.IntegerField()
        grasas = models.IntegerField()
        azucares = models.IntegerField()
        sal = models.IntegerField()
        contenido = models.TextField(max_length=4000)
        thumbnail = models.ImageField(upload_to='media/thumbnail/%Y/%m/%d/', null=True, blank=True)
        ingredientes = models.TextField(max_length=4000)
        likes = models.ManyToManyField(User, related_name='blog_post')
        

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
#Modelo comentario
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.name, self.name)


