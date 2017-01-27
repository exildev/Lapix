#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for Lapix project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(5)oh7r)ojyiu!r8$gq0=9eirnlhis5^0-s0bg9*5dud8ua=s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'exileui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hojadevida.apps.HojadevidaConfig',
    'supra',
    'configuracion',
    'curriculo',
    'horario',
    ]

EXILE_UI = {
    'site_title': 'Lapix',
    'site_header': 'Lapix',
    'index_title': 'Software Educativo',
    'media': {
        'logo': {
            'dashboard': '',
            'page': '',
            'login': ''
        },
        'icons': {
            'hojadevida': {
                'icon': 'school',
                'groups': [
                    'Usuarios',
                    'Configuración'
                ],
                'models': {
                    'Profesor': {'icon': 'person', 'group': 'Usuarios'},
                    'Estudiante': {'icon': 'person', 'group': 'Usuarios'},
                    'Acudiente': {'icon': 'people', 'group': 'Usuarios'},
                    'AsignacionSede': {'icon': 'settings', 'group': 'Configuración'},
                    'GradoEntrante': {'icon': 'settings', 'group': 'Configuración'}
                }
            },
            'curriculo': {
                'icon': 'start_rate',
                'groups': [
                    'Curriculo'
                ],
                'models': {
                    'Area': {'icon': 'public', 'group': 'Curriculo'},
                    'Materia': {'icon': 'widgets', 'group': 'Curriculo'}
                }
            },
            'configuracion': {
                'icon': 'settings',
                'groups': [
                    'Sede'
                ],
                'models': {
                    'Sede': {'icon': 'home', 'group': 'Sede'},
                }
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'hojadevida',
        'models': [
            'Profesor',
            'Estudiante',
            'Acudiente',
            'AsignacionSede',
            'GradoEntrante'
        ]
    },
    {
        'name': 'curriculo',
        'models': [
            'Area',
            'Materia'
        ]
    },
    {
        'name': 'configuracion',
        'models': [
            'Sede'
        ]
    }
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

ROOT_URLCONF = 'Lapix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Lapix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lapix2',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '104.236.33.228',
        'POST': '5432'
    },
    'default2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/Lapix/server/Lapix/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/Lapix/server/Lapix/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
