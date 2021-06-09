from django.contrib import admin

from .models import images,Comment,Like,Catagory


# Register your models here.


admin.site.register(images)
admin.site.register(Comment)
admin.site.register(Catagory)
admin.site.register(Like)


