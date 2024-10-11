from fastapi.templating import Jinja2Templates
import motor.motor_asyncio
from dotenv import dotenv_values
import jwt

env = dotenv_values("./creds.env")
client = motor.motor_asyncio.AsyncIOMotorClient(env["mongo_url"])
db = client["secretsociety"]
userdb = db["users"]
scannedb = db["scanned"]
templates = Jinja2Templates(directory="templates")

jwt_secret = env["jwt_secret"]
account_webhook = env["account_webhook"]
qr_webhook = env["qr_webhook"]

def authenticator(token)->dict:
    if token == None:
        return {}
    try:
        data = jwt.decode(token, jwt_secret, "HS256")
        return data
    except:
        return {}