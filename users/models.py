from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver
from django.db.models.signals import post_save

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


class User(AbstractUser):
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Lawyer(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation = models.CharField(max_length=25,default='inter lawyer')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')
    city = models.CharField(max_length=25,default='lucknow')
    lawyertype =models.CharField(max_length=25,default='Criminal Lawyer')
    experience = models.FloatField(default=1,help_text='no of years as lawyer')

    def __str__(self):
        return self.user.username

class Client(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')

    def __str__(self):
        return self.user


class Cases_Fought(models.Model):

    status_value =(
        ('win','win'),
        ('lose', 'lose')
    )

    case = models.CharField(max_length=255, default='Case Name')
    summary = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(Lawyer, on_delete = models.CASCADE, default=100)
    status = models.CharField(max_length=255, choices = status_value, default=status_value[0][1])
    def __str__(self):
        return self.case
  
class Contact(models.Model):

      full_name=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      subject=models.CharField(max_length=100)
      message=models.TextField(max_length=400)
      def __str__(self):
        return self.full_name

