from django.contrib import admin
from django.urls import path, include
from design import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name='homepage'), 
    path('api/', include('design.urls')),  
    path('api-auth/', include('rest_framework.urls')),
    path("", include("design.urls")),
]
