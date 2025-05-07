from PouriaSite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iw(5@!be6hh9m@%zvnvh)4*lrb57_)cs5+d-)zk!evfh^^duy('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

# sites framework settings
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'  # Directory to collect static files
MEDIA_ROOT = BASE_DIR / 'media'    # Directory to collect media files

STATICFILES_DIRS = [
    BASE_DIR / 'statics',  # Additional static files directories
]

CSRF_COOKIE_SECURE = True  # CSRF cookie should only be sent over HTTPS