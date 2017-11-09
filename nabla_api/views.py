#
# Copyright Cameron Curry (c) 2017
#

from django.http.response import HttpResponse


def nabla_api(request):
    return HttpResponse('hello from nabla_api')
