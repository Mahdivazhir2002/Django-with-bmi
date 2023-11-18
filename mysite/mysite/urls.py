
from django.contrib import admin
from django.urls import path,include
from bmi.views import index
urlpatterns = [
    
    
    path('',include('bmi.urls')),
    path('admin/', admin.site.urls),
]
