from fastapi import APIRouter,status, Response
from enum import Enum
from typing import Optional



router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)



# @router.get("/blog/all")
# def get_all_blogs():
#     return {'message': 'All blogs'}


# Query Parameters example
@router.get("/all", tags=["blog"], summary="요약해보자", description="설명해보자", response_description="리스폰스 결과 설명")
def get_all_blogs(page: int, page_size: int):
    return {'message': f'All blogs - Page: {page}, Page Size: {page_size}'}

# Optional Parameters
@router.get("/optional")
def get_optional_blogs(page: int = 1, page_size: Optional[int] = None):
    return {'message': f'All blogs - Page: {page}, Page Size: {page_size}'}

#Query & path parameters
@router.get("/{id}/comments/{comment_id}")
def get_blog_comments(id: int, comment_id: int, valid:bool = True, username: Optional[str] = None):
    """ 
     Simulates retrieving a blog post and its comments based on the provided parameters.
        - **id** The ID of the blog post (path parameter).
        - **comment_id** The ID of the comment (path parameter).
        - **valid** A boolean indicating if the comment is valid (query parameter, default is True).
        - **username** An optional username associated with the comment (query parameter).
    """
    return {'message': f'Blog with id {id}, comment id {comment_id}, valid: {valid}, username: {username}'}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"
    
# Predefined values
@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}


# 만약 blog/all 이 먼저 오게 된다면, all 이 id 로 인식되어 오류가 발생할 수 있다.
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):

    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}

