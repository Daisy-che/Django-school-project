from rest_framework import serializers
from .models import ClassPeriod

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'start_time', 'end_time', 'course', 'classroom', 'day_of_week']