#
# Copyright Cameron Curry (c) 2017
#

from rest_framework.generics import ListAPIView

from nabla_core.models import QTAccess
from nabla_core.models import QTAccount
from nabla_core.models import QTActivity

from .serializers.questrade import QTAccountSerializer
from .serializers.questrade import QTAccessSerializer
from .serializers.questrade import QTActivitySerializer


class QTAccessView(ListAPIView):

    queryset = QTAccess.objects.all()
    serializer_class = QTAccessSerializer


class QTAccountView(ListAPIView):

    queryset = QTAccount.objects.all()
    serializer_class = QTAccountSerializer


class QTActivityView(ListAPIView):

    queryset = QTActivity.objects.all()
    serializer_class = QTActivitySerializer

