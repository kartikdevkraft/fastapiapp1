from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int # Include the ID in the response

    class Config:
        from_attributes = True # This allows Pydantic to read SQLAlchemy models