# -*- coding: utf-8 -*-
from django.db import models

class Questao(models.Model):
    lugar = models.BooleanField(default=True, verbose_name='IFPEL')
    texto = models.TextField()
    imagem = models.ImageField(upload_to='ocupa')
    outro = models.CharField(max_length=200, verbose_name='Outro Lugar')

    class Meta:
        verbose_name_plural = 'Questões'
        verbose_name = 'Questão'

    def __unicode__(self):
        return self.outro