
from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

class Todo(models.Model):     
    priority_choice=[
          ('high', 'High'),
          ('medium', 'Medium'),
          ('low', 'Low'),
    ]
    title=models.CharField(max_length=240)       #title field
    details=models.TextField(blank=True)         #details field
    image = models.ImageField(upload_to='images', blank=True) #image field
    date_created=models.DateTimeField(auto_now_add=True)  
    completed=models.BooleanField(default=False) #date_created field
    user=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    priority=models.CharField(max_length=20,default='low',choices=priority_choice)
    due_date = models.DateField(blank=True, null=True, default=datetime.now)
    approaching_date = models.CharField(default='None',max_length=40,null=True)

 
    def __str__(self) :     #display objects with name as title
        return self.title      
    



    