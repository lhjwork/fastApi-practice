from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

routet = APIRouter(
    prefix="/blog",
    tags=["blog"],
)
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool] 


@routet.post("/new/{id}")
def create_blog(blog: BlogModel, id:int, version: int = 1):
    return {"data": blog, "id": id, "version": version}

