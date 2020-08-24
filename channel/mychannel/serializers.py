from rest_framework import serializers
from .models import SetUpChannel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetUpChannel
        fields = '__all__'
