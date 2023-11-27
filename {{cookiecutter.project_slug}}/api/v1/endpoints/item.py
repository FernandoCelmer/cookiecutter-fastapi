from fastapi import APIRouter

router = APIRouter()


@router.get("/item")
def get():
    return {"resource": "item"}
