# Django Template Quote Parsing Error Fix

## Problem
The Django application was throwing a `TemplateSyntaxError` with the message:
```
Could not parse the remainder: '"1"' from '"1"
```

This error occurred when accessing `/enrollment/manage/` and was related to quote handling in Django template conditionals.

## Root Cause
The issue was caused by incorrect use of double quotes within Django template `{% if %}` conditionals. The problematic code was:

```django
{% if semester_filter == "1" %}selected{% endif %}
{% if semester_filter == "2" %}selected{% endif %}
```

Django's template parser has difficulty parsing double quotes within template tags when they conflict with the HTML attribute quotes, leading to parsing ambiguity.

## Files Affected
1. `main_app/templates/hod_template/manage_enrollment.html` (lines 51, 52)
2. `main_app/templates/staff_template/my_assessments.html` (lines 24, 25)

## Solution Applied
Replaced double quotes with single quotes in Django template conditionals:

### Before (Problematic):
```django
<option value="1" {% if semester_filter == "1" %}selected{% endif %}>1º Semestre</option>
<option value="2" {% if semester_filter == "2" %}selected{% endif %}>2º Semestre</option>
```

### After (Fixed):
```django
<option value="1" {% if semester_filter == '1' %}selected{% endif %}>1º Semestre</option>
<option value="2" {% if semester_filter == '2' %}selected{% endif %}>2º Semestre</option>
```

## Why This Works
Using single quotes inside Django template tags avoids conflicts with the double quotes used in HTML attributes. This eliminates parsing ambiguity and allows the Django template engine to correctly parse the conditional expressions.

## Alternative Solutions
Other valid approaches could include:
1. Using template variables instead of hardcoded strings
2. Moving the logic to the view layer
3. Using custom template tags for complex conditionals
4. Using the `yesno` template filter for simple boolean-like comparisons

## Verification
After applying the fixes, the Django system check passed without any template syntax errors:
```bash
python manage.py check
# System check identified no issues (0 silenced)
```

## Best Practices for Django Templates
To prevent similar issues in the future:

1. **Quote Consistency**: Always use single quotes inside Django template tags when the HTML attributes use double quotes:
   ```django
   ✅ Good: <option {% if value == 'target' %}selected{% endif %}>
   ❌ Bad:  <option {% if value == "target" %}selected{% endif %}>
   ```

2. **Escape Complex Quotes**: For complex string comparisons, consider using template variables:
   ```django
   # In view
   context['target_value'] = '1'
   
   # In template
   {% if semester_filter == target_value %}selected{% endif %}
   ```

3. **Use Built-in Filters**: Leverage Django's built-in template filters when possible:
   ```django
   {{ semester_filter|yesno:"selected," }}
   ```

4. **Template Debugging**: Enable template debugging during development to catch syntax errors early.

## Prevention Checklist
- [ ] Use consistent quote styles in templates
- [ ] Test template changes in development environment
- [ ] Run `python manage.py check` after template modifications
- [ ] Use Django's template debugging tools
- [ ] Consider moving complex logic to views instead of templates

## Impact
This fix resolves the template parsing errors that were preventing the enrollment management and staff assessment pages from loading correctly, ensuring proper functionality of the college management system.

## Related Issues
This fix is part of a series of template syntax corrections that also included:
- StringFormat filter corrections (see STRINGFORMAT_FIX_SUMMARY.md)
- General template syntax improvements

Both issues highlight the importance of proper Django template syntax and testing template changes thoroughly before deployment.