from rest_framework import serializer
from student.models import Student

class StudentSerializer(serializers,modelSerializer):
    class Meta:
        model =Student
        fields ="__all__"