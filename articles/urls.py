from rest_framework.routers import DefaultRouter
from .views import ArticlesViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]