from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(pizzas)

admin.site.register(drink)
admin.site.register(burger)
admin.site.register(pasta)