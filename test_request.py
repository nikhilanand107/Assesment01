import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedulo_project.settings")
import django
django.setup()

from django.test import Client

c = Client()
try:
    response = c.post('/add/', {'title': 'Test Item'})
    print(f"Response status: {response.status_code}")
    if response.status_code == 302:
        print(f"Redirect URL: {response.url}")
except Exception as e:
    print(f"Exception: {e}")
    import traceback
    traceback.print_exc()
