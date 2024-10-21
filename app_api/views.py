from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework import status
from django.contrib.auth import get_user_model

from .serializers import UserAccountSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment


User = get_user_model()


class UserAccountViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        post_id = request.GET.get('post_id')

        if post_id:
            self.queryset = Comment.objects.filter(post__id=post_id)

        else:
            self.queryset = Comment.objects.all()

        serializer = self.serializer_class(self.queryset, many=True).data
        return Response(data=serializer)
