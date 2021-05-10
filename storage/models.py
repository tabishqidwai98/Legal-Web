from django.db import models

# Create your models here.

class Cases(models.Model):
    """Model definition for Cases."""

    Case_category = (
        (1,"Criminal Case"),
        (2,"Civil Case"),
        (3,"Marriage Dissolution"),
        (4,"Paternity and Child Custody"),
        (5,"Protection Orders Aganist Domestic Violence"),
        (6,"Name Changes"),
        (7,"Guardianship"),
        (8,"Termination of Parental Rights and Adoptions"),
        (9,"Juvenile Matters"),
        (10,"Emancipation and Approval of Underage Marriages.")
    )

    Case_Name = models.CharField(max_length=255,default='Case')
    category = models.IntegerField(choices=Case_category,default=Case_category[0][1])
    description = models.TextField()
    Case_image = models.ImageField(upload_to='ai_models/images',null=True)
    Contact_No = models.IntegerField(default=911234567890, unique=False)
       

    def __str__(self):
        return self.name
