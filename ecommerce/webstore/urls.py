from django.urls import path
from . import views
urlpatterns=[
path("home/",views.index,name ="webstore-home"),path("details/",views.details,name ="webstore-details"),path("contact/",views.contact,name ="webstore-contact")]