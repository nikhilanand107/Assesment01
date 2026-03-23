import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedulo_project.settings')
django.setup()
from django.test import Client
from django.contrib.auth.models import User
u = User.objects.filter(username='test_user123').first()
if not u:
    u = User.objects.create_user('test_user123', 'test@example.com', 'testpwd123')
c = Client(SERVER_NAME='localhost')
login_ok = c.login(username='test_user123', password='testpwd123')
print('Login OK:', login_ok)
if login_ok:
    r = c.get('/add/')
    print('Add view status after login:', r.status_code)
