from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views

#Auto Routing configurations
router = DefaultRouter()

#Registration of the router 
router.register(r"studentsapi", views.StudentViewset)

urlpatterns = [
    path('', views.index ,name='index'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('api/', include(router.urls)),
    path('register/', views.register, name='register'),
]
