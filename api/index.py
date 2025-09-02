import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_mgmt.settings")  # <-- update if your project module name differs
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()  # Vercel looks for 'app'
