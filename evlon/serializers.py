from rest_framework import serializers
from .models import Post

class EvlonPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"
        