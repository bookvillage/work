from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date','bread','bcommet','isDelete','bremack']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname','hgender','hcontent','isDelete','hbook']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)