from fastapi import APIRouter

router = APIRouter()

{%- if cookiecutter.use_serverless == 'y' %}
handler = Mangum(app)
{%- endif %}

@router.get("/item")
{{ async def if cookiecutter.use_serverless == 'y' else def }} get():
    return {"resource": "item"}
