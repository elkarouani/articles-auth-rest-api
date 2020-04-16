from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
