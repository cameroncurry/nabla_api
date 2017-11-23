#
# Copyright Cameron Curry (c) 2017
#

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from nabla_core.models import QTAccess
from nabla_core.models import QTAccount
from nabla_core.models import QTActivity
from nabla_core.questrade_support import QTAccessService

from .serializers.questrade import QTAccountSerializer
from .serializers.questrade import QTAccessSerializer
from .serializers.questrade import QTActivitySerializer


class QTAccessView(GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):

    queryset = QTAccess.objects.all()
    serializer_class = QTAccessSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        qt_access = get_object_or_404(QTAccess, *args, **kwargs)
        qt_access = QTAccessService.refresh_and_save_qt_access(qt_access)
        return Response(QTAccessSerializer(qt_access).data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QTAccountView(ListAPIView):

    queryset = QTAccount.objects.all()
    serializer_class = QTAccountSerializer


class QTActivityView(ListAPIView):

    queryset = QTActivity.objects.all()
    serializer_class = QTActivitySerializer

