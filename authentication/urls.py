from django.conf.urls import url, include
from .views import GitHubLogin


urlpatterns = [
    url(r'^rest-auth/github/$', GitHubLogin.as_view(), name='github_login')
]
