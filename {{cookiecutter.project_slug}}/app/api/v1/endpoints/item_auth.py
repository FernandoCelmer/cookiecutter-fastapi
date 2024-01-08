from fastapi import Depends, APIRouter
from app.core.auth.security import authorization

router = APIRouter()


@router.get("/item")
{%- if cookiecutter.use_async == 'y' %}
async def get(auth=Depends(authorization)):
{%- elif cookiecutter.use_async == 'n' %}
def get(auth=Depends(authorization)):
{%- endif %}
    return {"resource": "item"}
