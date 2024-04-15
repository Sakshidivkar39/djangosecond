from django.urls import path
from .import views

urlpatterns = [
    path('',views.firstmsg),
    path('second',views.secondmsg),
    path('third',views.thirdmsg),
    path('fourth',views.fourthmsg),
]