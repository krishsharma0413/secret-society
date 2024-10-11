"""
[ TODO ]
1. complete code for creator.
2. complete code for panel.
"""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from variables import userdb, authenticator, templates, jwt_secret, scannedb, account_webhook
import jwt
from datetime import datetime
from pytz import timezone
from discord_webhook import DiscordWebhook

india_ist = timezone('Asia/Kolkata')

admin_route = APIRouter(
    prefix="/admin"
)

@admin_route.get("/")
async def admin_home(request: Request):
    data = authenticator(request.cookies.get("token"))
    if not data or not data["admin"]:
        return RedirectResponse("/")
    
    superadmin = False
    if data["_id"] == "krish" or data["_id"] == "shaurya":
        superadmin = True
    
    return templates.TemplateResponse(
        "admin_menu.html",
        {
            "request": request,
            "superadmin": superadmin
        }
    )
    
@admin_route.get("/creator")
async def admin_creator(request: Request):
    data = authenticator(request.cookies.get("token"))
    if not data or not data["admin"]:
        return RedirectResponse("/")
    return templates.TemplateResponse(
        "admin_creator.html",
        {
            "request": request
        }
    )

@admin_route.get("/admin-creator")
async def admin_creator(request: Request):
    data = authenticator(request.cookies.get("token"))
    if not data or not data["admin"]:
        return RedirectResponse("/")
    return templates.TemplateResponse(
        "admin_admin_creator.html",
        {
            "request": request
        }
    )


    
default_user_template = """
<hr class="h-[1px] bg-text">
<a href="/admin/users/{0}" class="text-text font-bokor text-6xl p-3">{0}</a>
"""

@admin_route.get("/panel")
async def admin_panel(request: Request):
    data = authenticator(request.cookies.get("token"))
    if not data or not data["admin"]:
        return RedirectResponse("/")
    
    a = await userdb.find({}).to_list(length=1000)
    all_users = ""
    for x in a:
        all_users += default_user_template.format(x["_id"])
        
    return templates.TemplateResponse(
        "admin_panel.html",
        {
            "request": request,
            "all_users": all_users
        }
    )


users_template = """
<tr>
    <td class="border-2 px-2 font-bokor text-background text-center text-xl border-background">{0}</td>
    <td class="border-2 px-2 font-bokor text-background text-center text-xl border-background">{1}</td>
</tr>
"""

@admin_route.get("/register")
async def admin_register(request: Request, username: str, password: str):
    admindata = authenticator(request.cookies.get("token"))
    if not admindata or not admindata["admin"]:
        return RedirectResponse("/")

    data = await userdb.find_one({"_id": username})
    if not data:
        if not (admindata["_id"] == "krish" or admindata["_id"] == "shaurya"):
            return templates.TemplateResponse(
                "error.html",
                {
                    "request": request,
                    "heading": "403",
                    "description": "you are not allowed to create admin users. <a style='color:red !important' href='/admin'>go back</a>"
                }
            )
        userdb.insert_one(
            {
                "_id": username,
                "password": password,
                "admin": True,
                "token": jwt.encode({"_id": username, "admin": True}, jwt_secret, algorithm="HS256"),
                "lastscanned": ""
            }
        )
        try:
            webhook = DiscordWebhook(url=account_webhook)
            webhook.set_content(
                f"Account created by **{admindata['_id']}** for ADMIN **{username}** at time {datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')} IST"
            )
            resp = webhook.execute()
        except:
            pass
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "heading": "done",
                "description": "user created. <a style='color:red !important' href='/admin'>go back</a>"
            }
        )
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "heading": "400",
            "description": "user already exists. <a style='color:red !important' href='/admin'>go back</a>"
        }
    )

@admin_route.get("/users/{user_id}")
async def admin_user(request: Request, user_id: str):
    data = authenticator(request.cookies.get("token"))
    if not data or not data["admin"]:
        return RedirectResponse("/")
    
    userdata = await scannedb.find({"id": user_id}).to_list(length=1000)
    if not userdata:
        userdata = []
    userdata.sort(key=lambda x: x["time"], reverse=True)
    a  = ""
    for x in userdata:
        a += users_template.format(x["qr"], x["time"] + " IST")
    return templates.TemplateResponse(
        "users.html",
        {
            "request": request,
            "userdata": a
        }
    )