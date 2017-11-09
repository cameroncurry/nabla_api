#
# Copyright Cameron Curry (c) 2017
#

from rest_framework import serializers
from nabla_core.models import QTAccount


class QTAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = QTAccount
        fields = ('type', 'number', 'status', 'primary', 'client_account_type')
