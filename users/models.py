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

    category = models.CharField(default = "Criminal Case", max_length=50)

    def __str__(self):
        return self.category


class User(AbstractUser):
    
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Lawyer(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    email = models.EmailField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='')
    city = models.CharField(max_length=50,default='')
    lawyertype =models.CharField(max_length=50,default='')
    contact =models.CharField(max_length=15,default='')
    experience = models.FloatField(default=1,help_text='')
    pic= models.ImageField(upload_to="users/laywers",default="lawyer.png")
    

    def __str__(self):
        return f'{self.user}|{self.designation}|{self.gender}|{self.city}|{self.experience}|{self.lawyertype}'

class Client(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    email = models.EmailField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='')
    pic= models.ImageField(upload_to="users/client",default="client.png")
    contact =models.CharField(max_length=15,default='')

    def __str__(self):
        return self.user.username


class Cases_Fought(models.Model):

    status_value =(
        ('win','win'),
        ('lose', 'lose')
    )

    case = models.CharField(max_length=255, default='')
    summary = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(Lawyer, on_delete = models.CASCADE)
    status = models.CharField(max_length=255, choices = status_value, default=status_value[0][1])
    uploaded_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.case}|{self.category}|{self.user}|{self.status}'
  
class Contact(models.Model):

      full_name=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      subject=models.CharField(max_length=100)
      message=models.TextField(max_length=400)
      def __str__(self):
        return self.full_name

from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):
    lawyer = models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.score)