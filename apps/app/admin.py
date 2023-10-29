from django.contrib.admin import *
from .models import *

#addmin 123

#user
@register(ModelsUser)
class UserAdmin(ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

#post
@register(ModelsPost)
class PostAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
