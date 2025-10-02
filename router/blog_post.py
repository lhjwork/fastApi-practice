from typing import Optional, List
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool] 


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id:int, version: int = 1):
    return {"data": blog, "id": id, "version": version}

# Parameter metadata
@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id:int, comment_id : int = Query(None, title="Comment ID123143", description="The ID of the comment", alias="commentId", deprecated=True), content : str = Body(..., min_length=10, max_length=50 , regex="^[a-z\s]*$"), v : Optional[List[str]] = Query(["1.0", "1.1","2.0"])):
    return {"blog": blog, "id": id, "comment_id": comment_id, "content": content, "version": v}


