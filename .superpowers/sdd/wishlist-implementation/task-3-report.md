# Task 3 Report: API Endpoint Implementation

## Summary
Implemented the FastAPI endpoint `/submit-wishlist` in `backend/main.py`.

## Changes
- Created `backend/main.py`.
- Configured CORS middleware to allow all origins, methods, and headers.
- Implemented `POST /submit-wishlist` which integrates `WishlistRequest` schema and `send_wishlist_email` service.
- Added error handling to return a 500 HTTP exception on failure.

## Verification
- File created and committed.
- Implementation matches the brief exactly.
