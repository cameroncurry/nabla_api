#
# Copyright Cameron Curry (c) 2017
#

from rest_framework import generics
from nabla_core.models import QTAccount
from .serializers import QTAccountSerializer


class QTAccountView(generics.ListAPIView):

    queryset = QTAccount.objects.all()
    serializer_class = QTAccountSerializer

