from django.urls import path
from .views import SchollApiView, StudentApiVIew

urlpatterns = [
    path('school/', SchollApiView.as_view()),
    path('student/', SchollApiView.as_View()),
]