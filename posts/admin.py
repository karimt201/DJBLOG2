from django.contrib import admin

from .models import Post , category , coment

class ProductAdmin(admin.ModelAdmin) :
    list_display = ['title','category','draft']
    list_filter = ['draft','tags','category'] 
    search_fields = ['title','tags']



admin.site.register(Post,ProductAdmin)
admin.site.register(category)
admin.site.register(coment)
