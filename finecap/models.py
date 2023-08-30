from django.db import models

# Create your models here.
class Stand(models.Model):
    localizacao = models.CharField(max_length = 100)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao
    
class Categoria(models.Model):
    nome = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cnpj = models.CharField(max_length = 18)
    nome_empresa = models.CharField(max_length = 100)
    categoria_empresa = models.OneToOneField(Categoria, on_delete = models.SET_NULL, null = True)
    quitado = models.BooleanField()
    img = models.ImageField(upload_to = 'imagens', verbose_name = 'imagem')
    stand = models.OneToOneField(Stand, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.cnpj