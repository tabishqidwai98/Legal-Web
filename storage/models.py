from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import Client

# Create your models here.

class Cases(models.Model):
    # """Model definition for Cases."""

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

    caseName = models.CharField(max_length=255,default='')
    category = models.CharField(choices=Case_category, max_length=50)
    description = models.TextField()
    case_image = models.ImageField(upload_to='Case_dir/images',null=True)
    contact_No = models.CharField(unique=True, max_length=10)
    user = models.ForeignKey(Client,on_delete = models.CASCADE)
    requested_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caseName


class ReviewCases(models.Model):
    title = models.CharField(max_length=225,default="review title")
    detail = models.TextField()
    reviewer = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
    case = models.ForeignKey(Cases,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=3,validators=[MinValueValidator(1),MaxValueValidator(5)])
    uploaded_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} for {self.case}'