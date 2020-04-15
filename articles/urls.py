from rest_framework.routers import DefaultRouter
from .views import ArticlesViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]