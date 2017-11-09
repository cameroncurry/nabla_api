#
# Copyright Cameron Curry (c) 2017
#

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'nabla_api$', views.nabla_api)
]
