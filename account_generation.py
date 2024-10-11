"""
This code used the registration data from the google forms and generates accounts for the participants.
"""

from asyncio import run
from variables import userdb, authenticator, templates, jwt_secret
import csv
import jwt

async def generate_accounts():
    data = []
    start = 1
    exceldata = [
        ['Timestamp',
        'Team Name:',
        'Member 1 Name: ',
        'Member 1 Registration Number: ',
        'Member 1 Outlook Email ID: ',
        'Member 1 Whatsapp Number: ',
        ' Member 2 Name: ',
        ' Member 2 Registration Number: ',
        'Member 2 Outlook Email ID: ',
        'Member 2 Whatsapp Number:',
        'Member 3 Name: ',
        ' Member 3 Registration Number:',
        ' Member 3 Outlook Email ID: ',
        'Member 3 Whatsapp Number:',
        'Payment Screenshot',
        "Username",
        "Password"]
    ]
    inserted = open("./final_reg.csv", "w", newline="")
    inserted_writer = csv.writer(inserted)
    with open("./reg.csv", "r") as f:
        reader = csv.reader(f)
        for row in list(reader)[1:]:
            password = row[5].strip().replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").lower()
            username = "acm" + str(start).zfill(3)
            data.append(
                {
                    "_id": username,
                    "password": password,
                    "admin": False,
                    "token": jwt.encode({"_id": username, "admin": False}, jwt_secret, algorithm="HS256"),
                    "lastscanned": "root"
                }
            )
            
            row.append(username)
            row.append(password)
            exceldata.append(row)
            start += 1
            


    # await userdb.insert_many(data)
    inserted_writer.writerows(exceldata)

run(generate_accounts())