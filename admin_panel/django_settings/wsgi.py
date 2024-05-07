import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'admin_panel.django_settings.settings')

application = get_wsgi_application()
