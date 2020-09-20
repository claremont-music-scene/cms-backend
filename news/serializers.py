from rest_framework import serializers
from .models import Post

#TODO don't show draft posts
#TODO author
#https://www.django-rest-framework.org/api-guide/serializers/#relational-fields
#https://www.django-rest-framework.org/api-guide/relations/
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "teaser",
            "body",
            "image",
            #"author",
            "date_modified",
            "date_published"
        ]
