from django.contrib import admin
from users.models import Category, Cases_Fought, Lawyer, Client

# Register your models here.
admin.site.register(Category)
admin.site.register(Cases_Fought)
admin.site.register(Lawyer)
admin.site.register(Client)