from django.db import models

# Create your models here.
class Sentiments(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    compound = models.DecimalField(max_digits=19, decimal_places=10)
    neg = models.DecimalField(max_digits=19, decimal_places=10)
    neu = models.DecimalField(max_digits=19, decimal_places=10)
    pos = models.DecimalField(max_digits=19, decimal_places=10)

#class Meta:
#       ordering = ('created',)