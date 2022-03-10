# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*c+&oha-06n92ax4-qil*hm_4ttik+b#1y%ybw(1mtx&e^nq*5'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Shamgar1',

    }
}