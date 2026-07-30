---
title: Add login / role selection (user/admin)
labels:
  - enhancement
---

## Summary

Add a login page and role selection so the app can distinguish between student and admin flows.

## Requirements

- Create a login page with username/password and a role selector (user/admin).
- Redirect to a student dashboard or admin dashboard based on role.
- Preserve existing public activity browsing for unauthenticated users if possible.
- Keep authentication simple; a static file or in-memory credentials are acceptable for this exercise.

## Notes

This will support the admin mode feature from the ActivityHub comparison and help separate user/admin behavior.
