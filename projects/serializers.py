from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('category', 'id', 'title', 'slug',
                  'excerpt', 'content', 'status', 'tags', 'featured')