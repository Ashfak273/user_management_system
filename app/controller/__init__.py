from fastapi import APIRouter
from starlette.responses import HTMLResponse
from app.controller.user_controller import router as user_router

all_routers = APIRouter()
all_routers.include_router(user_router)


@all_routers.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>User Management</title>
        </head>
        <body>
            <h1>Welcome to User Management System</h1>
        </body>
    </html> 
    """
    return HTMLResponse(content=html_content)
