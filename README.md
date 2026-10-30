**py -m venv .venv**

**source .venv/Scripts/activate**

 **py -m pip install django djangorestframework**

**django-admin startproject config .**


**Next go to the config/settings.py**

**And add 'rest_framework' inside the INSTALLED_APP list.**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]
```
