# Wish List Project Design Spec
Date: 2026-09-04
Status: Draft

## Overview
A full-stack application allowing users to submit a wish list via a web form, which is then emailed to a specific recipient.

## Requirements
- Frontend: React.js
- Backend: Python (FastAPI)
- Email Recipient: parveshkumara001@gmail.com
- Form Fields:
    - Name
    - Item Names
    - Priority
    - Item Link

## Architecture
### Frontend (React.js)
- A single-page application (SPA).
- Form components with client-side validation.
- State management via `useState`.
- Communication with backend via REST API (POST `/submit-wishlist`).

### Backend (FastAPI)
- REST API providing a single endpoint for form submission.
- Pydantic models for request body validation.
- CORS middleware for frontend connectivity.
- Integration with SMTP for email delivery.

## Data Flow
1. **Client**: User fills form $\rightarrow$ POST request with JSON payload.
2. **Server**: FastAPI validates request $\rightarrow$ Triggers email sending logic.
3. **Email Service**: SMTP server sends an HTML formatted email to `parveshkumara001@gmail.com`.
4. **Client**: Receives success/error response and displays notification.

## Technical Specifications
- **SMTP Config**: Loaded from `.env` file (SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD).
- **Email Format**: HTML template for structured presentation of the wish list.
- **Validation**: 
    - Frontend: Required field checks.
    - Backend: Data type and format validation (e.g., valid URL for Item Link).

## Testing Plan
- **Frontend**: Manual test of form submission and validation errors.
- **Backend**: Unit tests for Pydantic models and API endpoint.
- **Integration**: End-to-end test from form submission to email receipt.
