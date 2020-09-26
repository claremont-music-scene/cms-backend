from rest_framework import permissions
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_draft=False).order_by(
        "-is_featured", "order", "date_published"
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
