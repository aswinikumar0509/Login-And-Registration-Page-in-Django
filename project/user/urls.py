from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from user.views import *
 
urlpatterns = [
         path('', views.index, name ='index'),
]