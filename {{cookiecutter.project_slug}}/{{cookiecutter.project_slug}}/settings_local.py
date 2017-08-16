from .settings import *     # noqa

DEBUG = True

# Order mater!
INSTALLED_APPS = ['debug_toolbar', 'livereload'] + INSTALLED_APPS

MIDDLEWARE_CLASSES = [
    'livereload.middleware.LiveReloadScript',   # Order mater!
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE_CLASSES

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',  # Avoid double jQuery load
    'PATCH_SETTINGS': False
}
