from django.db import models

# Create your models here.

class Device(models.Model):
    
    # defining datavariables
    
    type = models.CharField(max_length=50, blank= False)
    price = models.IntegerField()
     
    choices = (('Avialable','Ready to Purchase'),('Sold','Item Sold'),('Restockin','Item Restocking in few days'))
     
    status = models.CharField(max_length=10, choices=choices, default='sold')
    issue = models.CharField(max_length=50,default='No isssue')
    
    
    class Meta:
         abstract = True
    
    def __str__(self):
       return 'Type : {0} price : {1}'.format(self.type,self.price)
    
         
         
class Laptop(Device):
        pass
    
class Desktop(Device):
        pass
    
class Mobile(Device):
        pass


