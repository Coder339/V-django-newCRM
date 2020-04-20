from rest_framework import serializers
from .models import *

class SLASerializer(serializers.ModelSerializer):
      class  Meta:
          model        =           SLA
          fields       =           '__all__'

# class EscalationSerializer(serializers.ModelSerializer):
#     class Meta:
#           model         =           Escalation
#           fields        =           '__all__'
