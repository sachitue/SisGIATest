# Session Management Guide

This document explains how to manage academic sessions in the College Management System.

## Overview

In the College Management System, an academic session represents an academic year (e.g., 2023-2024). Only one session can be active at any given time, which is controlled by the `is_current` field in the Session model.

## How Session Management Works

### Session Model

The Session model has the following fields:
- `start_year`: Start date of the academic year
- `end_year`: End date of the academic year
- `is_current`: Boolean field indicating if this is the current active session

### Key Features

1. **Single Active Session**: The system ensures only one session can be active at a time through the model's `save()` method:

```python
def save(self, *args, **kwargs):
    if self.is_current:
        Session.objects.exclude(id=self.id).update(is_current=False)
    super().save(*args, **kwargs)
```

When a session is set as current (`is_current=True`), all other sessions automatically become inactive.

2. **Session Management Views**:
   - `manage_session`: Lists all sessions with their status
   - `add_session`: Creates a new session
   - `edit_session`: Edits an existing session (including setting it as current)
   - `toggle_session_status`: Quick toggle for session status
   - `delete_session`: Removes a session

## Managing Sessions

### Creating a New Session

1. Navigate to "Ano Lectivo" → "Adicionar" in the sidebar
2. Fill in the start and end dates
3. Optionally check "Set as Current Session" to make it active
4. Click "Create Academic Session"

### Editing a Session

1. Navigate to "Ano Lectivo" → "Gerir" in the sidebar
2. Find the session you want to edit and click "Edit"
3. Modify the dates if needed
4. To change the active status:
   - Check "Set as Current Session" to make it active (this will deactivate any currently active session)
   - Uncheck "Set as Current Session" to make it inactive
5. Click "Update Academic Session"

### Quick Toggle Session Status

1. Navigate to "Ano Lectivo" → "Gerir" in the sidebar
2. Find the session you want to toggle
3. Click the "Activate" or "Deactivate" button depending on its current status
4. Confirm the action in the dialog

### Deleting a Session

1. Navigate to "Ano Lectivo" → "Gerir" in the sidebar
2. Find the session you want to delete and click "Delete"
3. Confirm the deletion

Note: You cannot delete a session that has associated records (enrollments, assessments, etc.)

## Best Practices

1. **Always have an active session**: Most academic operations require an active session. Ensure there's always one active.

2. **Plan session transitions**: When activating a new session, ensure all necessary data migration or preparation is complete.

3. **Communicate changes**: Inform relevant stakeholders when session status changes, as it affects enrollment and other academic processes.

4. **Avoid gaps**: Try to maintain continuous session coverage to avoid issues with academic operations.

## Troubleshooting

### Issue: Cannot set a session as active

**Solution**: 
1. Check if another session is already active
2. Ensure the session dates are valid
3. Verify you have the necessary permissions

### Issue: No active session warning

**Solution**:
1. Go to "Ano Lectivo" → "Gerir"
2. Find a suitable session and activate it using either the "Edit" or "Activate" options

### Issue: Session not appearing in lists

**Solution**:
1. Check if the session was created successfully
2. Verify the date range is correct
3. Refresh the page or clear browser cache

## Technical Notes

### Template Filters

Two custom template filters have been added for session management:

1. `get_current_session_count`: Returns the number of active sessions
2. `get_inactive_session_count`: Returns the number of inactive sessions

### JavaScript Enhancements

The session management interface includes:
- DataTables for sorting and filtering sessions
- Real-time search functionality
- Status-based filtering
- Bulk action support (planned)

## API Endpoints

- `GET /session/manage/` - List all sessions
- `POST /session/add/` - Create new session
- `POST /session/edit/<id>/` - Update session
- `POST /session/toggle/<id>/` - Toggle session status
- `POST /session/delete/<id>/` - Delete session

## Future Improvements

1. Add bulk session operations
2. Implement session cloning functionality
3. Add session statistics and reports
4. Improve date validation and conflict detection