from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post , category , coment

class ProductAdmin(SummernoteModelAdmin) :
    list_display = ['title','category','draft']
    list_filter = ['draft','tags','category'] 
    search_fields = ['title','tags']
    summernote_fields = ['content',]



admin.site.register(Post,ProductAdmin)
admin.site.register(category)
admin.site.register(coment)

