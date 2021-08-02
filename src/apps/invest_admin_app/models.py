from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    date_created = models.DateTimeField(verbose_name='Date of creation')

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        db_table = 'stocks'


class Crypto(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(verbose_name='Date of creation')

    class Meta:
        verbose_name = 'Cryptocurrency'
        db_table = 'crypto'
