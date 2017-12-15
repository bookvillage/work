from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20);
    bpub_date = models.DateField();
    bread = models.IntegerField(default=0);
    bcommet = models.IntegerField(default=0);
    isDelete = models.BooleanField(default=False);
    bremack = models.CharField(max_length=100, null=True);
    class Meta:
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname= models.CharField(max_length=20);
    hgender = models.BooleanField(default=False);
    isDelete = models.BooleanField(default=False);
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('bookinfo')
    class Meta:
        db_table = 'heroinfo'

