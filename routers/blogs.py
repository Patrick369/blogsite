from fastapi import APIRouter

router = APIRouter()


@router.get("/blogs", tags=['blogs'])
def get_blog_list():
    return ['']


@router.get("/{username}/blogs", tags=["blogs"])
def get_blog_by_author(username: str):
    return ['']
