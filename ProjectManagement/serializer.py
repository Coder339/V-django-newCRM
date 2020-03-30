from rest_framework import serializers
from .models import *

class Business_opportunitySerializer(serializers.ModelSerializer):
      class  Meta:
          model        =           Business_opportunity
          fields       =           '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
          model         =           Project
          fields        =           '__all__'
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#           model         =           Task
#           fields        =           '__all__'
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
          model         =           TodoList
          fields        =           '__all__'
