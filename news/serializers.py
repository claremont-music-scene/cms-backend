from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]

#TODO don't show draft posts

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "teaser",
            "body",
            "image",
            "author",
            "date_modified",
            "date_published"
        ]
