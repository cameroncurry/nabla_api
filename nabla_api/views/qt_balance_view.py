#
# Copyright Cameron Curry (c) 2017
#

from django.db.models import Sum

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nabla_core.models import QTAccess
from nabla_core.models import QTBalance
from nabla_core.questrade_support import QTAccountService


class QTBalanceView:

    @staticmethod
    @api_view(['GET'])
    def summary(request):
        balance_aggregates = QTBalance.objects\
            .values('currency')\
            .filter(type='COMBINED')\
            .annotate(Sum('total_equity'))
        balances = {balance['currency']: balance['total_equity__sum'] for balance in balance_aggregates}
        return Response(balances, status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    def refresh(request):
        qt_access = QTAccess.objects.get(scope='ACC')
        qt_account_service = QTAccountService(qt_access)
        qt_account_service.sync_balances()
        return QTBalanceView.summary(request)
