from rest_framework.serializers import ModelSerializer
from apps.api.models import CurencyFormat


class CurencyFormatSerializer(ModelSerializer):

    class Meta:
        model = CurencyFormat
        fields = '__all__'

