---
title: Persist activities and registrations (replace in-memory storage)
labels:
  - enhancement
---

## Summary

Replace the current in-memory activity store with persistent storage so activity signups survive server restarts.

## Requirements

- Store activity and registration data in a JSON file, SQLite database, or other lightweight persistent storage.
- Load persisted data on startup.
- Save changes when signups, unregisters, or activity edits occur.

## Notes

This is critical for a real app experience; currently the backend resets all data when the server restarts.
