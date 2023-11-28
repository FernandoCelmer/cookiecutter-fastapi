from fastapi import APIRouter

router = APIRouter()


@router.get("/item")
{%- if cookiecutter.use_async == 'y' %}
async def get():
    return {"resource": "item"}
{%- endif %}

@router.get("/item")
{%- if cookiecutter.use_async == 'ns' %}
def get():
    return {"resource": "item"}
{%- endif %}
