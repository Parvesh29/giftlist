diff --git a/.superpowers/sdd/wishlist-implementation/progress.md b/.superpowers/sdd/wishlist-implementation/progress.md
new file mode 100644
index 0000000..f89024f
--- /dev/null
+++ b/.superpowers/sdd/wishlist-implementation/progress.md
@@ -0,0 +1,11 @@
+# SDD ledger ù plan: docs\superpowers\plans\2026-09-04-wishlist-implementation.md
+
+| Tasks | Interface | Finding | Ruling |
+|---|---|---|---|
+| 1 & 2 | WishlistRequest | Matches | N/A |
+| 2 & 3 | send_wishlist_email | Matches | N/A |
+| 3 & 4 | /submit-wishlist | Matches | N/A |
+| 1 | Self | Matches | N/A |
+| 2 | Self | Matches | N/A |
+| 3 | Self | Matches | N/A |
+| 4 | Self | Matches | N/A |
diff --git a/.superpowers/sdd/wishlist-implementation/task-1-brief.md b/.superpowers/sdd/wishlist-implementation/task-1-brief.md
new file mode 100644
index 0000000..00324a6
--- /dev/null
+++ b/.superpowers/sdd/wishlist-implementation/task-1-brief.md
@@ -0,0 +1,33 @@
+: Backend Scaffolding and Schemas
+
+**Files:**
+- Create: `backend/requirements.txt`
+- Create: `backend/schemas.py`
+
+**Interfaces:**
+- Produces: `WishlistRequest` Pydantic model in `backend/schemas.py`.
+
+- [ ] **Step 1: Create requirements.txt**
+```text
+fastapi
+uvicorn
+pydantic
+python-dotenv
+```
+- [ ] **Step 2: Define WishlistRequest schema**
+```python
+from pydantic import BaseModel, HttpUrl
+
+class WishlistRequest(BaseModel):
+    name: str
+    item_names: str
+    priority: str
+    item_link: HttpUrl
+```
+- [ ] **Step 3: Commit**
+```bash
+git add backend/requirements.txt backend/schemas.py
+git commit -m "feat: backend scaffolding and schemas"
+```
+
+
diff --git a/docs/superpowers/plans/2026-09-04-wishlist-implementation.md b/docs/superpowers/plans/2026-09-04-wishlist-implementation.md
new file mode 100644
index 0000000..415c696
--- /dev/null
+++ b/docs/superpowers/plans/2026-09-04-wishlist-implementation.md
@@ -0,0 +1,199 @@
+# Wish List Implementation Plan
+
+> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
+
+**Goal:** Build a React frontend and FastAPI backend that sends a wish list form to parveshkumara001@gmail.com.
+
+**Architecture:** React SPA communicates with a FastAPI backend via POST. FastAPI uses `smtplib` to send an HTML email to the recipient.
+
+**Tech Stack:** React.js, FastAPI, Python `smtplib`, Pydantic.
+
+**Spec:** docs/superpowers/specs/2026-09-04-wishlist-design.md
+
+## Global Constraints
+- Recipient Email: parveshkumara001@gmail.com
+- Backend: Python (FastAPI)
+- Frontend: React.js
+- Form Fields: Name, Item Names, Priority, Item link
+
+---
+
+### Task 1: Backend Scaffolding and Schemas
+
+**Files:**
+- Create: `backend/requirements.txt`
+- Create: `backend/schemas.py`
+
+**Interfaces:**
+- Produces: `WishlistRequest` Pydantic model in `backend/schemas.py`.
+
+- [ ] **Step 1: Create requirements.txt**
+```text
+fastapi
+uvicorn
+pydantic
+python-dotenv
+```
+- [ ] **Step 2: Define WishlistRequest schema**
+```python
+from pydantic import BaseModel, HttpUrl
+
+class WishlistRequest(BaseModel):
+    name: str
+    item_names: str
+    priority: str
+    item_link: HttpUrl
+```
+- [ ] **Step 3: Commit**
+```bash
+git add backend/requirements.txt backend/schemas.py
+git commit -m "feat: backend scaffolding and schemas"
+```
+
+### Task 2: Email Service Implementation
+
+**Files:**
+- Create: `backend/email_service.py`
+- Create: `backend/.env`
+
+**Interfaces:**
+- Produces: `send_wishlist_email(data: WishlistRequest) -> bool`
+
+- [ ] **Step 1: Create .env template**
+```text
+SMTP_SERVER=smtp.gmail.com
+SMTP_PORT=587
+SMTP_USER=your_email@gmail.com
+SMTP_PASSWORD=your_app_password
+```
+- [ ] **Step 2: Implement send_wishlist_email**
+```python
+import smtplib
+from email.mime.text import MIMEText
+from email.mime.multipart import MIMEMultipart
+import os
+from dotenv import load_dotenv
+from schemas import WishlistRequest
+
+load_dotenv()
+
+def send_wishlist_email(data: WishlistRequest):
+    msg = MIMEMultipart()
+    msg['From'] = os.getenv('SMTP_USER')
+    msg['To'] = 'parveshkumara001@gmail.com'
+    msg['Subject'] = f"New Wishlist from {data.name}"
+    
+    body = f"""
+    <h2>New Wishlist Submission</h2>
+    <p><b>Name:</b> {data.name}</p>
+    <p><b>Items:</b> {data.item_names}</p>
+    <p><b>Priority:</b> {data.priority}</p>
+    <p><b>Link:</b> <a href='{data.item_link}'>{data.item_link}</a></p>
+    """
+    msg.attach(MIMEText(body, 'html'))
+    
+    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
+        server.starttls()
+        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
+        server.send_message(msg)
+    return True
+```
+- [ ] **Step 3: Commit**
+```bash
+git add backend/email_service.py backend/.env
+git commit -m "feat: implement email service"
+```
+
+### Task 3: FastAPI Endpoint Implementation
+
+**Files:**
+- Create: `backend/main.py`
+
+**Interfaces:**
+- Consumes: `WishlistRequest` from `schemas.py`, `send_wishlist_email` from `email_service.py`.
+- Produces: POST `/submit-wishlist` endpoint.
+
+- [ ] **Step 1: Implement main.py**
+```python
+from fastapi import FastAPI, HTTPException
+from fastapi.middleware.cors import CORSMiddleware
+from schemas import WishlistRequest
+from email_service import send_wishlist_email
+
+app = FastAPI()
+
+app.add_middleware(
+    CORSMiddleware,
+    allow_origins=["*"],
+    allow_methods=["*"],
+    allow_headers=["*"],
+)
+
+@app.post("/submit-wishlist")
+async def submit_wishlist(request: WishlistRequest):
+    try:
+        send_wishlist_email(request)
+        return {"message": "Wishlist sent successfully!"}
+    except Exception as e:
+        raise HTTPException(status_code=500, detail=str(e))
+```
+- [ ] **Step 2: Commit**
+```bash
+git add backend/main.py
+git commit -m "feat: implement fastapi endpoint"
+```
+
+### Task 4: Frontend Form Implementation
+
+**Files:**
+- Create: `frontend/package.json`
+- Create: `frontend/src/App.js`
+- Create: `frontend/src/components/WishlistForm.js`
+
+**Interfaces:**
+- Consumes: POST `/submit-wishlist` from backend.
+
+- [ ] **Step 1: Create package.json** (minimal react setup)
+- [ ] **Step 2: Implement WishlistForm component**
+```jsx
+import React, { useState } from 'react';
+
+export default function WishlistForm() {
+    const [formData, setFormData] = useState({ name: '', item_names: '', priority: 'Medium', item_link: '' });
+    const [status, setStatus] = useState('');
+
+    const handleSubmit = async (e) => {
+        e.preventDefault();
+        try {
+            const res = await fetch('http://localhost:8000/submit-wishlist', {
+                method: 'POST',
+                headers: { 'Content-Type': 'application/json' },
+                body: JSON.stringify(formData),
+            });
+            if (res.ok) setStatus('Wishlist sent successfully!');
+            else setStatus('Error sending wishlist.');
+        } catch (err) { setStatus('Network error.'); }
+    };
+
+    return (
+        <form onSubmit={handleSubmit}>
+            <input placeholder="Name" onChange={e => setFormData({...formData, name: e.target.value})} required />
+            <textarea placeholder="Item Names" onChange={e => setFormData({...formData, item_names: e.target.value})} required />
+            <select onChange={e => setFormData({...formData, priority: e.target.value})}>
+                <option value="High">High</option>
+                <option value="Medium">Medium</option>
+                <option value="Low">Low</option>
+            </select>
+            <input placeholder="Item Link" type="url" onChange={e => setFormData({...formData, item_link: e.target.value})} required />
+            <button type="submit">Submit</button>
+            <p>{status}</p>
+        </form>
+    );
+}
+```
+- [ ] **Step 3: Implement App.js to render WishlistForm**
+- [ ] **Step 4: Commit**
+```bash
+git add frontend/
+git commit -m "feat: implement react frontend form"
+```
diff --git a/docs/superpowers/specs/2026-09-04-wishlist-design.md b/docs/superpowers/specs/2026-09-04-wishlist-design.md
new file mode 100644
index 0000000..f817466
--- /dev/null
+++ b/docs/superpowers/specs/2026-09-04-wishlist-design.md
@@ -0,0 +1,47 @@
+# Wish List Project Design Spec
+Date: 2026-09-04
+Status: Draft
+
+## Overview
+A full-stack application allowing users to submit a wish list via a web form, which is then emailed to a specific recipient.
+
+## Requirements
+- Frontend: React.js
+- Backend: Python (FastAPI)
+- Email Recipient: parveshkumara001@gmail.com
+- Form Fields:
+    - Name
+    - Item Names
+    - Priority
+    - Item Link
+
+## Architecture
+### Frontend (React.js)
+- A single-page application (SPA).
+- Form components with client-side validation.
+- State management via `useState`.
+- Communication with backend via REST API (POST `/submit-wishlist`).
+
+### Backend (FastAPI)
+- REST API providing a single endpoint for form submission.
+- Pydantic models for request body validation.
+- CORS middleware for frontend connectivity.
+- Integration with SMTP for email delivery.
+
+## Data Flow
+1. **Client**: User fills form $\rightarrow$ POST request with JSON payload.
+2. **Server**: FastAPI validates request $\rightarrow$ Triggers email sending logic.
+3. **Email Service**: SMTP server sends an HTML formatted email to `parveshkumara001@gmail.com`.
+4. **Client**: Receives success/error response and displays notification.
+
+## Technical Specifications
+- **SMTP Config**: Loaded from `.env` file (SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD).
+- **Email Format**: HTML template for structured presentation of the wish list.
+- **Validation**: 
+    - Frontend: Required field checks.
+    - Backend: Data type and format validation (e.g., valid URL for Item Link).
+
+## Testing Plan
+- **Frontend**: Manual test of form submission and validation errors.
+- **Backend**: Unit tests for Pydantic models and API endpoint.
+- **Integration**: End-to-end test from form submission to email receipt.
