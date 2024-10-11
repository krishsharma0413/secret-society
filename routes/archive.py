from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from variables import userdb, authenticator, templates, jwt_secret, scannedb
import jwt
from relations import redirecturl

archive_route = APIRouter(
    prefix="/archive"
)
default_archive_template = """
<hr class="h-[1px] bg-text">
<a href="/archive/{0}" class="text-text font-stalber cryptic text-6xl md:text-8xl p-3" data-value="{0}">{0}</a>
"""

@archive_route.get("/")
async def archive_home(request: Request):
    data = authenticator(request.cookies.get("token"))
    if data:
        all_archives = await scannedb.find({"id": data["_id"]}).to_list(length=100)
        all_archives.sort(key=lambda x: x["time"], reverse=True)
        archive = ""
        for x in all_archives:
            archive += default_archive_template.format(x["qr"])
        return templates.TemplateResponse(
            "archive.html",
            {
                "request": request,
                "archive": archive
            }
        )
        
    return RedirectResponse("/login")
   
@archive_route.get("/{archive_id}")
async def admin_creator(request: Request, archive_id: str):
    data = authenticator(request.cookies.get("token"))
    if data:
        archive = await scannedb.find_one({"id": data["_id"], "qr": archive_id})
        if archive:
            return RedirectResponse(redirecturl[archive_id])
    
    return RedirectResponse("/login")
        