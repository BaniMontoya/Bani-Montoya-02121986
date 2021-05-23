from rest_framework.routers import DefaultRouter
from apps.api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
router = DefaultRouter()

router.register(r'api/v1/currency',
                api_views.CurrencyFormatViewSet, 'currency_format')
schema_view = get_schema_view(
    openapi.Info(
        title="Currency format API",
        default_version='v1',
        description="Hiring Test",
        terms_of_service="",
        contact=openapi.Contact(email="banimontoya@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),
    path('api/v1/query_currency_format_by_country_and_currency_code/', api_views.query_currency_format_by_country_and_currency_code,
         name='query_currency_format_by_country_and_currency_code'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
