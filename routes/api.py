from fastapi import APIRouter
from fastapi import Request
from schemas.login import Login
from variables import userdb, authenticator, templates, jwt_secret, account_webhook
from fastapi.responses import RedirectResponse
import jwt
from discord_webhook import DiscordWebhook
from datetime import datetime
from pytz import timezone

india_ist = timezone('Asia/Kolkata')

api_route = APIRouter(
    prefix="/api"
)


@api_route.get("/login")
async def api_login(request: Request, username: str, password: str):
    data = await userdb.find_one({"_id": username})
    if data and data["password"] == password:
        if data["admin"]:
            redirect = RedirectResponse("/admin")
            redirect.set_cookie(
                "token", data["token"], expires=28800)  # 8 hours
            return redirect
        else:
            redirect = RedirectResponse("/menu")
            redirect.set_cookie(
                "token", data["token"], expires=28800)  # 8 hours
            return redirect
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "heading": "400",
            "description": "invalid credentials. <a style='color:red !important' href='/login'>go back</a>"
        }
    )
    
@api_route.get("/change-password")
async def api_changepassword(request: Request, password: str):
    data = authenticator(request.cookies.get("token"))
    if data:
        user = await userdb.find_one({"_id": data["_id"]})
        if user:
            await userdb.update_one({"_id": data["_id"]}, {"$set": {"password": password}})
            return templates.TemplateResponse(
                "error.html",
                {
                    "request": request,
                    "heading": "done",
                    "description": "password changed. <a style='color:red !important' href='/menu'>go back</a>"
                }
            )
    return RedirectResponse("/login")

@api_route.get("/register")
async def api_register(request: Request, username: str, password: str):
    admindata = authenticator(request.cookies.get("token"))
    if not admindata or not admindata["admin"]:
        return RedirectResponse("/")

    data = await userdb.find_one({"_id": username})
    if not data:
        userdb.insert_one(
            {
                "_id": username,
                "password": password,
                "admin": False,
                "token": jwt.encode({"_id": username, "admin": False}, jwt_secret, algorithm="HS256"),
                "lastscanned": "root"
            }
        )
        try:
            webhook = DiscordWebhook(url=account_webhook)
            webhook.set_content(
                f"Account created by **{admindata['_id']}** for user **{username}** at time {datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')} IST"
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


@api_route.get("/logout")
async def api_logout(request: Request):
    data = authenticator(request.cookies.get("token"))
    if data:
        redirect = RedirectResponse("/")
        redirect.delete_cookie("token")
        return redirect
    return RedirectResponse("/")
