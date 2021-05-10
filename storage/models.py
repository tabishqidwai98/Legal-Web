from django.db import models

# Create your models here.

class AiModel(models.Model):
    """Model definition for AiModel."""

    model_category = (
        (1,"image"),
        (2,"text"),
        (3,"nlp"),
        (4,"video"),
        (5,"others"),
    )

    name = models.CharField(max_length=255,default='model')
    summary = models.TextField()
    model_file = models.FileField(upload_to='ai_models',null=True)
    category = models.IntegerField(choices=model_category,default=model_category[0][1])
    model_image = models.ImageField(upload_to='ai_models/images',null=True)
       

    def __str__(self):
        return self.name
