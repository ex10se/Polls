from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Polls API",
        default_version='v1',
        description='''
              ### API для системы опросов пользователей
              [**Swagger**](/swagger/)  
              [**ReDoc**](/redoc/)
              ''',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('polls.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]

urlpatterns += [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
