#
# Copyright Cameron Curry (c) 2017
#

from django.conf.urls import url

from .views import QTAccountView
from .views import QTAccessView
from .views import QTBalanceView
from .views import QTActivityView


urlpatterns = [
    url(r'qt-access$', QTAccessView.as_view()),
    url(r'qt-access/(?P<pk>[0-9a-f-]+)$', QTAccessView.as_view()),
    url(r'qt-account$', QTAccountView.as_view()),
    url(r'qt-balance/summary', QTBalanceView.summary),
    url(r'qt-balance/refresh', QTBalanceView.refresh),
    url(r'qt-activity$', QTActivityView.as_view()),
]
