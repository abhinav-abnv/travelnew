from django.urls import path, include
from django.urls import path

from midoapp import views


urlpatterns=[
    path('',views.demo,name='demo'),
    # path('',views.nemo,name='nemo')
]

