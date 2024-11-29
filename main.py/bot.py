from pyrogram import Client, filters

API_ID = "21989020"
API_HASH = "3959305ae244126404702aa5068ba15c"
BOT_TOKEN = "7410194228:AAGyVEIgppL2tusKBIG_f-PI0XMwuD4uY1Y"

Pyxen = Client(
  name="pyxn",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

@Pyxen.on_message(filters.command("start"))
async def start_cmd(client, message):
  await message.reply_text("Hi 👋")
  
print("Bot was started")

Pyxen.run()
