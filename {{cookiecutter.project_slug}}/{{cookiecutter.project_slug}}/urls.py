""" {{cookiecutter.project_slug}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from apps.index.views import frontpage

urlpatterns = [
    url(r'^$', frontpage, name='index'),
    {% if cookiecutter.use_django_rest_framework == 'y' -%}
    url(r'^api/', include('apps.api.urls', namespace='api')),
    {% endif -%}
    {% if cookiecutter.use_authentication == 'y' -%}
    url(
        r'^login/',
        auth_views.login,
        {'template_name': 'admin/login.html'},
        name='login'
    ),
    url(r'^logout/', auth_views.login, name='logout'),
    {% endif -%}
    url(r'^admin/', admin.site.urls),
]

# if settings.LETS_ENCRYPT:
#     challenge = settings.LETS_ENCRYPT.split('.')
#     urlpatterns += [
#         url(r'^.well-known/acme-challenge/{}'.format(challenge[0]),
#             letsencrypt_challenge,
#             name='letsencrypt'),
#     ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
