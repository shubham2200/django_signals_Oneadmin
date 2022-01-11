from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class authenticate_history(models.Model):
    recordstype_choice = [
        ('reg' , 'register'),
        ('li','login'),
        ('lo','logout'),
        

    ]
    user_name = models.ForeignKey(User , on_delete = models.CASCADE)
    recordstype = models.CharField(max_length= 5 ,choices= recordstype_choice)
    date_time = models.DateTimeField(auto_created= True ,  null= True ,  blank= True)
    
    
    
    def __str__(self ):
        return str(self.user_name) + str(self.date_time) + str(self.recordstype)