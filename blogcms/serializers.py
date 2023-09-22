from rest_framework import serializers
from .models import CustomUser, BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = BlogPost
        fields = ['id','title', 'content', 'created_on', 'author']
        
