from rest_framework.routers import DefaultRouter
from apps.api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()

router.register(r'api/v1/currency',
                api_views.CurrencyFormatViewSet, 'currency_format')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),
    path('api/v1/query_currency_format_by_country_and_currency_code/', api_views.query_currency_format_by_country_and_currency_code,
         name='query_currency_format_by_country_and_currency_code'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
