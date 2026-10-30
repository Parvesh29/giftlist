from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import WishlistRequest
from .email_service import send_wishlist_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Backend is running!"}

@app.post("/submit-wishlist")
async def submit_wishlist(request: WishlistRequest):
    try:
        send_wishlist_email(request)
        return {"message": "Wishlist sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
