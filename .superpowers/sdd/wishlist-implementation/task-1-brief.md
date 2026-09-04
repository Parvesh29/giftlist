: Backend Scaffolding and Schemas

**Files:**
- Create: `backend/requirements.txt`
- Create: `backend/schemas.py`

**Interfaces:**
- Produces: `WishlistRequest` Pydantic model in `backend/schemas.py`.

- [ ] **Step 1: Create requirements.txt**
```text
fastapi
uvicorn
pydantic
python-dotenv
```
- [ ] **Step 2: Define WishlistRequest schema**
```python
from pydantic import BaseModel, HttpUrl

class WishlistRequest(BaseModel):
    name: str
    item_names: str
    priority: str
    item_link: HttpUrl
```
- [ ] **Step 3: Commit**
```bash
git add backend/requirements.txt backend/schemas.py
git commit -m "feat: backend scaffolding and schemas"
```


