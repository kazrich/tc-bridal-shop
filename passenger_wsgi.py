import sys, os

sys.path.insert(0, os.path.join(os.getcwd(), 'website'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
os.environ.setdefault("PYTHONPATH", "/home/tcbrwcwy/tcbridals.com/website")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
