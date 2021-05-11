from django.contrib import admin
from users.models import Category, Cases_Fought, lawyer_Profile, User_Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Cases_Fought)
admin.site.register(lawyer_Profile)
admin.site.register(User_Profile)