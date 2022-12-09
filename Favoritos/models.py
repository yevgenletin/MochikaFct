from django.db import models
from django.contrib.auth.models import User

# Modelo Favoritos
class Favoritos(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_producto = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=40, null=True, blank=True, default='')
    valor = models.IntegerField( default=1)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.id_user) + ' -> ' +  str(self.id_producto) + str(self.name) + '->' +str(self.comment)
    
    class Meta:
        ordering = ['created']
