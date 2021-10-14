from . import views
from django.urls import path


app_name = "actions"

urlpatterns = [
    path('',views.home,name = 'home'),
]