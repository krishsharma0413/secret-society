from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from variables import authenticator, userdb, templates, account_webhook, scannedb, qr_webhook
from relations import main_relation, all_possible, redirecturl
from discord_webhook import DiscordEmbed, DiscordWebhook
from datetime import datetime
from pytz import timezone

india_ist = timezone('Asia/Kolkata')


qr_route = APIRouter(
    prefix="/qr"
)

@qr_route.get("/{qr_id}")
async def qr_page(request: Request, qr_id: str):
    if qr_id not in all_possible:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "heading": "404", "description": "this content doesn't exist."}
        )
    data = authenticator(request.cookies.get("token"))
    if data:
        userdata = await userdb.find_one({"_id": data["_id"]})
        if userdata["lastscanned"] == "":
            await userdb.update_one({"_id": data["_id"]}, {"$set": {"lastscanned": qr_id}})
            await scannedb.insert_one({
                "id": data["_id"],
                "qr": qr_id,
                "time": datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')
            })
            try:
                webhook = DiscordWebhook(url=qr_webhook)
                webhook.set_content(f"User **{data['_id']}** scanned QR code **{qr_id}** at time {datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')} IST")
                resp = webhook.execute()
            except:
                pass
            return templates.TemplateResponse(
                "loading.html",
                {"request": request, "qr_id": qr_id, "redirect": redirecturl[qr_id]}
            )
        
        ddata = await scannedb.find({"id": data["_id"]}).to_list(length=1000)
        aaa = []
        for i in ddata:
            aaa.append(i["qr"])
            
        if qr_id in aaa:
            return templates.TemplateResponse(
                "loading.html",
                {"request": request, "qr_id": qr_id, "redirect": redirecturl[qr_id]}
            )
        
        if qr_id not in main_relation[userdata["lastscanned"]]:
            return templates.TemplateResponse(
                "error.html",
                {"request": request, "heading": "404", "description": "not your path."}
            )
        else:
            await userdb.update_one({"_id": data["_id"]}, {"$set": {"lastscanned": qr_id}})
            await scannedb.insert_one({
                "id": data["_id"],
                "qr": qr_id,
                "time": datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')
            })
            try:
                webhook = DiscordWebhook(url=qr_webhook)
                webhook.set_content(f"User **{data['_id']}** scanned QR code **{qr_id}** at time {datetime.now(india_ist).strftime('%Y-%m-%d %H:%M:%S')} IST")
                resp = webhook.execute()
            except:
                pass
            return templates.TemplateResponse(
                "loading.html",
                {"request": request, "qr_id": qr_id, "redirect": redirecturl[qr_id]}
            )
    return RedirectResponse("/login")