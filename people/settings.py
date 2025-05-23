import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-o$t7%e8%&u2japa*el@kf1*b2)r!#ly3ba9p2lije@zpyh2x4'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'easy_thumbnails',
    'main',
    'ckeditor',
    'ckeditor_uploader',
    'about',
    'categories',
    'peoples',
    'frends',
    'news',
    'policy',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'people.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'people.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CKEDITOR_UPLOAD_PATH = 'media/'

CKEDITOR_CONFIGS = {
       'default': {
           'toolbar': 'full',
           'height': 500,
           'width': '100%',
           'removePlugins': 'stylesheetparser',
           'extraPlugins': ','.join(['youtube']),
       },
    }

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MANAGERS = (("admin", "ochkarik1983@mail.ru"),)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'interesnijsim49293@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

THUMBNAIL_ALIASES = {
    "":{
        "hor_160": {"size":(160,120)},
        "hor_240": {"size":(240,180)},
        "hor_320": {"size":(320,240)},
        "hor_480": {"size":(480,360)},
        "hor_640": {"size":(640,480)},
        "hor_960": {"size":(960,720)},
        "hor_1280": {"size":(1280,960)},
        "hor_1440": {"size":(1440,1080)},
        "hor_1600": {"size":(1600,1200)},
        "hor_1920": {"size":(1920,1350)},
        "hor_2240": {"size":(2240,1350)},
        "hor_2560": {"size":(2560,1200)},
        "hor_2880": {"size":(2880,1350)},

        "vert_160": {"size":(160,213)},
        "vert_240": {"size":(240,320)},
        "vert_320": {"size":(320,427)},
        "vert_480": {"size":(480,640)},
        "vert_640": {"size":(640,853)},
        "vert_960": {"size":(960,1280)},
        "vert_1280": {"size":(1280,1600)},

        "og": {"size":(500,500)},
    },
}
