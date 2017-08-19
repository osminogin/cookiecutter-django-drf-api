from .settings import *     # noqa

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '::1', 'localhost']

# Order mater!
INSTALLED_APPS = ['debug_toolbar', 'livereload'] + INSTALLED_APPS

MIDDLEWARE = [
    'livereload.middleware.LiveReloadScript',   # Order mater!
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',  # Avoid double jQuery load
    'PATCH_SETTINGS': False
}
