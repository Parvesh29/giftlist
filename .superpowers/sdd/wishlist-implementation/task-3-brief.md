: FastAPI Endpoint Implementation

**Files:**
- Create: `backend/main.py`

**Interfaces:**
- Consumes: `WishlistRequest` from `schemas.py`, `send_wishlist_email` from `email_service.py`.
- Produces: POST `/submit-wishlist` endpoint.

- [ ] **Step 1: Implement main.py**
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import WishlistRequest
from email_service import send_wishlist_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit-wishlist")
async def submit_wishlist(request: WishlistRequest):
    try:
        send_wishlist_email(request)
        return {"message": "Wishlist sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
- [ ] **Step 2: Commit**
```bash
git add backend/main.py
git commit -m "feat: implement fastapi endpoint"
```


