# How to Fix TemplateSyntaxError for 'form_filters'

## Problem
You're encountering the following error:
```
TemplateSyntaxError at /session/manage/
'form_filters' is not a registered tag library.
```

## Root Cause
The issue occurs because Django cannot find the custom template filter library. This happens when:
1. The template filter is not in the correct location
2. The app containing the template filter is not properly registered
3. The template filter file has syntax errors

## Solution

### 1. Verify Template Filter Location
Django expects template filters to be in a `templatetags` directory within a registered app. 

The correct structure should be:
```
main_app/
  templatetags/
    __init__.py
    form_filters.py
```

### 2. Check App Registration
Ensure the app containing the templatetags directory is registered in `settings.py`:

In `college_management_system/settings.py`, verify that `main_app` is listed in `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ... other apps ...
    'main_app.apps.MainAppConfig',
    # ... other apps ...
]
```

### 3. Verify Template Filter File
Check that `main_app/templatetags/form_filters.py` contains:
```python
from django import template

register = template.Library()

@register.filter
def get_current_session_count(sessions):
    """Returns the count of current (active) sessions"""
    return sessions.filter(is_current=True).count()

@register.filter
def get_inactive_session_count(sessions):
    """Returns the count of inactive sessions"""
    return sessions.filter(is_current=False).count()
```

### 4. Check Template Usage
In your template (`main_app/templates/hod_template/manage_session.html`), ensure you're loading the filter correctly:
```html
{% load static %}
{% load form_filters %}
```

Not:
```html
{% load form_filters from main_app %}
```

### 5. Restart Development Server
After making these changes, restart your Django development server:
```bash
python manage.py runserver
```

## Additional Notes

1. The `templatetags` directory must contain an `__init__.py` file (can be empty) to be recognized as a Python package.

2. Template filters are automatically discovered by Django when the app is registered and the development server is restarted.

3. Make sure there are no syntax errors in your template filter file, as this will prevent Django from loading the filters.

4. If you're still having issues, try clearing Django's cache:
   ```bash
   python manage.py shell
   ```
   Then in the shell:
   ```python
   from django.template import engines
   engines.__dict__.clear()
   ```

## Verification
To verify that your template filters are working, you can create a simple test:

1. Create a test file `test_filters.py`:
```python
import os
import sys
import django

sys.path.append('D:/CollegeManagement-Django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_management_system.settings')
django.setup()

from main_app.models import Session
from main_app.templatetags.form_filters import get_current_session_count, get_inactive_session_count

def test_filters():
    sessions = Session.objects.all()
    current_count = get_current_session_count(sessions)
    inactive_count = get_inactive_session_count(sessions)
    print(f"Current sessions: {current_count}")
    print(f"Inactive sessions: {inactive_count}")

if __name__ == "__main__":
    test_filters()
```

2. Run the test:
```bash
python test_filters.py
```

If this runs without errors and shows the correct counts, your template filters are working properly.