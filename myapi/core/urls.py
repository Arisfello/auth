from django.urls import path, include
from myapi.core import views


urlpatterns =[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
   ]
