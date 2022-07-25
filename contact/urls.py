from django.urls import path
from . import views

app_name='contact' #utk url di home & contact
urlpatterns=[
    path('',views.index,name='index')
]
