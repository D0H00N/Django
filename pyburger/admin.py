from django.contrib import admin
from burgers.models import Burgers

# Register your models here.

@admin.register(Burgers)
class BurgerAdmin(admin.ModelAdmin):
    pass