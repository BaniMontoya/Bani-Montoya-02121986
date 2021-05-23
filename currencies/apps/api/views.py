from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from apps.api import serializers as api_serializers
from apps.api import models as api_models
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from django.db.utils import IntegrityError


def query_currency_format_by_country_and_currency_code(request):
    data = request.GET
    try:
        country = data['country']
    except:
        country = None
    if country:
        queryset = api_models.CurencyFormat.objects.filter(
            country=country)
        if queryset.exists():
            return JsonResponse({"results": list(queryset.values())})
        else:
            return JsonResponse({'Message': 'Currency or country not found!'}, status=404)
    else:
        return JsonResponse({'Message': 'Currency or country not found!'}, status=404)


class CurrencyFormatViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = api_models.CurencyFormat.objects.all()
    serializer_class = api_serializers.CurencyFormatSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return self.queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        if "country" in data:
            country = data['country']
        else:
            return Response({"Message": "country is mandatory!"}, status=403)
        if "currency_code" in data:
            currency_code = data['currency_code']
        else:
            return Response({"Message": "currency_code is mandatory!"}, status=403)
        if "currency_nomenclature" in data:
            currency_nomenclature = data['currency_nomenclature']
        else:
            return Response({"Message": "currency_nomenclature is mandatory!"}, status=403)
        if "currency_symbol_pos" in data:
            currency_symbol_pos = data['currency_symbol_pos']
        else:
            return Response({"Message": "currency_symbol_pos is mandatory!"}, status=403)
        if "cents_enabled" in data:
            cents_enabled = data['cents_enabled']
        else:
            return Response({"Message": "cents_enabled is mandatory!"}, status=403)
        if "display_format" in data:
            display_format = data['display_format']
        else:
            return Response({"Message": "display_format is mandatory!"}, status=403)
        try:
            create = api_models.CurencyFormat.objects.create(
                country=country, currency_code=currency_code, currency_nomenclature=currency_nomenclature,
                currency_symbol_pos=currency_symbol_pos, cents_enabled=str(cents_enabled).capitalize(), display_format=display_format
            )
        except IntegrityError:
            create = None
            return Response({"Message": "Country and Currency should by unique!"}, status=400)

        return Response({"Message": "Created!"}, status=200)

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=200)
