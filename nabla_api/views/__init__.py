#
# Copyright Cameron Curry (c) 2017
#

from rest_framework.generics import ListAPIView
from nabla_core.models import QTAccount
from nabla_core.models import QTActivity

from ..serializers.questrade import QTAccountSerializer
from ..serializers.questrade import QTActivitySerializer

from .qt_access_view import QTAccessView


class QTAccountView(ListAPIView):

    queryset = QTAccount.objects.all()
    serializer_class = QTAccountSerializer


class QTActivityView(ListAPIView):

    queryset = QTActivity.objects.all()
    serializer_class = QTActivitySerializer
