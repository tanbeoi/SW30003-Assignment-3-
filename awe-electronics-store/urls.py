# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This will make the normal urls accessable to the project
    path('awe-electronics-store/', include('app.urls')),
]