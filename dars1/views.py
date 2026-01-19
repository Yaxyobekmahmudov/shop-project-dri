from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer

# Create your views here.
    

class SchollApiView(APIView):
    
    def get(self, recuest):
        schools = School.objects.all()
        ser = SchoolSerializer(schools, many=True)
        return Response(ser.data)

class StudentApiVIew(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)
