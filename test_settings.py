SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'rest_framework',
    'nabla_core',
    'nabla_api',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
ROOT_URLCONF = 'nabla_api.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
