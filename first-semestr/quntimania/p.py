from telethon import TelegramClient
from telethon.tl.types import Channel

api_id = 31243406
api_hash = "78b843bbf5fbf8cfda1a633a23210058"

client = TelegramClient("session_mr", api_id, api_hash)

TARGET_FULL = -1003109382452

async def main():
    me = await client.get_me()
    print("Logged in as:", me.id)

    target_id = abs(TARGET_FULL)
    if str(target_id).startswith("100"):
        target_id = int(str(target_id)[3:])  # -100XXXXXXXXXX -> XXXXXXXXXX

    found = False
    async for d in client.iter_dialogs():
        ent = d.entity
        if isinstance(ent, Channel) and getattr(ent, "id", None) == target_id:
            found = True
            print("\nFOUND CHANNEL IN YOUR DIALOGS")
            print("Title:", getattr(ent, "title", None))
            print("Username:", getattr(ent, "username", None))
            print("ID:", ent.id)
            print("Access hash:", getattr(ent, "access_hash", None))
            break

    if not found:
        print("\nNOT FOUND in your dialogs.")
        print("Demak, siz bu kanalga a'zo emassiz yoki kanal private va account uni 'bilmaydi'.")

with client:
    client.loop.run_until_complete(main())
