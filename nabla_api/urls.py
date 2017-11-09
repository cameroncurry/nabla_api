#
# Copyright Cameron Curry (c) 2017
#

from django.conf.urls import url
from .views import QTAccountView


urlpatterns = [
    url(r'qt_accounts$', QTAccountView.as_view())
]
