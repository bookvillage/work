

# Register your models here.




# from django.contrib import admin
# from .models import BookInfo,HeroInfo
#
# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)

from django.contrib import admin
from .models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname','hgender','hcontent']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)