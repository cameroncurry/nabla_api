# nabla_api

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