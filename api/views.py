from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from rest_framework.response import Response
# from .serializers import StudentSerializer

class StudentListView(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)