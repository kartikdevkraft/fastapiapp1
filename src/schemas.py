from pydantic import BaseModel
from typing import Optional

# Base schema with shared fields
class PostBase(BaseModel):
    title: str
    content: str

# Schema for creating a new post (requires all fields)
class PostCreate(PostBase):
    pass

# NEW: Schema for partial updates (all fields optional)
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# Schema for returning data to the user (includes the ID)
class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True # Allows Pydantic to read SQLAlchemy models