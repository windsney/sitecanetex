from django.urls import path

import cd.views
from .views import Home

from django.contrib.auth import views as auth_view

app_name='cd'

urlpatterns = [

    
    
    path('cd_cadastradas/', Home.as_view(),name='cd_cadastradas'),
    

]