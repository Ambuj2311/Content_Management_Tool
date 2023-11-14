from django.contrib import admin
from .models import content
# Register your models here.
@admin.register(content)
class RegisterTable(admin.ModelAdmin):
    list_display=[
        'name','Image','video','Article'
    ]