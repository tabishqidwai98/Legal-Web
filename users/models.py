from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    case_category = (
        ('Criminal Case',"Criminal Case"),
        ('Civil Case',"Civil Case"),
        ('Marriage Dissolution',"Marriage Dissolution"),
        ('Paternity and Child Custody',"Paternity and Child Custody"),
        ('Protection Orders Aganist Domestic Violence',"Protection Orders Aganist Domestic Violence"),
        ('Name Changes',"Name Changes"),
        ('Guardianship',"Guardianship"),
        ('Termination of Parental Rights and Adoptions',"Termination of Parental Rights and Adoptions"),
        ('Juvenile Matters',"Juvenile Matters"),
        ('Emancipation and Approval of Underage Marriages',"Emancipation and Approval of Underage Marriages"),
    )

    category = models.CharField(choices=case_category,default = case_category[0][1], max_length=50)

    def __str__(self):
        return self.category

class Cases_Fought(models.Model):

    status_value =(
        ('win','win'),
        ('lose', 'lose')
    )

    case = models.CharField(max_length=255, default='Case Name')
    summary = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=100)
    status = models.CharField(max_length=255, choices = status_value, default=status_value[0][1])
    def __str__(self):
        return self.case


class Profile(models.Model):

    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user_kind = (
        ('user','user'),
        ('lawyer', 'lawyer')
    )

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    contact_no = models.IntegerField(default=911234567890)
    address = models.TextField()
    image = models.ImageField()
    gender = models.CharField(max_length=255,choices=gender,default=gender[0][1])
    bio = models.TextField()
    user_type = models.CharField(max_length=255, choices = user_kind, default=user_kind[0][1])

    def __str__(self):
        return self.user

