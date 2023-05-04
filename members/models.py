from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.IntegerField(null=True)
    joined_data = models.DateField(null=True)
    
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):

        return f"{self.first_name} {self.last_name} {self.phone}"