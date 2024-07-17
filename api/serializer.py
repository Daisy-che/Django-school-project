# from rest_framework import serializer
# from student.models import Student

# class StudentSerializer(serializers,modelSerializer):
#     class Meta:
#         model =Student
#         fields ="__all__"from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'grade']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model =ClassRoom
        fields = "__all__"
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'













