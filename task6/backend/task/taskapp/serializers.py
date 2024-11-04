from rest_framework import serializers
from . import models

#serialization
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = '__all__'