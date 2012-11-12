import os
import sys

sys.path.append("/home/nathan/renegade/mysite")
sys.path.append("/home/nathan/renegade")

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
