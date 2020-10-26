from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # 指定序列化的model 和fields
        model = Blog
        fields= '__all__'

