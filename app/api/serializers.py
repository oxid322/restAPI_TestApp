from rest_framework import serializers
from app.models import Add, Author


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = ['header', 'add_id', 'author', 'position', 'views']
