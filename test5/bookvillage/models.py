from django.db import models

# Create your models here.
class AeraInfo(models.Model):
    aname = models.CharField(max_length=100)
    aparent = models.ForeignKey('self',null=True,blank=True)

    class Meta:
        db_table = 'AeraInfo'