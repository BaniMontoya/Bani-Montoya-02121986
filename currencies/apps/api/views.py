from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from apps.api import serializers as api_serializers
from apps.api import models as api_models
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class CurrencyFormatViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        country = self.request.query_params.get('country', None)
        try:
            obj = api_models.CurencyFormat.objects.get(
                country=country)
            serializer = api_serializers.CurencyFormatSerializer(obj)
            return Response(serializer.data, status=200)
        except:
            return JsonResponse({'Message': 'Currency or country not found!'}, status=404)

    def create(self, request):
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
        create = api_models.CurencyFormat.objects.create(
            country=country, currency_code=currency_code, currency_nomenclature=currency_nomenclature,
            currency_symbol_pos=currency_symbol_pos, cents_enabled=cents_enabled, display_format=display_format
        )
        return Response({"Message": "Created!"}, status=200)


