from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Article


class ArticlesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'