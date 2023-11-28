from fastapi import APIRouter

router = APIRouter()


@router.get("/item")
{%- if cookiecutter.use_async == 'y' %}
async def get():
{%- endif %}
{%- if cookiecutter.use_async == 'ns' %}
def get():
{%- endif %}
    return {"resource": "item"}
