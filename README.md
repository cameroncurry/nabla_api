# nabla_api 

[![Build Status](https://travis-ci.org/cameroncurry/nabla_api.svg?branch=master)](https://travis-ci.org/cameroncurry/nabla_api) [![Known Vulnerabilities](https://snyk.io/test/github/cameroncurry/nabla_api/badge.svg)](https://snyk.io/test/github/cameroncurry/nabla_api)

INSTALLED_APPS = [
    '...',
    'nabla_api.apps.NablaApiConfig',
    'rest_framework',
    '...'
]


urlpatterns = [
    ... ,
    url(r'^api/', include('nabla_api.urls')),
    ...
]
