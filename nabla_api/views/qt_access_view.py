#
# Copyright Cameron Curry (c) 2017
#

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from nabla_core.models import QTAccess
from nabla_core.questrade_support import QTAccessService

from ..serializers.questrade import QTAccessSerializer


class QTAccessView(GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):
    """
    Methods:
        GET: Retrieve QTAccess list
        PUT: Update QTAccess
        POST: Create QTAccess
        DELETE: Delete QTAccess
    """

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

    def post(self, request, *args, **kwargs):
        if 'scope' not in request.data or 'refresh_token' not in request.data:
            response_data = {
                'scope': ['This Field is Required'],
                'refresh_token': ['This Field is Required']
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        if not QTAccess.is_valid_scope(request.data['scope']):
            response_data = {
                'scope': ['Not accepted, use ACC/MKT/ODR']
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        qt_access = QTAccess.objects.create(scope=request.data['scope'],
                                            refresh_token=request.data['refresh_token'])
        return Response(QTAccessSerializer(qt_access).data, status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
