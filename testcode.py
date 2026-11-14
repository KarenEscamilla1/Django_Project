 # no SQL approach to import data and filter data
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")  # getting learning_log folder
import django
django.setup()

from MainApp.models import *

topics = Topic.objects.all()   # query set object     

for topic in topics:    
    print(topic.id, topic)   # .id is an attribute of an object; you can do topic bc each id is the attribute

# you are printing a specific topic based by finding the id
t = Topic.objects.get(id=1)
print (t.text)
print (t.date_added)


# we are interacting with db.sqlite which we can't open up in visual studio code
entries = Entry.objects.filter(topic = t) #filters entries based on the attribute topic 
for entry in entries:
    print (entry)
