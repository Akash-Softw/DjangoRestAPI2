from django.db import models
 
class customerDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    
 
    def __str__(self) :
        return self.name
