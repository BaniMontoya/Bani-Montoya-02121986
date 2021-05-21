from rest_framework.routers import SimpleRouter
from apps.api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path


router = SimpleRouter()

router.register('api/v1/currency',
                api_views.CurrencyFormatViewSet, 'currency_get')

urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),
]