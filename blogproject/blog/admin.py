from django.contrib import admin
from blog.models import Post
# Register your models here.

#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    
    list_filter = ('status','author','created')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)
