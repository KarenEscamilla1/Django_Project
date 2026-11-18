from django.shortcuts import render, redirect
from MainApp.models import *
from .forms import *
from django.contrib.auth.decorators import login_required  # decorator: prewritten function within django framework a (function within a function)
from django.http import Http404 #produces an error if user tries to access a page using the url path

#get request
# Create your views here.
def index(request):    # there are two types of requests data from database -> get request or to database -> post request 
    return render(request, 'mainapp/index.html')   # view points to template MainApp/index/html 
def topics(request):
    topics = Topic.objects.filter(owner=request.user)       #fetches all topics from database; list of objects
    context = {'topics':topics}    # uses a dictionary the key is the name of what would be used in a template, value is what will be used in the view
    return render(request, 'mainapp/topics.html', context)
#### double check 

# from test code vew 
#gest request
@login_required #call decorator and requires login
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = Entry.objects.filter(topic= topic).order_by('-date_added') #adds entry objects so it is filtered by the topic selected and ordered and sorted by descending order
    context = {'topic':topic, 'entries':entries}

    return render(request, 'mainapp/topic.html', context)


#post request uses redirect and TopicForm
@login_required
def new_topic (request):
    if request.method != 'POST':   #therefore it is a get request (gives empty form)
        form = TopicForm()
    
    else:
        form = TopicForm(data=request.POST)  # if it is a post request then (gives filled out form)
        if form.is_valid():    #internal validation
            new_topic = form.save(commit=False) #in final exam
            new_topic.owner = request.user
            new_topic.save()
            form.save()   #saves it to the database
            return redirect('MainApp:topics') #automatically goes to the Topics page since a new topic has been added 
        
    context = {'form':form}
    return render(request, 'mainapp/new_topic.html', context)
    
@login_required
def new_entry (request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  #commit the object but don't save it to the database yet #we want to create a new object but it is not yet saved to the database bc it won't have a topic
            new_entry.topic = topic #gets topic from topic_id
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic.id)
        
    context = {'form':form, 'topic':topic}
    return render(request, 'mainapp/new_entry.html', context)

@login_required
def edit_entry (request, entryid):  # hast to be consistent to the path in urls.py
    entry = Entry.objects.get(entryid)
    topic = Entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance= entry)
    else: 
        form = EntryForm(instance=entry, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'mainapp/edit_entry.html', context)

        
        

