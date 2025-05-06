from django.urls import path
from . import views

urlpatterns = [
    path('portofolio/', views.porto, name='porto'),
]
