# nabla_api

INSTALLED_APPS = [
    '...',
    'nabla_api',
    '...'
]


urlpatterns = [
    ... ,
    url(r'^api/', include('nabla_api.urls')),
    ...
]