from fastapi import APIRouter

router = APIRouter()


@router.get("/item")
{%- if cookiecutter.use_async == 'y' %}
async def get():
{%- elif cookiecutter.use_async == 'n' %}
def get():
{%- endif %}
    return {"resource": "item"}
