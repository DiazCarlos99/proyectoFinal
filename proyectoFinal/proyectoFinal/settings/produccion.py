from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['CarlosRDiaz.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CarlosRDiaz$default',
        'USER': 'CarlosRDiaz',
        'PASSWORD': 'informatorio6',
        'HOST': 'CarlosRDiaz.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True  # O False si no es necesario TLS
EMAIL_HOST_USER = '**********@gmail.com'
EMAIL_HOST_PASSWORD = '********'



if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')