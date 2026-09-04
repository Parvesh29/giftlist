from pydantic import BaseModel, HttpUrl

class WishlistRequest(BaseModel):
    name: str
    item_names: str
    priority: str
    item_link: HttpUrl
