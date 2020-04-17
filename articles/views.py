from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsProvider
from .models import Article
from .serializers import ArticlesSerializer


class ArticlesViewSet(DestroyModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsProvider, IsOwner]
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user_id'] = request.user.id
        serializer.save()
        return Response({'success': "Article created successfully"})


    
