from django.contrib.auth.models import User
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"