from django.urls import path
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [

path('other/', views.other, name='othe'),
path('relative/', views.relative, name='relative'),
]
