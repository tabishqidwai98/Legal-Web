from django.db import models

# Create your models here.

class Category(models.Model):

    Case_category = (
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

    Name = models.CharField(max_length=255, default="Your name here")
    Email = models.EmailField(max_length=255,default='example@host.com')
    Category = models.CharField(choices=Case_category,default = Case_category[0][1], max_length=50)

    def __str__(self):
        return self.Category

class lawyer_Profile(models.Model):

    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    Name = models.CharField(max_length=255, default = "your name")
    Email = models.CharField(max_length=255,default="example@host.com")
    Phone_No = models.CharField(max_length=13 ,default=911234567890)
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    Gender = models.CharField(max_length=50, choices=gender, default=gender[0][1])
    Profile_Photo = models.ImageField(upload_to="profile",null=True)
    General_Fee = models.IntegerField(default=1000)


    def __str__(self):
        return self.Name

class Cases_Fought(models.Model):

    Cases = models.ForeignKey(lawyer_Profile, on_delete=models.CASCADE, default=1)
    Summary = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    Email = models.CharField(max_length=255, default="example@host.com")
    def __str__(self):
        return self.Case


class User_Profile(models.Model):
    User_name = models.CharField(max_length = 255, default = 'your name')
    email = models.EmailField(max_length = 255, default= "example@host.com")
    contact_no = models.IntegerField(default=911234567890)
    address = models.TextField()
    image = models.ImageField()
    bio = models.TextField() 
