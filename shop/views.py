from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import Category
from .serializer import CategorySerializer


class CategoryAPIView(APIView):
    def get(self, recuest):
        
        categories = Category.object.all()
        data = CategorySerializer(categories, many=True)
        return Response(data.data)



