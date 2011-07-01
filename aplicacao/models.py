from django.db import models

CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
)

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(verbose_name="nome da pessoa", max_length=30)
    idade = models.IntegerField(verbose_name="idade da pessoa")
    sexo = models.CharField(choices=CHOICES, verbose_name="sexo da pessoa", max_length=1)

    def __unicode__(self):
	    return unicode(self.nome) 

