diff --git a/backend/main.py b/backend/main.py
new file mode 100644
index 0000000..26641d8
--- /dev/null
+++ b/backend/main.py
@@ -0,0 +1,21 @@
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
