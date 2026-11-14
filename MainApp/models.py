from django.db import models
from django.contrib.auth.models import User #creating a foreign key conenction to the topic model 

# Create your models here.
class Topic(models.Model):   #topic adn date added are attributes
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    def __str__(self):
        return  self.text   #makes it so that topic_obect 1 = is called the text added by the user 
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # here topic is added as foreign key from the primary key in the topic table
    #field CASACADE -> cascades effect throughout database to maintain referential integrity
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):   #customizes what is displayed in the website 
        return f"{self.text[:50]}..."  #slicing it to teh first 50 characters

#using user model to 