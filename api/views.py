from django.shortcuts import render
from rest_framework.views import apiviews
from student.models import Student
from rest_framework.response import Response


# Create your views here.

class StudentListView(apiviews):
    def get(self,request)
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)