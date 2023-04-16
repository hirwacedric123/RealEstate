from django.urls import path
from realapp import views
from .views import send_message

urlpatterns = [
   path('',views.index, name='index'),
   path('send-message/index.html', send_message, name='send_message'),
   
]