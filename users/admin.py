from users.views import contact
from django.contrib import admin
from users.models import Category, Cases_Fought, Lawyer, Client, Contact,Rating

# Register your models here.
class AdminContact(admin.ModelAdmin):
  list_display=('full_name','email','subject','message')
admin.site.register(Category)
admin.site.register(Cases_Fought)
admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Contact, AdminContact)
admin.site.register(Rating)
