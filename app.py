from fastapi import Request, FastAPI
from variables import templates, userdb, authenticator
from routes.qr import qr_route
from routes.api import api_route
from routes.archive import archive_route
from routes.admin import admin_route
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import jwt

app = FastAPI(redoc_url=None, docs_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(qr_route)
app.include_router(api_route)
app.include_router(admin_route)
app.include_router(archive_route)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    if authenticator(request.cookies.get("token")):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "state": "play",
                "url": "/menu"
            }
        )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "state": "play",
            "url": "/login"
        }
    )

@app.get("/change-password", response_class=HTMLResponse)
async def changepassword_page(request: Request):
    data = authenticator(request.cookies.get("token"))
    if data:
        return templates.TemplateResponse(
            "change_password.html",
            {
                "request": request
            }
        )
    return RedirectResponse("/login")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )
    
@app.get("/menu", response_class=HTMLResponse)
async def menu_page(request: Request):
    data = authenticator(request.cookies.get("token"))
    if data:
        return templates.TemplateResponse(
            "menu.html",
            {
                "request": request
            }
        )
    return RedirectResponse("/login")