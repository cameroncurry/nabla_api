#
# Copyright Cameron Curry (c) 2017
#

from rest_framework.serializers import ModelSerializer

from nabla_core.models import QTAccess
from nabla_core.models import QTAccount
from nabla_core.models import QTActivity


class QTAccessSerializer(ModelSerializer):
    class Meta:
        model = QTAccess
        fields = ('id', 'modified', 'scope', 'access_token', 'refresh_token', 'api_server')


class QTAccountSerializer(ModelSerializer):
    class Meta:
        model = QTAccount
        fields = ('id', 'type', 'number', 'status', 'primary', 'client_account_type')


class QTActivitySerializer(ModelSerializer):
    class Meta:
        model = QTActivity
        fields = ('id', 'transaction_date', 'action', 'symbol', 'description', 'currency',
                  'quantity', 'price', 'gross_amount', 'commission', 'net_amount', 'type')
