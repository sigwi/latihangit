from . import views
from django.urls import path

app_name='blog' #utk url di home & contact
urlpatterns=[
    path('create/',views.create,name='create'),
    path('',views.index,name='index'),
]
