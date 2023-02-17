"""
WSGI config for mobile_tracking_location project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/Mobile_Tracker_location/mobile_tracking_location')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_tracking_location.settings')

application = get_wsgi_application()
