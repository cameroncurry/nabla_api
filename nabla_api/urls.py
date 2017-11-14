#
# Copyright Cameron Curry (c) 2017
#

from django.conf.urls import url

from .views import QTAccountView
from .views import QTAccessView
from .views import QTActivityView


urlpatterns = [
    url(r'qt_access$', QTAccessView.as_view()),
    url(r'qt_account$', QTAccountView.as_view()),
    url(r'qt_activity$', QTActivityView.as_view()),
]
