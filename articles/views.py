from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsProvider
from .models import Article
from .serializers import ArticlesSerializer


class ArticlesViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated, IsProvider, IsOwner]
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(user=user)
    