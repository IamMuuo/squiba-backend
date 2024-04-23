from django.core.wsgi import get_wsgi_application
import sys
import os

sys.path.append(os.getcwd())
# change 'application_name' to
os.environ["DJANGO_SETTINGS_MODULE"] = "squiba.settings"
# the name of the Django project


application = get_wsgi_application()
