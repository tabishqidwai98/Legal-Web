from users.models import User_Profile
from django.db import models

# Create your models here.

class Cases(models.Model):
    """Model definition for Cases."""

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

    Case_Name = models.CharField(max_length=255,default='Case')
    Category = models.CharField(choices=Case_category,default=Case_category[0][1], max_length=50)
    Description = models.TextField()
    Case_image = models.ImageField(upload_to='Case_dir/images',null=True)
    Contact_No = models.IntegerField(default=911234567890,unique=True)
    Name = models.ForeignKey(User_Profile,on_delete = models.CASCADE)
    email= models.EmailField(max_length=255,default='example@host.com')
       

    def __str__(self):
        return self.Case_Name

