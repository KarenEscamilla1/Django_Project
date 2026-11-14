from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path ('', include('django.contrib.auth.urls')), # do not have to create view for the user but you do have to create the template
    path ('register/', views.register, name='register')
]