import datetime

from django.db import models
from django.utils import timezone


class Item(models.Model):
    item_text = models.CharField(max_length=100)
    descricao_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('data de publicação')
    
    def __str__(self):
        return self.item_text

    def foi_adicionado_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Escolha(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    escolha_text = models.CharField(max_length=200)
    boolean = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha_text

